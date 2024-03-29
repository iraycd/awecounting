$(document).ready(function () {
    vm = new SaleViewModel(ko_data);
    ko.applyBindings(vm);
});

function SaleViewModel(data) {
    var self = this;

    for (var k in data)
        self[k] = ko.observable(data[k]);

    self.party = ko.observable();
    self.status = ko.observable();

    $.ajax({
        url: '/inventory/api/items.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.items = ko.observableArray(data);
        }
    });

    $.ajax({
        url: '/ledger/api/parties_with_balance.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.parties = ko.observableArray(data);
        }
    });

    $.ajax({
        url: '/inventory/api/units.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.units = ko.observableArray(data);
        }
    });

    self.party_balance = ko.computed(function () {
        if (self.party())
            return self.party().balance;
    });

    self.table_view = new TableViewModel({rows: data.rows, argument: self}, SaleRow);

    self.save = function (item, event) {
        if (self.credit() && !self.party()) {
            bsalert.error('Party is required for credit sale!');
            return false;
        }
        $.ajax({
            type: "POST",
            url: '/voucher/sale/save/',
            data: ko.toJSON(self),
            success: function (msg) {
                if (msg.id)
                    self.id(msg.id);
                if (typeof (msg.error_message) != 'undefined') {
                    bsalert.error(msg.error_message);
                    self.status('errorlist');
                }
                else {
                    bsalert.success('Saved!');
                    self.table_view.deleted_rows([]);
                    $("tbody > tr").each(function (i) {
                        $($("tbody > tr:not(.total)")[i]).addClass('invalid-row');
                    });
                    for (var i in msg.rows) {
                        self.table_view.rows()[i].id = msg.rows[i];
                        $($("tbody > tr")[i]).removeClass('invalid-row');
                    }
                }
            }
        });
    }

    self.id.subscribe(function (id) {
        update_url_with_id(id);
    });

    self.sub_total = function () {
        var sum = 0;
        self.table_view.rows().forEach(function (i) {
            if (i.total()) {
                sum += parseFloat(i.total());
            }
        });
        return round2(sum);
    }
}


function SaleRow(row, sale_vm) {
    var self = this;

    self.item = ko.observable();
    self.item_id = ko.observable();
    self.quantity = ko.observable();
    self.rate = ko.observable();
    self.discount = ko.observable(0);
    self.unit = ko.observable();
    self.unit_id = ko.observable();

    for (var k in row)
        self[k] = ko.observable(row[k]);

    self.item.subscribe(function (item) {
        if (item.unit) {
            var unit = get_by_id(sale_vm.units(), item.unit.id);
            if (!self.unit_id())
                self.unit_id(unit.id);
            if (!self.rate()) {
                self.rate(item.selling_rate);
            }
        }
    });

    self.unit.subscription_changed(function (new_val, old_val) {
        if (old_val && old_val != new_val) {
            var conversion_rate = old_val.convertible_units[new_val.id];
            if (conversion_rate) {
                if (self.quantity()) {
                    self.quantity(self.quantity() * conversion_rate);
                }
                if (self.rate()) {
                    self.rate(self.rate() / conversion_rate);
                }
            }
        }
    });

    self.total = ko.computed(function () {
        if (self.discount() > 0) {
            var total = self.quantity() * self.rate();
            return round2(total - self.discount());
        } else {
            return round2(self.quantity() * self.rate());
        }
    });

    //self.render_selected_unit = function (data) {
    //    var obj = get_by_id(sale_vm.units(), data.id);
    //    return '<div>' + obj.name + '</div>';
    //}

    self.render_unit_options = function (data) {
        var obj = get_by_id(sale_vm.units(), data.id);
        var klass = '';
        if (self.unit_id() && obj.id != self.unit_id()) {
            if (obj.convertible_units[self.unit_id()])
                klass = 'green';
            else
                klass = 'red';
        }
        return '<div class="' + klass + '">' + obj.name + '</div>';
    }

    self.render_option = function (data) {
        var obj = get_by_id(sale_vm.items(), data.id);
        return '<div>' + obj.full_name + '</div>';
    }

}