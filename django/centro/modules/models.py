from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from django.utils.translation import ugettext_lazy as _


#
# This class provides support for saving some fields
# of the Module model in different languages.
#
class ModuleTranslation (MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Module', related_name='translations')

    name = models.CharField (verbose_name=_('name'),
                             max_length=70)
    description = models.CharField (verbose_name=_('description'),
                                    null=True,
                                    max_length=255)


#
# This model represents a module within the application.
# A module may contain submodules by specifying a parent.
# Access control should be used to enable/disable user's rights.
#
class Module (MultilingualModel):
    path = models.CharField (verbose_name=_('module relative path'),
                             max_length=100)
    sort = models.IntegerField (verbose_name=_('module sort order'),
                                null=True)
    parent = models.ForeignKey ('self', 
                                null=True, 
                                blank=True,
                                verbose_name=_('parent category'))

    class Meta:
        verbose_name = _('module')
        verbose_name_plural = _('modules')

    def __unicode__ (self):
        return self.unicode_wrapper ('name')

    @staticmethod
    def get_submodule (name):
        """
        Returns the Module object of the received submodule name.
        """
        submodules = Module.objects.filter (translations__name__in=[name]).\
                                    filter (parent__isnull=False)
        if (len(submodules) > 0):
            return submodules[0]
        else:
            #
            # unknown module
            #
            return Module.objects.get(pk=1)

