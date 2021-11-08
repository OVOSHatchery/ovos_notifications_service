""" Install the ovos_notifications_service package
"""
from setuptools import setup

setup(
    name='ovos_notifications_service',
    version='0.0.1',
    url='https://github.com/OpenVoiceOS/ovos_notifications_service',
    keywords='OVOS Notifications Service',
    packages=['ovos_notifications_service'],
    install_requires=['mycroft-messagebus-client'],
    include_package_data=True,
    license='Apache',
    author='Aditya Mehra',
    author_email='aix.m@outlook.com',
    description='OVOS Notifications Service',
    entry_points={
        'console_scripts': [
            'ovos_notifications_service=ovos_notifications_service.__main__:main',
            ]
        }
)
