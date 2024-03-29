from django.db import models
from apps.ledger.models import Account
from apps.users.models import Company, File
from awecounting.utils.helpers import get_next_voucher_no
from django.utils.translation import ugettext_lazy as _
from njango.fields import BSDateField, today
from django.contrib.contenttypes.fields import GenericRelation


class BankAccount(models.Model):
    bank_name = models.CharField(max_length=254)
    ac_no = models.CharField(max_length=50, verbose_name=_('Account No.'))
    branch_name = models.CharField(max_length=254, blank=True, null=True)
    account = models.OneToOneField(Account)
    company = models.ForeignKey(Company)

    def save(self, *args, **kwargs):
        if self.pk is None:
            account = Account(code=self.ac_no[-10:], name=self.bank_name + ' Account (' + str(self.ac_no) + ' )')
            account.company = self.company
            account.add_category('Bank Account')
            account.save()
            self.account = account
        super(BankAccount, self).save(*args, **kwargs)

    def __str__(self):
        if self.ac_no:
            return self.bank_name + ' Account (' + str(self.ac_no) + ' )'
        else:
            return self.bank_name + ' Account '


class ChequeDeposit(models.Model):
    voucher_no = models.IntegerField()
    date = BSDateField(default=today)
    bank_account = models.ForeignKey(Account, related_name='cheque_deposits')
    clearing_date = BSDateField(default=today, null=True, blank=True)
    benefactor = models.ForeignKey(Account)
    deposited_by = models.CharField(max_length=254, blank=True, null=True)
    narration = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company)
    files = models.ManyToManyField(File, blank=True)

    def __init__(self, *args, **kwargs):
        super(ChequeDeposit, self).__init__(*args, **kwargs)
        if not self.pk and not self.voucher_no:
            self.voucher_no = get_next_voucher_no(ChequeDeposit, self.company_id)

    def __str__(self):
        return str(self.voucher_no) + ' : ' + str(self.deposited_by)

    def get_voucher_no(self):
        return self.id

    class Meta:
        unique_together = ('voucher_no', 'company')

    @property
    def total(self):
        grand_total = 0
        for obj in self.rows.all():
            total = obj.amount
            grand_total += total
        return grand_total


class ChequeDepositRow(models.Model):
    sn = models.IntegerField()
    cheque_number = models.CharField(max_length=50, blank=True, null=True)
    cheque_date = BSDateField(default=today, null=True, blank=True)
    drawee_bank = models.CharField(max_length=254, blank=True, null=True)
    drawee_bank_address = models.CharField(max_length=254, blank=True, null=True)
    amount = models.FloatField()
    cheque_deposit = models.ForeignKey(ChequeDeposit, related_name='rows')

    def get_absolute_url(self):
        return self.cheque_deposit.get_absolute_url()

    def get_voucher_no(self):
        return self.cheque_deposit.id


class BankCashDeposit(models.Model):
    voucher_no = models.IntegerField()
    date = BSDateField(default=today)
    bank_account = models.ForeignKey(Account, related_name='cash_deposits')
    benefactor = models.ForeignKey(Account)
    amount = models.FloatField()
    deposited_by = models.CharField(max_length=254, blank=True, null=True)
    narration = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company)

    def __init__(self, *args, **kwargs):
        super(BankCashDeposit, self).__init__(*args, **kwargs)
        if not self.pk and not self.voucher_no:
            self.voucher_no = get_next_voucher_no(BankCashDeposit, self.company_id)

    def get_voucher_no(self):
        return self.id

    class Meta:
        unique_together = ('voucher_no', 'company')


class ChequePayment(models.Model):
    cheque_number = models.CharField(max_length=50)
    date = BSDateField(default=today, null=True, blank=True)
    beneficiary = models.ForeignKey(Account)
    bank_account = models.ForeignKey(Account, related_name='cheque_payments')
    amount = models.FloatField()
    narration = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company)

    def get_voucher_no(self):
        return self.cheque_number