from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.geolocationbehavior


class CollectiveGeolocationbehaviorLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.geolocationbehavior)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.geolocationbehavior:default")


COLLECTIVE_GEOLOCATIONBEHAVIOR_FIXTURE = CollectiveGeolocationbehaviorLayer()


COLLECTIVE_GEOLOCATIONBEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEOLOCATIONBEHAVIOR_FIXTURE,),
    name="CollectiveGeolocationbehaviorLayer:IntegrationTesting",
)


COLLECTIVE_GEOLOCATIONBEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GEOLOCATIONBEHAVIOR_FIXTURE,),
    name="CollectiveGeolocationbehaviorLayer:FunctionalTesting",
)
