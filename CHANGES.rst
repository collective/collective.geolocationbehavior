Changelog
=========


.. towncrier release notes start

Breaking changes:

- Switch to a PEP 420 native namespace package (no ``collective/__init__.py``
  with ``pkg_resources`` namespace declaration any more). Mixing native and
  ``pkg_resources``-style packages in the ``collective`` namespace does not
  work; in environments that still contain old-style ``collective.*`` eggs
  (typically Plone 6.1 buildouts) use ``horse-with-no-namespace``.
  [erral, petschki]

- Require Plone 6.1 or 6.2 and Python 3.10 to 3.14, drop support for
  Plone 5.2 and 6.0.
  [erral, petschki]

New features:

- Add Spanish translation and new translation strings.
  [macagua]

- Complete the German translation.
  [petschki]

Internal:

- Add an integration test suite (install/uninstall, behavior registration,
  ``latitude``/``longitude`` indexes and metadata, GeoJSON properties adapter)
  and a ``test`` extra, run on Plone 6.1 and 6.2 in CI.
  [petschki]

- Move to the ``src/`` layout and configure the repository with plone/meta
  (2.11.1): tox, GitHub workflows, pre-commit with pyupgrade, isort, black,
  zpretty, flake8, codespell, check-manifest, pyroma, i18ndude.
  [erral, petschki]

- Replace the deprecated ``pkg_resources`` probe for ``plone.app.multilingual``
  with ``importlib`` (setuptools 81+ warns about ``pkg_resources``).
  [petschki]

- Use the SPDX license expression ``GPL-2.0-or-later`` (matching the
  license grant in ``LICENSE.txt``) instead of the deprecated license
  classifier; ``LICENSE.txt`` moved to the package root next to
  ``LICENSE.GPL``.
  [petschki]

- Remove the obsolete ``buildout.cfg`` and ``docs/INSTALL.txt``; fix
  ``build-i18n.sh`` for the ``src/`` layout.
  [petschki]

- Fixed some errors from code-analysis scripts.
  [macagua]


1.7.2 (2021-09-16)
------------------

- Fix Italian .po file location
  [laulaz]

- Add French translation
  [laulaz]


1.7.1 (2020-07-10)
------------------

- Do not use autoinclude for ZCML, load explicit.
  [jensens]


1.7.0 (2019-12-09)
------------------

- Make geolocation language independent
  [agitator]


1.6.0 (2019-04-24)
------------------

- Add ``IGeoJSONProperties`` adapter.
  [petschki]

- Add latitude/longitude indexer.
  [petschki]

- Add uninstall profile.
  [petschki]

- Prepare testing environment.
  [petschki]


1.5.1 (2017-04-04)
------------------

- Explicitly include necessary zcml dependencies to avoid having to explicitly doing that in tests.
  plone.app.testing disables z3c.autoinclude.
  [thet]


1.5 (2016-10-06)
----------------

- Register the ``collective.geolocationbehavior.geolocation.IGeolocatable`` behavior under the name ``geolocatable``.
  Do not bind ``for`` because its superfluous.
  [thet, jensens]

- Code cleanup, remove BBB classes.
  [thet]


1.4 (2015-07-15)
----------------

- Install the plone.formwidget.geolocation default profile in order to get
  Leaflet map support.
  [thet]

- Fix upgrade step with broken persistent classes and re-create BBB class
  definitions for upgrading. Reindex the object while upgrading to get updated
  object_provides indexes.
  [thet]


1.3.2 (2015-03-04)
------------------

- Fix the import bug, introduced of previous commit.


1.3.1 (2015-03-04)
------------------

- Fix import of GeolocationField.


1.3 (2015-03-04)
----------------

- Remove browserlayer, which isn't needed any more. Includes an Upgrade step.
  [thet]

- Switch to Attribute storage instead of Annotation storage. This is easier to
  access and needs less ZODB unpickling. It's unlikely that two behaviors share
  the same geolocation schema name. A upgrade step is provided.
  [thet]

- Removed code related to Google Maps integration. The integration is better
  done with Mockup Javascript.
  [thet]

- PEP8.
  [thet]


1.2 (2014-04-30)
----------------

- Add italian translation
  [gborelli]

- Remove dependency on Products.Maps and copy some of it's interfaces to here.
  Note, Google Map integration is not available at this point.
  For mapping functionality I suggest to backport the Leaflet integration from
  collective.venue.
  [thet]

- Remove dependency on Grok and use Dexterity 2 way with plone.supermodel to
  define the schema.
  [thet]


1.1.0.2 (2012-09-21)
--------------------

- 1.1 was somehow broken again


1.1 (2012-09-21)
----------------

- Fix egg, add authors


1.0 (2012-09-21)
----------------

- Initial release
