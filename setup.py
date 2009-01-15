# -*- coding: utf-8 -*-
# $Id$
import os
from setuptools import setup, find_packages

def _textOfModuleFile(filename):
    return open(filename, 'r').read().strip()

version = _textOfModuleFile(os.path.join('Products', 'windowZ', 'version.txt'))
long_description = _textOfModuleFile(os.path.join('Products', 'windowZ', 'README.txt'))

setup(name='Products.windowZ',
      version=version,
      description=("windowZ provides a new content type, named Window, "
                   "that is similar to the content type Link, but it shows "
                   "the provided relative or absolute URL inside an iFrame "
                   "rendered as a Plone page."),
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 5 - Production/Stable",
        ],
      keywords='plone layout composition themeing',
      author='Jean Rodrigo Ferri',
      author_email='jeanrodrigoferri@yahoo.com.br',
      url='http://www.plone.org/products/windowz',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
