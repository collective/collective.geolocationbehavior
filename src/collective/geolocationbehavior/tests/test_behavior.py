"""Tests for the geolocatable behavior, its indexers and the GeoJSON adapter."""

from collective.geolocationbehavior.geolocation import IGeolocatable
from collective.geolocationbehavior.interfaces import IGeoJSONProperties
from collective.geolocationbehavior.testing import (  # noqa: E501
    COLLECTIVE_GEOLOCATIONBEHAVIOR_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.uuid.interfaces import IUUID
from zope.component import queryUtility

import unittest

ANYWHERE = {"query": [-180, 180], "range": "min:max"}


class TestBehavior(unittest.TestCase):

    layer = COLLECTIVE_GEOLOCATIONBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.catalog = self.portal.portal_catalog
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        fti = queryUtility(IDexterityFTI, name="Document")
        fti.behaviors = tuple(fti.behaviors) + ("geolocatable",)
        self.portal.invokeFactory(
            "Document",
            "located",
            title="Located document",
            description="A document with a geolocation.",
        )
        self.doc = self.portal["located"]

    def brain(self):
        return self.catalog(UID=IUUID(self.doc))[0]

    def test_behavior_adapts_content(self):
        adapted = IGeolocatable(self.doc, None)
        self.assertIsNotNone(adapted)
        self.assertIsNone(adapted.geolocation)

    def test_geolocation_is_indexed(self):
        IGeolocatable(self.doc).geolocation = Geolocation(47.4125, 9.7417)
        self.doc.reindexObject()
        brain = self.brain()
        self.assertEqual(brain.latitude, 47.4125)
        self.assertEqual(brain.longitude, 9.7417)
        self.assertEqual(len(self.catalog(latitude=47.4125, longitude=9.7417)), 1)

    def test_missing_geolocation_is_not_indexed(self):
        self.assertEqual(len(self.catalog(latitude=ANYWHERE)), 0)
        self.assertEqual(len(self.catalog(longitude=ANYWHERE)), 0)
        self.assertNotIsInstance(self.brain().latitude, float)

    def test_geojson_properties(self):
        props = IGeoJSONProperties(self.doc)
        self.assertEqual(props.color, "green")
        self.assertEqual(props.extraClasses, f"uuid-{IUUID(self.doc)}")
        self.assertIn(self.doc.absolute_url(), props.popup)
        self.assertIn("Located document", props.popup)
        self.assertIn("A document with a geolocation.", props.popup)
