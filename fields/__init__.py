"""Extended fieldtypes for use with django.

audit             - store inforation about current user and IP
defaulting        - set default values
scalingimagefield - ImageField variant  wich scales images on the fly.
"""

from audit import *
from defaulting import *
from scalingimagefield import *

from django.db.models import ManyToManyField

class RelaxedManyToManyField(ManyToManyField):
    """"This is a many to many field which can handle non integer primary keys for the relation."""
    def isValidIDList(self, field_data, all_data):
        "Validates that the value is a valid list of foreign keys"
        mod = self.rel.to
        pks = field_data.split(',')
        objects = mod._default_manager.in_bulk(pks)
        if len(objects) != len(pks):
            badkeys = [k for k in pks if k not in objects]
            raise validators.ValidationError, "Please enter valid %(self)s IDs." % {'self': self.verbose_name}
            #raise validators.ValidationError, "Please enter valid %(self)s IDs.  The value %(value)r is invalid. Please enter valid %(self)s IDs. The values %(value)r are invalid.", len(badkeys)) % {
            #    'self': self.verbose_name,
            #    'value': len(badkeys) == 1 and badkeys[0] or tuple(badkeys),
            #}