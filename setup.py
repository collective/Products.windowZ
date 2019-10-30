# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '2.0.1'
long_description = (
    open('README.rst').read() + '\n' +
    open(os.path.join('docs', 'INSTALL.txt')).read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='Products.windowZ',
      version=version,
      description='Show web-pages inside an iframe. Plone content-type.',
      long_description=long_description,
      classifiers=[
          'Development Status :: 6 - Mature',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 5.0',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone layout composition themeing',
      author='Jean Rodrigo Ferri',
      author_email='jeanrodrigoferri@yahoo.com.br',
      url='http://plone.org/products/windowz',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.registry',
          'plone.z3cform',
          'Products.Archetypes',
          'Products.ATContentTypes',
          'Products.CMFCore',
          'Products.CMFPlone',
          'Products.GenericSetup',
          'setuptools',
          'stripogram',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      extras_require={
          'test': [
              'Products.PloneTestCase',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
