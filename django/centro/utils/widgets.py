import locale
from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import escape



class BaseCurrencyWidget(forms.TextInput):
    """
    A Text Input widget that shows the currency amount
    """
    def __init__(self, attrs={}):
        final_attrs = {'class': 'vCurrencyField'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(BaseCurrencyWidget, self).__init__(attrs=final_attrs)

    def format_currency (self, value):
        """
        Returns the received value as currency in the current locale.
        """
        try:
            value = float (value)
            value = '%.2f' % (float (value))
            value = value.replace ('.', locale.localeconv( )['decimal_point'])
        except (TypeError, ValueError):
            pass
        finally:
            return value


class CurrencyWidget(BaseCurrencyWidget):
    def render(self, name, value, attrs=None):
        value = self.format_currency (value)
        rendered = super(CurrencyWidget, self).render(name, value, attrs)
        curr = locale.localeconv( )['int_curr_symbol']
        curr = curr.replace("_", "&nbsp;")
        return mark_safe('<span class="currency">%s</span>%s' % (curr, rendered))


class TruncatedCurrencyWidget(BaseCurrencyWidget):
    """
    A Text Input widget that shows the currency amount - stripped to two digits by default.
    """
    def render(self, name, value, attrs=None):
        value = self.format_currency (value)
        rendered = super(TruncatedCurrencyWidget, self).render(name, value, attrs)
        curr = locale.localeconv( )['int_curr_symbol']
        curr = curr.replace("_", "&nbsp;")
        return mark_safe('<span class="currency">%s</span>%s' % (curr, rendered))

class StrippedDecimalWidget(forms.TextInput):
    """
    A textinput widget that strips out the trailing zeroes.
    """

    def __init__(self, attrs={}):
        final_attrs = {'class': 'vDecimalField'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(StrippedDecimalWidget, self).__init__(attrs=final_attrs)

    def render(self, name, value, attrs=None):
        value = self.format_currency (value)
        return super(StrippedDecimalWidget, self).render(name, value, attrs)


class ReadOnlyWidget(forms.Widget):
    def render(self, name, value, attrs):
        final_attrs = self.build_attrs(attrs, name=name)
        if hasattr(self, 'initial'):
            value = self.initial
        if value:
            return mark_safe("<p>%s</p>" % escape(value))
        else:
            return ''

    def _has_changed(self, initial, data):
        return False

