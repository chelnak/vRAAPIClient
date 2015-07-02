import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='vRAAPIClient',
      version='0,1',
      description='vRealize Automation API Client',
      author='chelnak',
      author_email='',
      install_requires=['requests', 'prettytable'],
      packages=['vraapiclient'],
      long_description=read('README.md'),
      classifiers=[
          "Environment :: No Input/Output (Daemon)",
          "Intended Audience :: Information Technology",
          "Intended Audience :: System Administrators",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Distributed Computing"
      ],
      zip_safe=True)
