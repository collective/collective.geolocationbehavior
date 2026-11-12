"""Setup tests for this package."""

from collective.geolocationbehavior.geolocation import HAS_PAM
from collective.geolocationbehavior.geolocation import IGeolocatable
from collective.geolocationbehavior.testing import (  # noqa: E501
    COLLECTIVE_GEOLOCATIONBEHAVIOR_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from Products.CMFPlone.utils import get_installer
from zope.component import queryUtility

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.geolocationbehavior is properly installed."""

    layer = COLLECTIVE_GEOLOCATIONBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        self.assertTrue(
            self.installer.is_product_installed("collective.geolocationbehavior")
        )

    def test_dependency_installed(self):
        self.assertTrue(
            self.installer.is_product_installed("plone.formwidget.geolocation")
        )

    def test_behavior_registered(self):
        # registered under the short name and under the dotted interface name
        for name in (
            "geolocatable",
            "collective.geolocationbehavior.geolocation.IGeolocatable",
        ):
            behavior = queryUtility(IBehavior, name=name)
            self.assertIsNotNone(behavior, name)
            self.assertIs(behavior.interface, IGeolocatable)
        self.assertEqual(behavior.name, "geolocatable")

    def test_catalog_indexes_and_metadata(self):
        catalog = self.portal.portal_catalog
        for name in ("latitude", "longitude"):
            self.assertIn(name, catalog.indexes())
            self.assertEqual(catalog.Indexes[name].meta_type, "FieldIndex")
            self.assertIn(name, catalog.schema())

    def test_field_is_language_independent(self):
        if not HAS_PAM:
            self.skipTest("plone.app.multilingual is not available")
        from plone.app.multilingual.dx.interfaces import ILanguageIndependentField

        self.assertTrue(
            ILanguageIndependentField.providedBy(IGeolocatable["geolocation"])
        )


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_GEOLOCATIONBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.geolocationbehavior")

    def test_product_uninstalled(self):
        self.assertFalse(
            self.installer.is_product_installed("collective.geolocationbehavior")
        )
