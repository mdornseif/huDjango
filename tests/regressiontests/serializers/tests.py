#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by Maximillian Dornseif on 2009-08-17.
Copyright (c) 2009 HUDORA. All rights reserved.
"""

from django.test import TestCase
from regressiontests.serializers.models import Place
from hudjango.serializers import queryset_to_xls

class SerializerTests(TestCase):
    def test_serializer_list(self):
        place1 = Place.objects.create(name="Dempsey's", address="623 Vermont St")
        place2 = Place.objects.create(name="Eich", address=u"An dür Eich 1")
        xlsdata = queryset_to_xls([place1, place2])
        self.assertEqual(xlsdata[:4], '\xd0\xcf\x11\xe0')
