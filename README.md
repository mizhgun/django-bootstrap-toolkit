**!!!This is the fix to support leagacy bootstrap2 layout on Django 2.x!!!**

Django Toolkit for integration with Bootstrap v2
================================================

The easiest way to use Bootstrap v2 in your Django project. What is Bootstrap? You can find out all about it here: http://getbootstrap.com


This project is retired
-----------------------

The time for development on Bootstrap v2 has passed. This app is provided 'as is', and will not be updated.

Everyone using Django and Bootstrap is encouraged to upgrade to `django-bootstrap3`. You can find it at https://github.com/dyve/django-bootstrap3.


Installation
------------
1. Install using pip:

        pip install django-bootstrap-toolkit

2. Add to INSTALLED_APPS:

        'bootstrap_toolkit',

Alternatively, you can add `django-bootstrap-toolkit` to your requirements.txt.

If you want to hack django-bootstrap itself, clone this repo and call `pip install -e .`.

Use in templates
----------------

    {% load bootstrap_toolkit %}

    # Using a filter

    <form action="/url/to/submit/" method="post">
        {% csrf_token %}
        {{ form|as_bootstrap }}
        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>

    # Using template tags

    <form action="/url/to/submit/" method="post" class="form">
        {% csrf_token %}
        {% bootstrap_form form layout="vertical" %}
        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>

Use in forms
------------

    class TestForm(forms.Form):
        date = forms.DateField(
            widget=BootstrapDateInput(),
        )
        title = forms.CharField(
            max_length=100,
            help_text=u'This is the standard text input',
        )
        uneditable = forms.CharField(
            max_length=100,
            help_text=u'I am uneditable and you cannot enable me with JS',
            initial=u'Uneditable',
            widget=BootstrapUneditableInput()
        )
        prepended = forms.CharField(
            max_length=100,
            help_text=u'I am prepended by a P',
            widget=BootstrapTextInput(prepend='P'),
        )

More examples
-------------

See Django project `demo_project/demo_app` for more examples.

TODO
----

- Create a more easy way to customize BootstrapDateInput


Questions
---------

Do you have a question about the usage of this toolkit in your Django project? Please ask it on StackOverflow.com so others can help out and/or learn. Label your question django-bootstrap-toolkit if possible.

http://stackoverflow.com/

Bugs and requests
-----------------

If you have found a bug or a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/dyve/django-bootstrap-toolkit/issues

About
-----

django-bootstrap-toolkit is written by Dylan Verheul (dylan@dyve.net).

History
-------

When building my first Django project with Bootstrap I went looking for available open source applications that connected Django and Bootstrap.

I found  https://github.com/tzangms/django-bootstrap-form. The approach to template tags and filters seemed right, but Bootstrap does so much more than just forms.

This is how `django-bootstrap-toolkit` started. I used ideas from other Django apps. The code was started from scratch.

License
-------

You can use this under Apache 2.0. See LICENSE file for details.

Thanks
------

* to Twitter, @fat and @mdo for building and releasing Bootstrap
* to the Django community for Django
* to the authors of django-bootstrap-form for the inspiration
* to Stefan Petre and Andy Rowles for the datepicker https://github.com/eternicode/bootstrap-datepicker
