# -*- coding: utf-8 -*-
from collective.geolocationbehavior import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.geolocation.field import GeolocationField
from plone.supermodel import model
from zope.interface import provider


@provider(IFormFieldProvider)
class IGeolocatable(model.Schema):
    """Form field for geolocation behavior"""
    geolocation = GeolocationField(
        title=_('label_geolocation', default=u'Geolocation'),
        description=_('help_geolocation',
                      default=u'Click on the map to select a location, or '
                              u'use the text input to search by address.'),
        required=False)
