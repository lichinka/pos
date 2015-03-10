from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company (models.Model):
    """
    The Company model represents a firm using the system
    """
    name = models.CharField (verbose_name=_('name'),
                             max_length=255)
    address = models.CharField (verbose_name=_('address'),
                                max_length=255)
    email = models.EmailField (verbose_name=_('e-mail'))
    identification = models.CharField (verbose_name=_('tax identification number'),
                                       max_length=255)
    
    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __unicode__ (self):
        return self.name



class Store (models.Model):
    """
    The Store model represents a business unit inside a Company
    """
    name = models.CharField (verbose_name=_('name'),
                             max_length=255)
    address = models.CharField (verbose_name=_('address'),
                                max_length=255)
    telephone = models.CharField (verbose_name=_('telephone number'),
                                  max_length=100)
    company = models.ForeignKey (Company,
                                 verbose_name=_('company'))

    class Meta:
        verbose_name = _('store')
        verbose_name_plural = _('stores')

    def __unicode__ (self):
        return self.name
    


class Terminal (models.Model):
    """
    The Terminal model represents one cash terminal running inside a Store
    """
    name = models.CharField (verbose_name=_('name'),
                             max_length=100)
    store = models.ForeignKey (Store,
                               verbose_name=_('store'))

    class Meta:
        verbose_name = _('terminal')
        verbose_name_plural = _('terminals')

    def __unicode__ (self):
        return "%s - %s" % (self.store.name, self.name)
    


class Terminal_configuration (models.Model):
    """
    The Terminal_configuration model holds all system settings for one Terminal
    """
    key = models.CharField (verbose_name=_('key'),
                            max_length=100)
    value = models.CharField (verbose_name=_('value'),
                              max_length=100)
    terminal = models.ForeignKey (Terminal,
                                  verbose_name=_('terminal'))

    class Meta:
        verbose_name = _('terminal configuration')
        verbose_name_plural = _('terminal configuration values')

    def __unicode__ (self):
        return self.key + ' => ' + self.value
    
