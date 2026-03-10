from collective.geolocationbehavior import _
from collective.geolocationbehavior.interfaces import IGeoJSONProperties
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.geolocation.field import GeolocationField
from plone.supermodel import model
from plone.uuid.interfaces import IUUID
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider

import pkg_resources

try:
    pkg_resources.get_distribution("plone.app.multilingual")
except pkg_resources.DistributionNotFound:
    HAS_PAM = False
else:
    from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
    from zope.interface import alsoProvides

    HAS_PAM = True


@provider(IFormFieldProvider)
class IGeolocatable(model.Schema):
    """Form field for geolocation behavior"""

    geolocation = GeolocationField(
        title=_("label_geolocation", default="Geolocation"),
        description=_(
            "help_geolocation",
            default="Click on the map to select a location, or "
            "use the text input to search by address.",
        ),
        required=False,
    )


if HAS_PAM:
    alsoProvides(IGeolocatable["geolocation"], ILanguageIndependentField)


@adapter(Interface)
@implementer(IGeoJSONProperties)
class GeoJSONProperties:

    def __init__(self, context):
        self.context = context

    @property
    def popup(self):
        return """
<header><a href="{}">{}</a></header>
<p>{}</p>""".format(
            self.context.absolute_url(),
            self.context.Title(),
            self.context.Description(),
        )

    @property
    def color(self):
        return "green"

    @property
    def extraClasses(self):
        return f"uuid-{IUUID(self.context)}"
