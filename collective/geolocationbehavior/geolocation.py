from persistent import Persistent
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.formwidget.geolocation import GeolocationField
from plone.supermodel import model
from zope.annotation import factory
from zope.component import adapts
from zope.interface import alsoProvides, implements, Interface

from collective.geolocationbehavior import _


class IGeolocatable(model.Schema):
    """Form field for geolocation behavior"""
    geolocation = GeolocationField(
        title=_('label_geolocation', default=u'Geolocation'),
        description=_('help_geolocation',
                      default=u'Click on the map to select a location, or '
                              u'use the text input to search by address.'),
        required=False)
alsoProvides(IGeolocatable, IFormFieldProvider)


class IGeolocatableMarker(Interface):
    """Marker for geolocatable content"""
    pass


class GeolocatableAnnotation(Persistent):
    """Geolocation storage in annotation"""
    implements(IGeolocatable)
    adapts(IDexterityContent)

    def __init__(self):
        self.geolocation = None
Geolocatable = factory(GeolocatableAnnotation)
