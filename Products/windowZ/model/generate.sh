#!/bin/sh
# Generate windowZ code

echo "==>> Generating code..."
python2.3 ArchGenXML/ArchGenXML.py -c windowZ/model/generate.conf windowZ/model/windowZ.zuml
./windowZ/model/cleanup.sh
