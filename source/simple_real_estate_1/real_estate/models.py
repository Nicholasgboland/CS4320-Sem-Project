# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.views import generic

class ExpenseRecord(models.Model):
    expense_record_id = models.BigAutoField(primary_key=True)
    expense_report_date = models.DateField()
    property = models.ForeignKey('Property', models.DO_NOTHING)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    expense_total = models.TextField()  # This field type is a guess.
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'expense_record'


class ExpenseRecordItem(models.Model):
    expense_item_id = models.BigAutoField(primary_key=True)
    expense_record = models.ForeignKey(ExpenseRecord, models.DO_NOTHING)
    expense_item_name = models.TextField()

    expense_item_cost = models.IntegerField(blank=True, null=True)  # This field type is a guess.

    expense_type = models.TextField()
    expense_category = models.TextField(null=True)
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'expense_record_item'


class MaintQuote(models.Model):
    maint_quote_id = models.BigAutoField(primary_key=True)
    maint_record = models.ForeignKey('MaintRecord', models.DO_NOTHING)
    maint_quote_date = models.DateField()
    quote_total = models.TextField()

    class Meta:
        managed = True
        db_table = 'maint_quote'


class MaintQuoteInvoice(models.Model):
    maint_invoice_id = models.BigAutoField(primary_key=True)
    maint_quote = models.ForeignKey(MaintQuote, models.DO_NOTHING)
    issue_date = models.DateField()
    check_num = models.TextField(null=True)
    amount_paid = models.TextField()
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'maint_quote_invoice'


class MaintQuoteItem(models.Model):
    quote_item_id = models.BigAutoField(primary_key=True)
    maint_quote = models.ForeignKey(MaintQuote, models.DO_NOTHING)
    quote_item_name = models.TextField()
    quote_item_cost = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maint_quote_item'


class MaintRecord(models.Model):
    maint_record_id = models.BigAutoField(primary_key=True)
    maint_record_date = models.DateField()
    property = models.ForeignKey('Property', models.DO_NOTHING, null=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'maint_record'


class MaintRecordItem(models.Model):
    maint_item_id = models.BigAutoField(primary_key=True)
    maint_record = models.ForeignKey(MaintRecord, models.DO_NOTHING)
    maint_item_name = models.TextField()
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'maint_record_item'


class Property(models.Model):
    property_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    street_addr = models.TextField()
    city = models.TextField()
    county = models.TextField(null=True)
    state_abrv = models.TextField()
    zip = models.TextField()
    purchase_date = models.DateField(blank=True, null=True)
    sqr_ft = models.TextField(blank=True, null=True)
    price_per_sqqr_ft = models.TextField(blank=True, null=True)
    purchase_price = models.TextField(blank=True, null=True)
    market_price = models.TextField(blank=True, null=True)
    num_of_units = models.TextField(blank=True, null=True)
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'property'
class PropertyListView(generic.ListView):
    model = Property

class RentalAgreement(models.Model):
    agreement_id = models.BigAutoField(primary_key=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING)
    tenant = models.ForeignKey('Tenant', models.DO_NOTHING)
    contract_num = models.TextField(null=True)
    contract_docs = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    curr_rent = models.TextField()
    accepted = models.BooleanField()
    active = models.BooleanField()
    payment_sched = models.TextField(null=True)
    notes = models.TextField(null=True)
    next_increase = models.DateField(blank=True, null=True)
    last_increase = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rental_agreement'


class RentalInvoice(models.Model):
    invoice_id = models.BigAutoField(primary_key=True)
    issue_date = models.DateField()
    cash_date = models.DateField(blank=True, null=True)
    check_num = models.TextField(null=True)
    agreement = models.ForeignKey(RentalAgreement, models.DO_NOTHING)
    tenant = models.ForeignKey('Tenant', models.DO_NOTHING)
    amount_paid = models.TextField()
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'rental_invoice'


class Tenant(models.Model):
    tenant_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'tenant'


class Unit(models.Model):
    unit_id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(Property, models.DO_NOTHING)
    name = models.TextField()
    unit_number = models.TextField()
    sqr_ft = models.TextField(blank=True, null=True)
    price_per_sqqr_ft = models.TextField(blank=True, null=True)
    notes = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'unit'
