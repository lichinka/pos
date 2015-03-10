from django.contrib import admin
from companies.models import Company, Store, Terminal


class TerminalAdmin (admin.StackedInline):
    """
    Defines a stacked view for Terminals to be displayed
    within the corresponding Store.
    """
    model = Terminal
    extra = 1


class StoreAdmin (admin.ModelAdmin):
    """
    Defines the look of the Store administration interface.
    """
    inlines = [TerminalAdmin]
    list_display = ('name', 'company', 'address', 'telephone')


class CompanyAdmin (admin.ModelAdmin):
    """
    Defines the look of the Company administration interface.
    """
    fields = ['name', 'email', 'address', 'identification']
    list_display = ('name', 'address', 'email')


admin.site.register (Company, CompanyAdmin)
admin.site.register (Store, StoreAdmin)
