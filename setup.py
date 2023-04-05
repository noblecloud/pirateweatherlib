import os
from setuptools import setup

# use pandoc to convert
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')) as f:
    README = f.read()

setup(name='pirateweatherlib',
      version='0.4.0',
      description='A Pirate Weather API wrapper',
      long_description=README,
      url='https://github.com/noblecloud/pirateweatherlib',
      author='Lukas Kubis and adapted for Pirate Weather by noblecloud',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
          'Topic :: Home Automation',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Operating System :: OS Independent',
      ],
      keywords='pirateweather pirate-weather pirate forecast home weather home-weather weather-station',
      packages=['pirateweather'],
      install_requires=[
          'future',
          'requests',
      ],
      test_suite='test',
      zip_safe=True
      )
