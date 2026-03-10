from collective.geolocationbehavior.geolocation import IGeolocatable
from plone.browserlayer.utils import unregister_layer
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAnnotations
from zope.component.hooks import getSite
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent

import logging

log = logging.getLogger(__name__)


GEO_ANNOTATION_KEY = (
    "collective.geolocationbehavior.geolocation.GeolocatableAnnotation"  # noqa
)


def upgrade_attribute_storage(context):
    portal = getSite()
    catalog = getToolByName(portal, "portal_catalog")
    query = {}
    query["object_provides"] = (
        "collective.geolocationbehavior.geolocation.IGeolocatableMarker"  # noqa
    )
    results = catalog(**query)
    log.info(f"There are {len(results)} in total, stating migration...")
    for result in results:
        try:
            obj = result.getObject()
        except Exception:
            log.warning(
                "Not possible to fetch object from catalog result for "
                "item: {}.".format(result.getPath())
            )
            continue
        if not IAnnotatable.providedBy(obj):
            log.warning(
                "The object at {} does provide annotation capabilities, "
                "skipping.".format(obj.absolute_url())
            )
            continue
        annotations = IAnnotations(obj)
        oldvalue = annotations.get(GEO_ANNOTATION_KEY, None)
        geolocation = getattr(oldvalue, "geolocation", None)
        if geolocation and not IGeolocatable(obj).geolocation:
            # Only write the old value if there is no new value yet
            IGeolocatable(obj).geolocation = geolocation
            notify(ObjectModifiedEvent(obj))
            log.info(
                "Set geolocation lat: {}, lng: {} for {}".format(
                    geolocation.latitude, geolocation.longitude, obj.absolute_url()
                )
            )
        if oldvalue:
            del annotations[GEO_ANNOTATION_KEY]
        obj.reindexObject()  # reindex - old IGeolocatableMarker doesn't exist anymore  # noqa


def remove_browserlayer(context):
    try:
        unregister_layer(name="collective.geolocationbehavior")
    except KeyError:
        # No browser layer with name collective.geolocationbehavior registered
        pass
