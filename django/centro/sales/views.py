import logging
import locale
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from centro.modules.models import Module
from centro.items.models import Item, Category, Size_group, Tax
from sales.models import Sale, SaleDetail
from utils.views import render
from utils import formats



def open_sale_list (request):
    """
    Generates a list of open sales.
    """
    column_data = []
    all_sales = Sale.objects.filter (completed='0').order_by('date_time')

    for sale in all_sales:
        row = [sale.date_time, sale.number, sale.customer]
        column_data.append ({'detail_url' : reverse('sales.views.sale_detail_list',
                                                     args=[sale.id]),
                             'fields' : row})

    return render ('object_list.html', 
                   {'selected_submodule': Module.get_submodule('Open sales'),
                    'columns': [_('time'), _('number'), _('customer')],
                    'column_data': column_data},
                   RequestContext (request))


def closed_sale_list (request):
    """
    Generates a list of closed sales.
    """
    column_data = []
    all_sales = Sale.objects.filter (completed='1').order_by('date_time')

    for sale in all_sales:
        row = [sale.date_time, sale.number, sale.customer]
        column_data.append ({'detail_url' : reverse('items.views.item_detail',
                                                    args=[sale.id]),
                             'fields' : row})

    return render ('object_list.html', 
                   {'selected_submodule': Module.get_submodule('Closed sales'),
                    'columns': [_('time'), _('number'), _('customer')],
                    'column_data': column_data},
                   RequestContext (request))


def sale_detail_list (request, sale_id):
    """
    Generates a detail entry list of the given 'sale_id'.
    """
    column_data = []
    sale_details = SaleDetail.objects.filter (sale__id=sale_id)

    for detail in sale_details:
        #
        # if item is not given, display the comment
        #
        if (detail.item):
            row = [detail.item]
        else:
            row = [detail.comment]
        row.append (formats.format_float(detail.quantity))
        row.append (formats.format_float(detail.sale_price))
        column_data.append ({'fields' : row})

    the_sale = Sale.objects.get (pk=sale_id)
   
    #
    # sale-related values
    #


    return render ('sales/sale_entry.html', 
                   {'display_title': _('invoice'),
                    'columns': [_('item'), _('quantity'), _('price')],
                    'column_data': column_data,
                    'customer': the_sale.customer,
                    'amount_paid': the_sale.get_amount_paid ( ),
                    'subtotal': the_sale.get_subtotal ( ),
                    'taxes': the_sale.get_taxes ( ),
                    'total': the_sale.get_total ( )},
                   RequestContext (request))




"""       
def category_list (request):
    ""
    Generates a list of categories.
    ""
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
    ""
    Generates a list of items.
    ""
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
    ""
    Generates a list of size groups.
    ""
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
    ""
    Generates a list of taxes.
    ""
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
    ""
    Displays the item(s) that match some fields
    of the one with the received id.
    ""
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
    ""
    Displays the sizes of the size group with the received id.
    ""
    return render_to_response ('object_list.html', 
                               {'columns': [],
                                'detail_view': size_group_id},
                               context_instance = RequestContext (request))
"""
