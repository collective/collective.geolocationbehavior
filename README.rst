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

.. figure:: https://raw.githubusercontent.com/collective/collective.geolocationbehavior/refs/heads/master/docs/images/igeolocatable_behavior.png
   :align: center
   :height: 77px
   :width: 876px
   :alt: The 'IGeolocatable' Behavior

   The ``IGeolocatable`` Behavior.

----

.. figure:: https://raw.githubusercontent.com/collective/collective.geolocationbehavior/refs/heads/master/docs/images/igeolocatable_behavior_used.png
   :align: center
   :height: 320px
   :width: 800px
   :alt: Using the 'IGeolocatable' Behavior into a custom content type

   Using the ``IGeolocatable`` Behavior into a custom content type.


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

If you installed Plone with `Cookieplone`_, you can install ``collective.geolocationbehavior`` add-on
from a source control system such as GitHub.

Add a line with ``collective.geolocationbehavior`` in the ``backend/requirements.txt`` file.

::

    collective.geolocationbehavior

Next add the add-on to ``zcml_package_includes`` in the file ``backend/instance.yaml`` so
that its configuration will load.

::

    default_context:
        zcml_package_includes: project_title, collective.geolocationbehavior

Finally, add the package's source to the ``mx.ini`` file.

::

    [collective.geolocationbehavior]
    url = https://github.com/collective/collective.geolocationbehavior.git
    pushurl = git@github.com:collective/collective.geolocationbehavior.git
    branch = master

To actually download and install the new add-on, run the following command.

::

    make backend-build

Now restart the backend.

----

If you installed Plone with `buildout`_, you can install ``collective.geolocationbehavior`` add-on
by adding it to your ``buildout`` eggs list like so:

::

   [buildout]

    ...

    eggs =
        collective.geolocationbehavior


and then running ``bin/buildout``

Now restart the instance.


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

.. _Cookieplone: https://github.com/plone/cookieplone
.. _buildout: https://6.docs.plone.org/admin-guide/add-ons.html#buildout
