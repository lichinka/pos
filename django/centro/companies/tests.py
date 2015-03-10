"""
Test cases for the companies application.-
"""
from django.test import TestCase
from companies.models import Company, Store, Terminal


class CompanyTest (TestCase):
    """
    All tests regarding the Company model.
    """
    def test_company_existance (self):
        """
        At least one company should exist in the fixture.
        """
        all_companies = Company.objects.all ( )
        
        self.assertTrue (len(all_companies) > 0,
                         "No company exists within the fixture.")

class StoreTest (TestCase):
    """
    All tests regarding the Store model.
    """
    def test_store_existance_within_a_company (self):
        """
        At least one store should exist as part of a company.
        """
        all_stores = Store.objects.all ( )
       
        self.assertTrue (len(all_stores) > 0,
                         "No stores exist within the fixture.")
        self.assertFalse (all_stores[0].company is None,
                          "At least one store should exist within a company.")


class TerminalTest (TestCase):
    """
    All tests regarding the Terminal model.
    """
    def test_terminal_existance_within_a_store (self):
        """
        At least one terminal should exist as part of a store.
        """
        all_terminals = Terminal.objects.all ( )
       
        self.assertTrue (len(all_terminals) > 0,
                         "No terminals exist within the fixture.")
        self.assertFalse (all_terminals[0].store is None,
                          "At least one terminal should exist within a store.")

