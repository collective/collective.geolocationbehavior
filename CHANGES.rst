Changelog
=========


1.5 (2016-10-06)
----------------

- Register the ``collective.geolocationbehavior.geolocation.IGeolocatable`` behavior under the name ``geolocatable``.
  Do not bind ``for`` because its superfluos.
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
