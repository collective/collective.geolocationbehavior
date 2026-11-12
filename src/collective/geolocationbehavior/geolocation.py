from collective.geolocationbehavior import _
from collective.geolocationbehavior.interfaces import IGeoJSONProperties
from importlib.util import find_spec
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.geolocation.field import GeolocationField
from plone.supermodel import model
from plone.uuid.interfaces import IUUID
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider

# plone.app.multilingual is optional: mark the field language independent
# when it is available (pkg_resources is deprecated, so probe the import).
HAS_PAM = find_spec("plone.app.multilingual") is not None
if HAS_PAM:
    from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
    from zope.interface import alsoProvides


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
