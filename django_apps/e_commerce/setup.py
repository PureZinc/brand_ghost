from setuptools import setup, find_packages

setup(
    name='e_commerce',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
        'Stripe',
    ],
)
