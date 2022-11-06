from setuptools import setup

setup(
    name='log-cli',
    version='0.2.2',
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
