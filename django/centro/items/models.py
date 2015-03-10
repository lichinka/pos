from django.conf import settings
from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from django.utils.translation import ugettext_lazy as _
from utils.fields import CurrencyField

#
# The Category model represents a group of articles.
# Any category may have a parent, meaning that the category tree
# could be of any depth.
#
class Category (MultilingualModel):
    parent = models.ForeignKey ('self', 
                                null=True, 
                                blank=True,
                                verbose_name=_('parent category'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__ (self):
        return self.unicode_wrapper ('name')

    def as_tree_node (self):
        """
        Returns a string representing the tree node
        where this category is placed.
        """
        def node_depth (category, depth=0):
            """
            A recursive function to find out how deep is this
            category within the category tree.
            """
            if (category.parent is not None):
                depth = node_depth (category.parent, depth+1)
            return depth

        category_depth = node_depth (self)
        if (category_depth > 0):
            ret_value = '=' * category_depth
            ret_value = '%s> ' % ret_value
        else:
            ret_value = ' '

        ret_value = '%s%s' % (ret_value, self.__unicode__ ( ))
        return ret_value
    # Name to be displayed in the admin, as column title
    as_tree_node.short_description = _('category')


#
# This class provides support for saving some fields
# of the Category model in different languages.
#
class CategoryTranslation (MultilingualTranslation):
    parent = models.ForeignKey (Category,
                                related_name='translations')
    name = models.CharField (verbose_name=_('name'),
                             max_length=100)
    description = models.CharField (verbose_name=_('description'),
                                    null=True,
                                    max_length=255)

    class Meta:
        unique_together = ('parent', 'language_code')


#
# The Size_group model represents a group of sizes (e.g. XS,S,
# M,... or 36,38,40,...). It is used to narrow the possible sizes
# of a given item.
#
class Size_group (models.Model):
    name = models.CharField (verbose_name=_('name'),
                             max_length=255)

    class Meta:
        verbose_name = _('size group')
        verbose_name_plural = _('size groups')

    def __unicode__ (self):
        return self.name


#
# The Size model represents an element within a size group (e.g. XS
# or S or 36 or 40). It is always related to an item.
#
class Size (models.Model):
    name = models.CharField (verbose_name=_('name'),
                             max_length=20)
    sort = models.IntegerField (verbose_name=_('order'))
    size_group = models.ForeignKey (Size_group,
                                    verbose_name=_('size group'))

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')

    def __unicode__ (self):
        return self.name


#
# The Tax model represents a tax that is applied when selling an item.
#
class Tax (models.Model):
    name = models.CharField (verbose_name=_('name'),
                             max_length=100)
    percent = models.DecimalField (max_digits=4,
                                   decimal_places=2,
                                   verbose_name=_('percent'))
    locale = models.CharField (verbose_name=_('country code'),
                               max_length=30)

    class Meta:
        verbose_name = _('tax')
        verbose_name_plural = _('taxes')

    def __unicode__ (self):
        return self.name


class Item (MultilingualModel):
    """
    The Item model represents an article that may be sold
    and kept in warehouses. An item must always belong to
    a category.
    """
    active = models.BooleanField (verbose_name=_('active'))
    barcode = models.CharField (verbose_name=_('barcode'),
                                unique=True, 
                                max_length=100)
    category = models.ForeignKey (Category,
                                  verbose_name=_('category'))
    size_group = models.ForeignKey (Size_group,
                                    verbose_name=_('size group'))
    size = models.ForeignKey (Size,
                              verbose_name=_('size'))
    tax = models.ForeignKey (Tax,
                             verbose_name=_('tax'))

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')

    def __unicode__ (self):
        return "%s - %s" % (self.unicode_wrapper ('name'),
                            self.size)

    @staticmethod
    def get_unique_tuples ( ):
        """
        Returns a list of unique item tuples containing only some fields.
        """
        #
        # Find out the currently active language to select the correct fields
        #
        lang = settings.LANGUAGE_CODE.split ('_')
        lang = lang[0]

        name = 'name_' + lang
        sale_price = 'sale_price_' + lang

        some_items = Item.objects.values ('category', name, 'size_group', sale_price). \
                                          annotate (id=Min('id'))
        ids = list ([i['id'] for i in some_items])
        
        return Item.objects.filter (id__in=ids)


class ItemTranslation (MultilingualTranslation):
    """
    This class provides support for saving some fields
    of the Item model in different languages.
    """
    parent = models.ForeignKey ('Item',
                                related_name='translations')
    name = models.CharField (verbose_name=_('name'),
                             max_length=100)
    description = models.CharField (verbose_name=_('description'),
                                    null=True, 
                                    max_length=255)
    cost_price = CurrencyField (verbose_name=_('cost price'),
                                       max_digits=7,
                                       decimal_places=2)
    sale_price = CurrencyField (verbose_name=_('sale price'),
                                       max_digits=7,
                                       decimal_places=2)

    class Meta:
        unique_together = ('parent', 'language_code')

