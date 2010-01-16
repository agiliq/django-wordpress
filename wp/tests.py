"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import Template, Context
class SimpleTest(TestCase):
    def test_template_tags(self):
        template_string = """
        {% load wordpress_tags %}
        {% show_comments 5 %}
        {% show_posts 5 %}
        {% populate_comments 5 as commnts%}
        {% populate_posts 10 as posts %}
        """
        t = Template(template_string)
        c = Context({})
        t.render(c)