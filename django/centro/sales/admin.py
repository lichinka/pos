from django import forms
from django.forms import widgets
from django.contrib import admin
from sales.models import Payment, Sale, SaleDetail, SaleTax
from sales.models import PaymentTranslation
from multilingual_model.admin import TranslationInline


class PaymentTranslationInline (TranslationInline):
    """
    Displays Payment translations as inlined forms.
    """
    model = PaymentTranslation


class PaymentAdmin (admin.ModelAdmin):
    inlines = [PaymentTranslationInline]
    order = ['sort']


class SaleDetailInline (admin.StackedInline):
    """
    Displays the sale details, inlined with the sale header.
    """
    model = SaleDetail
    extra = 1


class SaleAdmin (admin.ModelAdmin):
    inlines = [SaleDetailInline]
    list_display = ['date_time', 'number', 'completed']


admin.site.register (Sale, SaleAdmin)
admin.site.register (SaleTax)
admin.site.register (Payment, PaymentAdmin)
