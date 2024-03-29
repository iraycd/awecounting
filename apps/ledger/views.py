from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from awecounting.utils.mixins import DeleteView, UpdateView, CreateView, AjaxableResponseMixin, CompanyView
from .models import Party, Category, Account, JournalEntry
from .forms import PartyForm, AccountForm, CategoryForm


class ViewAccount(ListView):
    model = Account
    template_name = 'view_account.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ViewAccount, self).get_context_data(**kwargs)
        base_template = 'dashboard.html'
        pk = int(self.kwargs.get('pk'))
        obj = get_object_or_404(self.model, pk=pk, company=self.request.company)
        journal_entries = JournalEntry.objects.filter(transactions__account_id=obj.pk).order_by('pk',
                                                                                                    'date') \
            .prefetch_related('transactions', 'content_type', 'transactions__account').select_related()
        context['account'] = obj
        context['journal_entries'] = journal_entries
        context['base_template'] = base_template
        return context


class CategoryView(CompanyView):
    model = Category
    success_url = reverse_lazy('category_list')
    form_class = CategoryForm

class CategoryList(CategoryView, ListView):
    pass


class CategoryCreate(AjaxableResponseMixin, CategoryView, CreateView):
    pass


class CategoryUpdate(CategoryView, UpdateView):
    pass


class CategoryDelete(CategoryView, DeleteView):
    pass



# Party CRUD with mixins
class PartyView(CompanyView):
    model = Party
    success_url = reverse_lazy('party_list')
    form_class = PartyForm


class PartyList(PartyView, ListView):
    pass


class PartyCreate(AjaxableResponseMixin, PartyView, CreateView):
    pass


class PartyUpdate(PartyView, UpdateView):
    pass


class PartyDelete(PartyView, DeleteView):
    pass


class AccountView(CompanyView):
    model = Account
    success_url = reverse_lazy('account_list')
    form_class = AccountForm


class AccountList(AccountView, ListView):
    pass


class AccountCreate(AjaxableResponseMixin, AccountView, CreateView):
    pass


class AccountUpdate(AccountView, UpdateView):
    pass


class AccountDelete(AccountView, DeleteView):
    pass
