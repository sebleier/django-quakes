from setuptools import setup

setup(
    name="django-quakes",
    url="http://github.com/sebleier/django-quakes/",
    author="Sean Bleier",
    author_email="sebleier@gmail.com",
    version="0.0.1",
    packages=["quakes"],
    description="A simple app to download and display USGS earthquake data",
    install_requires=['django', 'redis>=2.4.5', 'django-celery', 'python-dateutil'],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
