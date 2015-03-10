from django.test import TestCase
from modules.models import Module
from items.models import Item, Category, Size

"""
FIXME: Add a test to assure that the field 'locale' in the model Tax
       contains valid locale labels.
"""

class ItemTest (TestCase):
    """
    All tests of the Item model.
    """
    def _size_belongs_to_size_group (self, item):
        """
        The selected size in an item must belong to the
        selected size group in the same item.
        """
        self.assertTrue (item.size in Size.objects.filter (size_group = item.size_group),
                         "Size %s of item %s doesn't belong to size group %s." %
                            (str(item.size), str(item), str(item.size_group)))

    def test_all_items (self):
        """
        Run all tests on all existing items.
        """
        for item in Item.objects.all ( ):
            self._size_belongs_to_size_group (item)


class CategoryTest (TestCase):
    """
    All tests of the Category model.
    """
    def _category_cannot_have_itself_as_parent (self, category):
        """
        A category cannot have itself as parent category.
        Otherwise, cycles would occur in the category tree.
        """
        self.assertFalse (category == category.parent,
                          "Category %s cannot have itself as parent category." %
                          (str(category)))

    def test_all_categories (self):
        """
        Run all tests on all existing categories.
        """
        for cat in Category.objects.all ( ):
            self._category_cannot_have_itself_as_parent (cat)


class SubmoduleExistanceTest (TestCase):
    """
    These tests are needed to ensure the correct creation of the
    tabbed view in which the submodules are displayed.
    """
    def _submodule_existance (self, module_path):
        """
        The module with path 'module_path' should be
        a submodule (i.e. it should have a parent).
        """
        modules = Module.objects.filter (path=module_path). \
                                 filter (parent__isnull=False)
        self.assertTrue (len(modules) > 0,
                         "Module with path %s does not exist in fixture." %
                         module_path)

        parent_module = modules[0].parent
        self.assertFalse (parent_module is None,
                          "Module with path %s is not a submodule." %
                          module_path)

    def test_items_submodule_existance (self):
        self._submodule_existance ('/items')

    def test_categories_submodule_existance (self):
        self._submodule_existance ('/items/categories')

    def test_sizes_submodule_existance (self):
        self._submodule_existance ('/items/sizes')

