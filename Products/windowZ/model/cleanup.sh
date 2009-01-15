#!/bin/sh
# General cleanup of product windowZ

echo "==>> Cleaning product..."
find ./windowZ/ -name "*.pyc" -exec rm {} \;
find ./windowZ/ -name "*.pyo" -exec rm {} \;
find ./windowZ/ -name "*~" -exec rm {} \;
find ./windowZ/ -name "*.zuml.bak.*" -exec rm {} \;
rm -f windowZ/skins/windowZ/readme.txt
cp windowZ/skins/windowZ/window_icon.gif windowZ/tool.gif
