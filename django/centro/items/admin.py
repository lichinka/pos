from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from multilingual_model.admin import TranslationInline
from items.models import Category, Size_group, Size, Tax, Item
from items.models import CategoryTranslation, ItemTranslation


class CategoryTranslationInline (TranslationInline):
    """
    Displays Category translations as inlined forms.
    """
    model = CategoryTranslation


class CategoryForm (forms.ModelForm):
    """
    Overrides the Form definition for the Category model
    to run custom validation rules.
    """
    class Meta:
        model = Category

    def clean_parent (self):
        """
        Checks that a category does not have itself as parent.
        """
        parent_cat = self.cleaned_data['parent']
        this_cat = self.instance
        if (parent_cat is not None) and (parent_cat.id == this_cat.id):
            raise forms.ValidationError (_("Category cannot be parent of itself"))
        return parent_cat


class CategoryAdmin (admin.ModelAdmin):
    form = CategoryForm
    list_display = ['as_tree_node']
    ordering = ['parent__id']
    inlines = [CategoryTranslationInline]


class ItemTranslationInline (TranslationInline):
    """
    Displays Item translations as inlined forms.
    """
    model = ItemTranslation


class ItemForm (forms.ModelForm):
    """
    Overrides the Form definition for the Item model
    to displayed custom fields and run custom validation rules.
    """
    size = forms.ModelChoiceField (queryset=Size.objects.all( ).order_by('size_group').order_by('sort'),
                                   empty_label=None)

    class Meta:
        model = Item

    def clean_size (self):
        """
        Checks that the selected size belongs to the selected size group.
        """
        sgroup = self.cleaned_data['size_group']
        size = self.cleaned_data['size']

        if (size not in Size.objects.filter (size_group__id=sgroup.id)):
            raise forms.ValidationError (_("Selected size does not belong to selected size group"))
        return size


class ItemAdmin (admin.ModelAdmin):
    form = ItemForm
    list_display = ['__unicode__', 'barcode', 'active']
    inlines = [ItemTranslationInline]
    ordering = ['-active']


class SizeAdmin (admin.StackedInline):
    """
    Defines a form for the sizes to be displayed with their size group.
    """
    model = Size
    extra = 1


class SizeGroupAdmin (admin.ModelAdmin):
    """
    Defines a form to display the size group together with its sizes.
    """
    inlines=[SizeAdmin]


admin.site.register (Category, CategoryAdmin)
admin.site.register (Size_group, SizeGroupAdmin)
admin.site.register (Tax)
admin.site.register (Item, ItemAdmin)
