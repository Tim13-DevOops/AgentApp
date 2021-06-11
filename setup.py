from setuptools import setup, find_packages

setup(
    name='simple-flask-app',
    version='0.1.0',
    description='Setting up a python package',
    author='Rogier van der Geer',
    author_email='rogiervandergeer@godatadriven.com',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['start_server=app.app:main']
    },
)