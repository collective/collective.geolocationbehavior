from persistent import Persistent
from zope.annotation import factory
from zope.interface import alsoProvides, implements
from zope.component import adapts

from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.geolocation import GeolocationField

from Products.Maps.interfaces import IMapEnabled

from collective.geolocationbehavior import _


class IGeolocatable(form.Schema):
    """ Form field for geolocation behavior """
    geolocation = GeolocationField(title = _(u'Geolocation'),
                                   description = _(u'Click on the map to select a location, '
                                                   u'or use the text input to search by address.'),
                                   required=False)
alsoProvides(IGeolocatable, IFormFieldProvider)

class IGeolocatableMarker(IMapEnabled):
    """ Marker for geolocatable content """
    pass

class GeolocatableAnnotation(Persistent):
    """ Geolocation storage in annotation """
    implements(IGeolocatable)
    adapts(IDexterityContent)

    def __init__(self):
        self.geolocation = None
Geolocatable = factory(GeolocatableAnnotation)
