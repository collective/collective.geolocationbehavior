# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


version = '1.6.0'

setup(
    name='collective.geolocationbehavior',
    version=version,
    description="Dexterity behavior to add geographic locations to contents.",
    long_description="{0}\n{1}".format(
        open("README.rst").read(),
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Jesse Snyder, davisagli et al',
    url='https://github.com/collective/collective.geolocationbehavior/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # Dependencies for the behavior and form
        'plone.app.dexterity',  # remove this one to get a generic behavior
        'plone.autoform',
        'plone.behavior',
        'plone.dexterity',
        'plone.formwidget.geolocation',
        'plone.supermodel',
        # Framework dependencies
        'zope.annotation',
        'zope.component',
        'zope.interface',
    ],
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
