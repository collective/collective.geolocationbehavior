# -*- coding: utf-8 -*-
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


@provider(IFormFieldProvider)
class IGeolocatable(model.Schema):
    """Form field for geolocation behavior"""
    geolocation = GeolocationField(
        title=_('label_geolocation', default=u'Geolocation'),
        description=_('help_geolocation',
                      default=u'Click on the map to select a location, or '
                              u'use the text input to search by address.'),
        required=False)


@adapter(Interface)
@implementer(IGeoJSONProperties)
class GeoJSONProperties(object):

    def __init__(self, context):
        self.context = context

    @property
    def popup(self):
        return u"""
<header><a href="{0}">{1}</a></header>
<p>{2}</p>""".format(
            self.context.absolute_url(),
            self.context.Title(),
            self.context.Description(),
        )

    @property
    def color(self):
        return 'green'

    @property
    def extraClasses(self):
        return 'uuid-{0}'.format(IUUID(self.context))
