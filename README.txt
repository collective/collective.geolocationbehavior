Introduction
============

Dexterity based behaviors for geotagging.


TODO
----

- Remove dependency on Products.Maps. Eventually create a generic plone.geo
  package with required interfaces.

- Remove dependency on plone.app.dexterity. It's just needed for installing
  p.a.dexterity in this case. Thats better done in integration products and not
  the behavior extension itself. Removing this dep gives us a more generic
  behavior.
