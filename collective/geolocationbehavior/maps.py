from zope.interface import implements
from zope.component import adapts

from Products.CMFCore.interfaces import IFolderish
from Products.Maps.interfaces import IMarker
from Products.Maps.adapters import BaseMap

from collective.geolocationbehavior.geolocation import IGeolocatableMarker
from collective.geolocationbehavior.geolocation import IGeolocatable


class GeolocatableMap(BaseMap):
    adapts(IGeolocatableMarker)
    
    def getMarkers(self):
        return GeolocatableMarker(self)

class ContainerMap(BaseMap):
    adapts(IFolderish)
    
    def __init__(self, context):
        self.context = context
    
    def getMarkers(self):
        # return GeolocatableMarker(self)
        return None

class GeolocatableMarker(object):
    implements(IMarker)
    adapts(IGeolocatableMarker)

    def __init__(self, context):
        self.context = context

    @property
    def latitude(self):
        return IGeolocatable(self.context).geolocation.latitude

    @property
    def longitude(self):
        return IGeolocatable(self.context).geolocation.longitude

    @property
    def title(self):
        return self.context.Title()

    @property
    def description(self):
        return self.context.Description()

    @property
    def layers(self):
        return ()

    @property
    def icon(self):
        return "Red Marker"

    @property
    def url(self):
        return self.context.absolute_url()
