from zope.interface import Attribute
from zope.interface import Interface


class IGeoJSONProperties(Interface):
    """Adapter adapting an content object for determining geojson properties.
    """

    popup = Attribute("Return a string to display in the marker popup.")
    color = Attribute("Return the marker color.")
    extraClasses = Attribute("Return a string of extra css classes to be added to the marker icon.")  # noqa
