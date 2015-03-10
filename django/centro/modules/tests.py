from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from modules.models import Module


"""
TODO: Chack that all modules 'path' fields exist and are accesible.
"""

class LanguageCodesTest (TestCase):
    """
    These tests ensure that the language codes used across the 
    application and database are consistent.
    """
    def test_language_settings_match_language_codes (self):
        lang_code = settings.LANGUAGE_CODE.split('_')
        lang_code = lang_code[0]
        languages = [lcode for (lcode, lname) in settings.LANGUAGES]

        print lang_code, languages

        self.assertTrue (lang_code in languages,
                         "Language '" + lang_code + "' is not any of settings.LANGUAGES")


class ModulePathsTest (TestCase):
    def module_paths_exist_and_are_accesible (self):
        """
        Checks that all module paths exist and are accessible.
        """
        cli = Client ( )
        all_modules = Module.objects.all ( )

        for module in all_modules:
            response = cli.get (module.path)
            self.assertTrue (response.status_code == 200,
                             "Path '" + module.path + "' of module '" + module.name + "' is not accessible.")
 
