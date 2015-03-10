from django import template
from modules.models import Module


register = template.Library ( )

@register.inclusion_tag ('modules/module_panel.html')
def module_panel ( ):
    """
    Compiles the custom tag {% module_panel %}.
    """
    all_top_modules = Module.objects.filter (parent__isnull = True).order_by ('sort')
    return {'all_top_modules' : all_top_modules}

