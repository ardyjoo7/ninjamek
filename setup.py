#!/usr/bin/env python

from distutils.core import setup

setup(name='PlayNinjaLegends',
      version='0.0.3',
      description='Ninja Legends API',
      author='wobm',
      author_email='wobm@teknik.io',
      url='https://git.teknik.io/wobm/playninjalegends',
      packages=['playninjalegends'],
      install_requires=['Py3AMF', 'requests']
      )
