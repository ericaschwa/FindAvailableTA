from distutils.core import setup

setup(name='findAvailableTA',
      version='1.0',
      description='Finds TA available at given day and time',
      author='Erica Schwartz',
      author_email='erica.schwartz.4@gmail.com',
      url='https://github.com/ericaschwa/FindAvailableTA',
      install_requires=[
      	'pytz',
		'lxml',
		'requests'
      ],
)