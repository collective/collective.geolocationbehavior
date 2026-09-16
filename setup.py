from setuptools import setup

version = "3.0.0.dev0"

setup(
    name="collective.geolocationbehavior",
    version=version,
    description="Dexterity behavior to add geographic locations to contents.",
    long_description="{}\n{}".format(
        open("README.rst").read(), open("CHANGES.rst").read()
    ),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords="plone dexterity behavior geographic locations contents",
    author="Jesse Snyder, davisagli et al",
    author_email="collective@plone.org",
    url="https://github.com/collective/collective.geolocationbehavior/",
    license="GPL-2.0-only",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        # Dependencies for the behavior and form
        "plone.app.dexterity",  # remove this one to get a generic behavior
        "plone.autoform",
        "plone.behavior",
        "plone.formwidget.geolocation",
        "plone.supermodel",
        # Framework dependencies
        "zope.annotation",
        "zope.component",
        "zope.interface",
        "Products.CMFCore",
        "Products.GenericSetup",
        "plone.browserlayer",
        "plone.indexer",
        "plone.uuid",
        "zope.i18nmessageid",
        "zope.lifecycleevent",
        "zope.event",
    ],
    extras_require={
        "test": [
            # plone.formwidget.geolocation < 4 imports plone.api without
            # declaring it, so the test layer would not load otherwise.
            "plone.api",
            "plone.app.contenttypes[test]",
            "plone.app.testing",
            "plone.dexterity",
            "Products.CMFPlone",
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
