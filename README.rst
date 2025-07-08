==============================
collective.geolocationbehavior
==============================

This package provides a Dexterity based behaviors for
`Geotagging <https://en.wikipedia.org/wiki/Geotagging>`_.


Features
========

- Implements the `plone.formwidget.geolocation <https://github.com/collective/plone.formwidget.geolocation>`_ add-on which adds `LeafletJS <https://leafletjs.com/>`_ support.
- Adds catalog indexes/metadata for latitude/longitude to support GeoJSON feature list output/filtering.
- The GeoJSON properties can be customized with the provided ``IGeoJSONProperties`` adapter.


Examples
========

This add-on can be seen in action at the following add-ons:

- https://github.com/collective/collective.collectionfilter
- https://github.com/collective/collective.contentsections
- https://github.com/collective/collective.venue


Translations
============

This product has been translated into:

- German
- France
- Italian
- Spanish


Installation
============

Install ``collective.geolocationbehavior`` by adding it to your buildout:

::

   [buildout]

    ...

    eggs =
        collective.geolocationbehavior


and then running "bin/buildout".

After installation, you will find a new item in your site control panel where to set various options.


Contribute
==========

- Issue Tracker: https://github.com/collective/collective.geolocationbehavior/issues
- Source Code: https://github.com/collective/collective.geolocationbehavior


Support
=======

If you are having issues, please let us know at our `Issue Tracker <https://github.com/collective/collective.geolocationbehavior/issues>`_.


License
=======

The project is licensed under the GPLv2.
