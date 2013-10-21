from zope.interface import Interface
from zope.interface import Attribute
from zope.schema import Float


class IGeolocationBehaviorLayer(Interface):
    """Browser layer for sites with this behavior installed."""


class IMap(Interface):
    """ Interface for maps
    """

    def getMarkers():
        """Returns an iterable of markers."""


class IMarker(Interface):
    """Interface for a map marker
    """

    latitude = Float(
        title=u"Latitude",
        description=u"",
        required=False,
    )

    longitude = Float(
        title=u"Longitude",
        description=u"",
        required=False,
    )

    title = Attribute("Title of this marker")
    description = Attribute("Short description of this marker")
    layers = Attribute("A tuple of names of the layers this marker is in")
    icon = Attribute("Icon for this marker")
    url = Attribute("URL used on the title")
