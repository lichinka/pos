from decimal import Decimal
from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from items.models import Item
from utils.fields import CurrencyField



class SaleDetail (models.Model):
    """
    The SaleDetail model represents each of the detailed entries
    within a sale (i.e. each of the sold articles).
    """
    sale = models.ForeignKey ('Sale',
                              null=False,
                              blank=False,
                              verbose_name=_('sale'))
    item = models.ForeignKey (Item,
                              null=True,
                              blank=True,
                              verbose_name=_('item'))
    comment = models.CharField (max_length=255,
                                null=True,
                                blank=True,
                                verbose_name=_('comment'))
    quantity = models.DecimalField (max_digits=10,
                                    decimal_places=2,
                                    null=False,
                                    blank=False,
                                    verbose_name=_('quantity'))
    cost_price = CurrencyField (max_digits=7,
                                decimal_places=2,
                                verbose_name=_('cost price'))
    sale_price = CurrencyField (max_digits=7,
                                decimal_places=2,
                                verbose_name=_('sale price'))
    class Meta:
        verbose_name = _('sale detail')
        verbose_name_plural = _('sale details')

    def __unicode__ (self):
        ret_value = str(self.sale)
        if (self.item):
            return '%s - %s' % (ret_value, str(self.item))
        else:
            return '%s - %s' % (ret_value, self.comment)



class SaleTax (models.Model):
    """
    The SaleDetailTax model represents each of the taxes applied
    to the detailed articles within a sale.
    """
    sale_detail = models.ForeignKey (SaleDetail,
                                     null=False,
                                     blank=False,
                                     verbose_name=_('sale detail'))
    name = models.CharField (max_length=100,
                             verbose_name=_('name'))
    percent = models.DecimalField (max_digits=4,
                                   decimal_places=2,
                                   verbose_name=_('percent'))
    class Meta:
        verbose_name = _('sale tax')
        verbose_name_plural = _('sale taxes')

    def __unicode__ (self):
        return '%s - %s' % (self.sale_detail, self.name)



class Sale (models.Model):
    """
    The Sale model represents a set of articles sold to a customer.
    """
    date_time = models.DateTimeField (null=False,
                                      blank=False,
                                      verbose_name=_('time'))
    number = models.IntegerField (null=True,
                                  blank=True,
                                  verbose_name=_('invoice number'))
    customer = models.CharField (max_length=100,
                                 verbose_name=_('customer'))
    user = models.ForeignKey (User,
                              null=False,
                              blank=False,
                              verbose_name=_('user'))
    completed = models.BooleanField (null=False,
                                     blank=False,
                                     default=False,
                                     verbose_name=_('completed'))
    class Meta:
        verbose_name = _('sale')
        verbose_name_plural = _('sales')

    def __unicode__ (self):
        return '#%s' % str(self.number)

    def get_subtotal (self):
        """
        Returns a Decimal representation of the 
        subtotal of this sale without taxes.
        """
        ret_value = Decimal ('0.0')
        details = SaleDetail.objects.filter (sale=self)
        for det in details:
            linear_tax = Decimal ('1.0')
            for tax in SaleTax.objects.filter (sale_detail=det):
                linear_tax += tax.percent / Decimal ('100.0')
            price = det.sale_price / linear_tax
            ret_value += price * det.quantity
        return ret_value

    def get_taxes (self):
        """
        Returns a Decimal representation of the taxes of this sale.
        """
        return Decimal(self.get_total ( ) - self.get_subtotal ( ))

    def get_total (self):
        """
        Returns a Decimal representation of the 
        total of this sale (i.e. subtotal+taxes).
        """
        ret_value = Decimal ('0.0')
        details = SaleDetail.objects.filter (sale=self)
        for det in details:
            ret_value += det.sale_price * det.quantity
        return ret_value

    def get_amount_paid (self):
        """
        Returns a Decimal representation of the total amount
        paid for this sale (i.e. all payments together).
        """
        ret_value = Decimal ('0.0')
        pays = SalePayment.objects.filter (sale=self)
        for pay in pays:
            ret_value += pay.amount
        return ret_value



class Payment (MultilingualModel):
    """
    The Payment model represent the diffent ways a 
    customer may pay for a given sale.
    """
    sort = models.IntegerField (null=True,
                                blank=True,
                                verbose_name=_('payment sort order'))
    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __unicode__ (self):
        return self.unicode_wrapper ('name')


class PaymentTranslation (MultilingualTranslation):
    """
    This model provides support to save some 'Payment' fields
    in different languages.
    """
    name = models.CharField (max_length=100,
                             null=False,
                             blank=False,
                             verbose_name=_('name'))
    parent = models.ForeignKey (Payment, related_name = 'translations')

    class Meta:
        unique_together = ('parent', 'language_code')


class SalePayment (models.Model):
    """
    The SalePayment model represents all payments by which a sale is payed.
    It supports combining different payment methods within the same sale.
    """
    sale = models.ForeignKey (Sale,
                              null=False,
                              blank=False,
                              verbose_name=_('sale'))
    payment = models.ForeignKey (Payment,
                                 null=False,
                                 blank=False,
                                 verbose_name=_('payment'))
    amount = CurrencyField (max_digits=7,
                            decimal_places=2,
                            verbose_name=_('amount'))
    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __unicode__ (self):
        return '%s - %s - %s' % (self.sale, self.payment, self.amount)

