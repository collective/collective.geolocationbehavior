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


Screenshots
===========

After installation, you will find a new behavior available, go to ``Site Setup`` > ``Content Types`` there select a content type and
click on the ``Behaviors`` tab, there you can see the new behavior called ``geolocatable`` as the following screenshot:

.. figure:: https://raw.githubusercontent.com/collective/collective.geolocationbehavior/refs/heads/master/docs/images/geolocatable.png
   :align: center
   :height: 77px
   :width: 876px
   :alt: The geolocatable Behavior

   The geolocatable Behavior.


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


Contribute
==========

- Issue Tracker: https://github.com/collective/collective.geolocationbehavior/issues
- Source Code: https://github.com/collective/collective.geolocationbehavior


Support
=======

If you are having issues, please let us know at our `issue tracker <https://github.com/collective/collective.geolocationbehavior/issues>`_.


License
=======

The project is licensed under the `GPLv2 <https://raw.githubusercontent.com/collective/collective.geolocationbehavior/refs/heads/master/LICENSE.GPL>`_.
