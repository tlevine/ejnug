from distutils.core import setup

setup(name='ejnug',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Share emails publically',
      url='https://github.com/tlevine/ejnug',
      install_requires=[
          'lxml>=3.3.5',
          'bottle>=0.12.7',
          'notmuch>=0.15.2',
          'Unidecode>=0.04.16',
      ]
      tests_require = ['nose'],
      scripts = ['ejnug.py'],
      version='0.0.1',
      license='AGPL',
)
