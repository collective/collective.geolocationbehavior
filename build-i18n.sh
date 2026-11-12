#!/bin/sh
# Rebuild the translation catalogs. Needs i18ndude on the PATH, e.g.
#   pip install i18ndude   (or use the i18ndude of a Plone buildout: export PATH=$PATH:/path/to/buildout/bin)
set -e
cd "$(dirname "$0")"
I18NPATH=src/collective/geolocationbehavior
DOMAIN=collective.geolocationbehavior
i18ndude rebuild-pot --pot $I18NPATH/locales/$DOMAIN.pot --create $DOMAIN $I18NPATH
i18ndude sync --pot $I18NPATH/locales/$DOMAIN.pot $I18NPATH/locales/*/LC_MESSAGES/$DOMAIN.po
