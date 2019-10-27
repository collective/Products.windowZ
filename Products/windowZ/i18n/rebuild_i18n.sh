#! /bin/sh

# Synchronise the templates and scripts with the .pot.
# All on one line normally:
i18ndude rebuild-pot --pot windowZ.pot \
   	--create windowZ \
    --merge generated.pot \
    --merge2 manual.pot ../

# Synchronise the resulting .pot with all .po files
# for po in locales/*/LC_MESSAGES/${I18NDOMAIN}.po; do
# 	i18ndude sync --pot locales/${I18NDOMAIN}.pot $po
# done
