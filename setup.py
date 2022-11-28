from setuptools import setup

setup(
    name='log-cli',
    version='0.2.2',
    py_modules=['log_cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'log-cli = log_cli:cli',
        ],
    },
)
