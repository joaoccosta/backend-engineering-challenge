from setuptools import setup
setup(
    name = 'unbabel',
    version = '0.1.0',
    packages = ['unbabel'],
    entry_points = {
        'console_scripts': [
            'unbabel = unbabel.unbabel_cli:run'
        ]
    })