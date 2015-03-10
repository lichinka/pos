from django import forms
from django.forms import widgets
from django.contrib import admin
from stock.models import Stock, StockEvent, StockLog
from stock.models import StockEventTranslation
from multilingual_model.admin import TranslationInline


class StockEventTranslationInline (TranslationInline):
    """
    Displays StockEvent translations as inlined forms.
    """
    model = StockEventTranslation


class StockEventAdmin (admin.ModelAdmin):
    inlines = [StockEventTranslationInline]


class StockLogForm (forms.ModelForm):
    """
    Overrides the Form definition for the Item model
    to displayed custom fields and run custom validation rules.
    """
    #date_time = forms.DateTimeInput (format='%Y-%m-%d %H:%M:%S')
    date_time = forms.DateTimeField (widget=widgets.SplitDateTimeWidget)

    class Meta:
        model = StockLog


class StockLogAdmin (admin.ModelAdmin):
    form = StockLogForm
    list_display = ['date_time', 'event', 'user']


class StockAdmin (admin.ModelAdmin):
    list_display = ['item', 'store', 'quantity']


admin.site.register (StockEvent, StockEventAdmin)
admin.site.register (StockLog, StockLogAdmin)
admin.site.register (Stock, StockAdmin)
