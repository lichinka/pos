from django import template
from modules.models import Module


register = template.Library ( )

@register.inclusion_tag ('modules/submodule_tabs.html')
def submodule_tabs (selected_submodule):
    """
    Generates tabs containing the submodules of the
    received parent module.
    """
    parent_module = selected_submodule.parent
    all_submodules = Module.objects.filter (parent = parent_module.pk).order_by ('sort')
    return {'selected_submodule' : selected_submodule,
            'all_submodules' : all_submodules}

