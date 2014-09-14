from distutils.core import setup

setup(name='ejnug',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Share emails publically',
      url='https://github.com/tlevine/ejnug',
      tests_require = ['nose'],
      scripts = ['ejnug.py'],
      version='0.0.1',
      license='AGPL',
)
