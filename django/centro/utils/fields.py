from django import forms
from django.db.models.fields import DecimalField
from widgets import CurrencyWidget


class CurrencyField (DecimalField):
    """
    An extension of the built-in DecimalField to display monetary data.
    """
    def __init__(self, *args, **kwargs):
        self.places = kwargs.pop('display_decimal', 2)
        super(CurrencyField, self).__init__(*args, **kwargs)


    def formfield(self, **kwargs):
        defaults = {
            'max_digits': self.max_digits,
            'decimal_places': self.decimal_places,
            'form_class': forms.DecimalField,
            'widget': CurrencyWidget,
            'localize': True
        }
        defaults.update(kwargs)
        return super(CurrencyField, self).formfield(**defaults)

