from setuptools import find_packages
from setuptools import setup

version = "2.0.0.dev0"

setup(
    name="collective.geolocationbehavior",
    version=version,
    description="Dexterity behavior to add geographic locations to contents.",
    long_description="{}\n{}".format(
        open("README.rst").read(), open("CHANGES.rst").read()
    ),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="plone dexterity behavior geographic locations contents",
    author="Jesse Snyder, davisagli et al",
    url="https://github.com/collective/collective.geolocationbehavior/",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["collective"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # Dependencies for the behavior and form
        "plone.app.dexterity",  # remove this one to get a generic behavior
        "plone.autoform",
        "plone.behavior",
        "plone.dexterity",
        "plone.formwidget.geolocation",
        "plone.supermodel",
        # Framework dependencies
        "zope.annotation",
        "zope.component",
        "zope.interface",
    ],
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
