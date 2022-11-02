from setuptools import setup

setup(
    name='log-cli',
    version='0.2.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'log-cli = main:cli',
        ],
    },
)
