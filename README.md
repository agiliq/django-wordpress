[![Build Status](https://travis-ci.org/agiliq/django-wordpress.png?branch=master)](https://travis-ci.org/agiliq/django-wordpress)
[![Coverage Status](https://coveralls.io/repos/agiliq/django-wordpress/badge.png?branch=master)](https://coveralls.io/r/agiliq/django-wordpress?branch=master)


This is a Django App which allows easy
integration between athe Django and Wordpress.

All the core Wordpress tables are made available as Django models.

Installation & Usage
--------------------
* pip install -e git+git@github.com:agiliq/django-wordpress.git#egg=django-wordpress
* Add 'wp' to installed apps.
* Enter the wordpress database name in your database settings. 

Now, you can edit the wordpress database using django admin. And you can use templatetags for showing latest posts etc.

More details are available at
http://agiliq.com/blog/2010/01/wordpress-and-django-best-buddies/



