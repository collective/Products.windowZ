#!/bin/sh

# see https://community.plone.org/t/not-using-bootstrap-py-as-default/620
ln -fs plone-5.1.x.cfg buildout.cfg
./bootstrap-base.sh
