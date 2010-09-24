import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-wordpress",
    version = "0.1",
    packages = find_packages(),
    author = "Agiliq and friends",
    author_email ="shabda@agiliq.com", 
    description = "Django app to easily integrate Wordpress.",
    url = "http://github.com/agiliq/django-wordpress",
    include_package_data = True
)
