from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class DeliciousAccount(models.Model):
    user = models.ForeignKey(User, related_name="delicious_account", verbose_name=_('user'))
    username = models.CharField(_('username'), max_length=30, unique=True)
    password = models.CharField(_('password'), max_length=128)

    def __unicode__(self):
        return self.username

# TODO: save password encrypted
#    def set_password(self, raw_password):
#        import random
#        algo = 'sha1'
#        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
#        hsh = get_hexdigest(algo, salt, raw_password)
#        self.password = '%s$%s$%s' % (algo, salt, hsh)

#    def check_password(self, raw_password):
#        """
#        Returns a boolean of whether the raw_password was correct. Handles
#        encryption formats behind the scenes.
#        """
#        # Backwards-compatibility check. Older passwords won't include the
#        # algorithm or salt.
#        if '$' not in self.password:
#            is_correct = (self.password == get_hexdigest('md5', '', raw_password))
#            if is_correct:
#                # Convert the password to the new, more secure format.
#                self.set_password(raw_password)
#                self.save()
#            return is_correct
#        return check_password(raw_password, self.password)

#    def set_unusable_password(self):
#        # Sets a value that will never be a valid hash
#        self.password = UNUSABLE_PASSWORD

#    def has_usable_password(self):
#        return self.password != UNUSABLE_PASSWORD
