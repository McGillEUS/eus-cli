from setuptools import setup, find_packages

setup(
    name="eus",
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'paramiko',
        'scp'
    ],
    entry_points='''
        [console_scripts]
        eus=eus.cli:cli
    ''',
)
