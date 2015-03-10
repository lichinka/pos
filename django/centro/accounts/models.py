from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from companies.models import Terminal


class UserProfile (models.Model):
    """
    This model keeps extra data about the users of the system.
    It is accessible through 'user.userprofile'.
    """
    user = models.OneToOneField (User,
                                 verbose_name=_('user'))
    #
    # The terminals on which the user may login
    #
    terminals = models.ManyToManyField (Terminal,
                                        null=True,
                                        blank=True,
                                        verbose_name=_('terminals'))
    #
    # An icon to display in the login page
    #
    avatar = models.CharField (max_length=100,
                               null=True,
                               blank=True,
                               default='/images/login/style_green_x_medium.png',
                               verbose_name=_('avatar'))
   
    class Meta:
        verbose_name = _("user's profile")
        verbose_name_plural = _("users' profiles")

    def __unicode__ (self):
        return self.user.username

