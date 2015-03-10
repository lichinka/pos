import logging
import locale
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Min
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from centro.modules.models import Module
from centro.items.models import Item, Category, Size_group, Tax



def _submodule (name):
    """
    Searches and returns the Module object of the received submodule name.
    """
    submodules = Module.objects.filter(name_en=name).\
                                filter(parent__isnull=False)
    if (len(submodules) > 0):
        return submodules[0]
    else:
        return _("unknown")


        
def category_list (request):
    """
    Generates a list of categories.
    """
    root_categories = Category.objects.filter (parent__isnull=True).order_by ('name')

    column_data = []

    #
    # Generate a tree-like view for subcategories
    #
    for root_cat in root_categories:
        row = [root_cat.name, root_cat.description]
        column_data.append ({'fields': row})

        sub_categories = Category.objects.filter (parent=root_cat).order_by ('name')

        for cat in sub_categories:
            row = ['=> ' + cat.name, cat.description]
            column_data.append ({'fields': row})

    return render_to_response ('object_list.html', 
                               {'selected_submodule': _submodule('Categories'),
                                'columns': [_('name'), _('description')],
                                'column_data': column_data},
                               context_instance = RequestContext (request))



def item_list (request):
    """
    Generates a list of items.
    """
    #
    # Choose only unique item tuples to shorten the list
    #
    some_items = Item.get_unique_tuples ( )
    column_data = []
    
    for item in some_items:
        row = [item.category.name, item.name,
               item.size_group.name, locale.currency (item.sale_price,
                                                      grouping=True)]
        column_data.append ({'detail_url' : reverse('items.views.item_detail',
                                                    args=[item_id]),
                             'fields' : row})

    return render_to_response ('object_list.html', 
                               {'selected_submodule': _submodule('Items'),
                                'columns': [_('category'), _('name'),
                                            _('size group'), _('sale price')],
                                'column_data': column_data},
                               context_instance = RequestContext (request))



def size_group_list (request):
    """
    Generates a list of size groups.
    """
    all_groups = Size_group.objects.all ( ).order_by ('name')

    column_data = []

    for group in all_groups:
        row = [group.name]
        column_data.append ({'detail_url' : reverse('items.views.size_group_detail',
                                                    args=[group.id]),
                             'fields' : row})

    return render_to_response ('object_list.html', 
                               {'selected_submodule': _submodule('Sizes'),
                                'columns': [_('size group')],
                                'column_data': column_data},
                               context_instance = RequestContext (request))

   
def tax_list (request):
    """
    Generates a list of taxes.
    """
    all_taxes = Tax.objects.filter (locale=settings.LANGUAGE_CODE).order_by ('name')

    column_data = []

    for tax in all_taxes:
        row = [tax.name]
        column_data.append ({'fields':row})

    return render_to_response ('object_list.html', 
                               {'selected_submodule': _submodule('Taxes'),
                                'columns': [_('tax')],
                                'column_data': column_data},
                               context_instance = RequestContext (request))


def item_detail (request, item_id):
    """
    Displays the item(s) that match some fields
    of the one with the received id.
    """
    item = Item.objects.get(id=item_id)

    logging.debug ("Category is " + str(item.category))
    logging.debug ("Name is " + str(item.name))

    some_items = Item.objects.filter (category__in=[item.category])
    logging.debug ("Cardinality is " + str(len(some_items)))

    some_items = some_items.filter (name=item.name)
    logging.debug ("Cardinality is " + str(len(some_items)))

    #                          filter (size_group__in=[item.size_group]). \
    #                          filter (sale_price__in=[item.sale_price])
    #
    # Item field data is grouped and display accordingly
    #
    general_data = []
    size_data = []
    tax_data = []

    for item in some_items:
        general_data.append ([{'field' : _('name'),
                              'data' : item.name},
                             {'field' : _('description'),
                              'data' : item.description},
                             {'field' : _('category'),
                              'data' : item.category},
                             {'field' : _('sale price'),
                              'data' : item.sale_price}])
        size_data.append ([{'field' : _('size'),
                           'data' : item.size},
                          {'field' : _('barcode'),
                           'data' : item.barcode}])
        tax_data.append ([{'field' : _('tax'),
                          'data' : item.tax}])

    data_groups = [{'name': _('general data'),
                    'data': general_data},
                   {'name': _('sizes'),
                    'data': size_data},
                   {'name': _('tax'),
                    'data': tax_data}]
    
    return render_to_response ('items/item_detail.html', 
                               {'selected_submodule': _submodule('Items'),
                                'data_groups': data_groups},
                               context_instance = RequestContext (request))



def size_group_detail (request, size_group_id):
    """
    Displays the sizes of the size group with the received id.
    """
    return render_to_response ('object_list.html', 
                               {'columns': [],
                                'detail_view': size_group_id},
                               context_instance = RequestContext (request))

