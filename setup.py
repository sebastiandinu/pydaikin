#!/usr/bin/env python

from distutils.core import setup

setup(name='pydaikin',
      version='0.4',
      description='Python Daikin HVAC appliances interface',
      author='Yari Adan',
      author_email='mustang@yadan.org',
      license='GPL',
      url='https://github.com/andrei4002/pydaikin',
      packages=['pydaikin'],
      keywords=['homeautomation', 'daikin'],
      install_requires=['netifaces', 'requests'],
      scripts=['bin/pydaikin']
     )
