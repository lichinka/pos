from django.conf import settings
from django.test import TestCase, client



class SettingsTest (TestCase):
    """
    Checks that the settings used by the Accounts app have been defined.
    """
    def test_admin_url_exists (self):
        """
        Checks that the user defined the setting ADMIN_URL.
        """
        self.assertTrue (len (str (settings.ADMIN_URL)) > 0,
                         "The setting ADMIN_URL has not been defined.") 

    def test_login_redirect_url_exists (self):
        """
        Checks that the user defined the setting LOGIN_REDIRECT_URL.
        """
        self.assertTrue (len (str (settings.LOGIN_REDIRECT_URL)) > 0,
                         "The setting LOGIN_REDIRECT_URL has not been defined.")


class FileExistsTest (TestCase):
    """
    Checks that certain files exist and are accessible.
    """
    def test_default_avatar_exists (self):
        c = client.Client ( )
        res = c.get ('/images/login/style_green_x_medium.png')
        self.assertTrue ('error' not in res.content,
                         'Default avatar image does not exists')

