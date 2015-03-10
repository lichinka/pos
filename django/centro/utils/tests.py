from django.test import TestCase
from django.conf import settings



class SettingsTest (TestCase):
    """
    Checks that the settings used by the Utils app have been defined.
    """
    def test_application_name_exists (self):
        """
        Checks that the user defined the setting APPLICATION_NAME.
        """
        self.assertTrue (len (str (settings.APPLICATION_NAME)) > 0,
                         "The setting APPLICATION_NAME has not been defined.") 

    def test_application_version_exists (self):
        """
        Checks that the user defined the setting APPLICATION_VERSION.
        """
        self.assertTrue (len (str (settings.APPLICATION_VERSION)) > 0,
                         "The setting APPLICATION_VERSION has not been defined.")

    def test_this_terminal_id_exists (self):
        """
        Checks that the user defined the setting THIS_TERMINAL_ID.
        """
        self.assertTrue (int(settings.THIS_TERMINAL_ID) != 0,
                         "The setting THIS_TERMINAL_ID has not been defined.")

