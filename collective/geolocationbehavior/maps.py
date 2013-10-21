from zope.interface import implements
from zope.component import adapts

from collective.geolocationbehavior.interfaces import IMap
from collective.geolocationbehavior.interfaces import IMarker
from collective.geolocationbehavior.geolocation import IGeolocatableMarker
from collective.geolocationbehavior.geolocation import IGeolocatable


class GeolocatableMap(object):
    implements(IMap)
    adapts(IGeolocatableMarker)

    def __init__(self, context):
        self.context = context

    def getMarkers(self):
        return GeolocatableMarker(self)


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
