import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='vRAAPIClient',
      version='1.0',
      description='vRealize Automation API Client',
      author='chelnak',
      author_email='',
      install_requires=['requests', 'prettytable'],
      packages=['vraapiclient'],
      long_description=read('README.md'),
      keywords=['VMWare', 'vRealize Automation', 'vRA']
      classifiers=[
          'Environment :: No Input/Output (Daemon)'',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 2.7',
      ],
      zip_safe=True)
