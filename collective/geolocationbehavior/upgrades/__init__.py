# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from collective.geolocationbehavior.geolocation import IGeolocatable
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAnnotations
from zope.component.hooks import getSite
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
import logging
from plone.browserlayer.utils import unregister_layer

log = logging.getLogger(__name__)


BEHAVIOR_LIST = [
    IGeolocatable
]


def upgrade_attribute_storage(context):
    portal = getSite()
    catalog = getToolByName(portal, 'portal_catalog')
    query = {}
    query['object_provides'] = 'collective.geolocationbehavior.geolocation.IGeolocatableMarker'  # noqa
    results = catalog(**query)
    log.info('There are {0} in total, stating migration...'.format(
        len(results)))
    for result in results:
        try:
            obj = result.getObject()
        except:
            log.warning(
                'Not possible to fetch object from catalog result for '
                'item: {0}.'.format(result.getPath()))
            continue
        if not IAnnotatable.providedBy(obj):
            log.warning(
                'The object at {0} does provide annotation capabilities, '
                'skipping.'.format(obj.absolute_url()))
            continue
        annotations = IAnnotations(obj)
        did_work = False
        for behavior in BEHAVIOR_LIST:
            for name in behavior.names():
                fullname = '{0}.{1}'.format(behavior.__identifier__, name)
                oldvalue = annotations.get(fullname, None)
                # Only write the old value if there is no new value yet
                if oldvalue and not getattr(obj, name, None):
                    setattr(obj, name, oldvalue)
                    did_work = True
        if did_work:
            notify(ObjectModifiedEvent(obj))
        log.debug('Handled object at {0}'.format(obj.absolute_url()))


def remove_browserlayer(context):
    try:
        unregister_layer(name=u"collective.geolocationbehavior")
    except KeyError:
        # No browser layer with name collective.geolocationbehavior registered
        pass
