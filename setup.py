# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


version = '1.7.1'

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
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
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
