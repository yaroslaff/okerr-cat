from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='okerr-cat',
      version='0.0.1',
      description='Demo website (simulating failures) for Okerr project',
      url='https://github.com/yaroslaff/okerr-cat',
      author='Yaroslav Polyakov',
      author_email='yaroslaff@gmail.com',
      license='GPL',
      packages = ['okerrcat', 'okerrcat.templates'],
      #packages=[
      #    'okerrcat', 
      
      #    ],

      # scripts=['bin/locker-server.py'],
      # include_package_data=True,

      long_description = read('README.md'),
      long_description_content_type='text/markdown',

      install_requires=[
          'flask',
          'dnspython',
          'requests'],

        data_files = [
            ('contrib', [
                'contrib/okerr-cat.service',
                'contrib/okerr-cat.nginx',
                'contrib/okerr-cat.default']),
            ('.', [
                'wsgi.py',
                'okerr-cat.ini'
            ])
        ], 
        include_package_data = True,

      zip_safe=True
      )

