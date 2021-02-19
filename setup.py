from setuptools import setup
import os

def readme():
    with open('README.md') as file:
        return file.read()

setup(name='arrangepy',
      version='1.1.2',
      description='Arrange your files in distinct folder, help you clean your PC',
      long_description=readme(),
      long_description_content_type = 'text/markdown',
      keywords='arrange files windows cleaning tool open source prashant sengar',
      url='https://github.com/prashantsengar/ArrangePy',
      author='Prashant Sengar',
    #   author_email='contact--AT--prashants.in',
      license='MIT',
      packages=['arrangepy'],
##      scripts=['bin/arrange'],
      install_requires=[
          'flask',
      ],
      entry_points={
          'console_scripts': ['arrange=arrangepy.main:main'],
      },
      include_package_data=True,
      zip_safe=False)
