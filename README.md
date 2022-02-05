# bookr
This repo houses my work to create the sample bookr app, a Django app suggested as part of the book [Web Development with Django: Learn to build modern web applications with a Python-based framework](https://www.goodreads.com/book/show/57330076-web-development-with-django).

I do indeed realize the irony of creating an app called bookr and the linking to a goodreads entry. 

# Basic Rules

There is only one contributor here, myself. That being said, I'm establishing basic rules just in case anyone else comes in to add to this:
* Use a branching strategy. Don't push directly to main.
* Don't commit dead code or dead files. 
* Dockerize.


# Some Gotchas

The book uses a <=3.0 version of Django as a guide. I am not actually interested in this. 

As a result, I am choosing to follow the book as closely as possible, except when it doesn't
actually make sense and will result if needless tech debt. This section is for capturing gotchas,
or other things that might come up because the book is based on an older version of Django:

* Be aware of BASE_DIR in settings.py. In <=3.0 this value is created as a string, in >=3.1, it is a pathlib.Path object.
* The book suggests using the django-admin startproject command to get a project dir layout started. Since this is
a solo project that won't reach many people, I am fine with that. If I were working on something intended for consumption
by multiple users in a production setting, I would prefer to use [Cookiecutter Django](https://cookiecutter-django.readthedocs.io/en/latest/). 
