from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from items.models import Item
from companies.models import Store, Terminal



class Stock (models.Model):
    """
    The stock model represents the current existence
    of items per store (i.e. bussiness unit)
    """
    store = models.ForeignKey (Store, 
                               null=False, 
                               blank=False,
                               verbose_name=_('store'))
    item = models.ForeignKey (Item,
                               null=False, 
                               blank=False,
                               verbose_name=_('item'))
    reorder_level = models.DecimalField (max_digits=10,
                                         decimal_places=2,
                                         null=True,
                                         blank=True,
                                         verbose_name=_('reorder level'))
    quantity = models.DecimalField (max_digits=10,
                                    decimal_places=2,
                                    null=False,
                                    blank=False,
                                    verbose_name=_('quantity'))

    class Meta:
        unique_together = ('store', 'item')
        verbose_name = _('stock')
        verbose_name_plural = _('stocks')

    def __unicode__ (self):
        return self.item.__unicode__ ( )


class StockEvent (MultilingualModel):
    """
    This model represents events that may occur on a stocked item.
    It also defines the user groups and/or users that may execute an
    event.
    """
    users = models.ManyToManyField (User,
                                    null=True,
                                    blank=True,
                                    verbose_name=_('users'))
    groups = models.ManyToManyField (Group,
                                     null=True,
                                     blank=True,
                                     verbose_name=_('groups'))
    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __unicode__ (self):
        return self.unicode_wrapper ('name')


class StockEventTranslation (MultilingualTranslation):
    """
    This class provides translation support for the StockEvent model.
    """
    parent = models.ForeignKey (StockEvent,
                                related_name='translations')
    name = models.CharField (verbose_name=_('name'),
                             max_length=100)
    description = models.CharField (verbose_name=_('description'),
                                    null=True,
                                    max_length=255)

    class Meta:
        unique_together = ('parent', 'language_code')


class StockLog (models.Model):
    """
    This model represents all movements of items within the company.
    The first log entry is always a delivery of goods; the last one
    a product sale.
    """
    date_time = models.DateTimeField (null=False,
                                      blank=False,
                                      verbose_name=_('time'))
    item = models.ForeignKey (Item,
                              null=False, 
                              blank=False,
                              verbose_name=_('item'))
    event = models.ForeignKey (StockEvent,
                               null=False,
                               blank=False,
                               verbose_name=_('event'))
    user = models.ForeignKey (User,
                              null=False,
                              blank=False,
                              verbose_name=_('user'))
    terminal = models.ForeignKey (Terminal,
                                  null=False,
                                  blank=False,
                                  verbose_name=_('terminal'))
    receipt = models.CharField (max_length=100,
                                verbose_name=_('document'))
    quantity = models.DecimalField (max_digits=10,
                                    decimal_places=2,
                                    null=False,
                                    blank=False,
                                    verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('stock log')
        verbose_name_plural = _('stock logs')

    def __unicode__ (self):
        return str(self.date_time)

