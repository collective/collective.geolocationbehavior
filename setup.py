from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.geolocationbehavior',
      version=version,
      description="A behavriior which makes it possible to mark and item with a geographic location.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Jesse Snyder',
      author_email='jesses@npowerseattle.org',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'collective.autopermission',
          'plone.app.textfield',
          'plone.formwidget.geolocation',
          'Products.Maps',        
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
