======
Center
======

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
  :alt: Gitter
  :target: https://gitter.im/axju/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link

.. image:: https://img.shields.io/twitter/url/https/github.com/axju/axju.svg?style=social
  :alt: Twitter
  :target: https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Faxju%2Faxju

A very small and lightweight project management tool.


Features
--------
- lightweight
- fast work flow
- unlimited projects
- classify projects according to priority
- track the progress of each project
- setup your own server or sing up


Why?
----
My project management is really simple. I do some crazy stuff, after a wile I
lose the focus and start another project. So I have a lot of old and lost
projects. Some times I looked to my old project and try to find out which one
should I finished. I have many lists but they are garbage. To solve my problem,
I searched for programs that fit my needs. But did not find it. :(

The software developer in me is happy. Another project for my list. :D

I design the project so that it meets my requirements. A simple list I can look
throw, save the process and the priority. Every time I look on the list, the
most import project is the first. I hope that I focus more on one project.


Development
-----------
Yes it is still under develop. Some short facts:

- django project
- bootstrap 4
- uses django-crispy-forms
- test with python 3.6 and 3.7
- on win7 and linux

Setup::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip
  pip install -r requirement/production.txt
  pip install -r requirement/development.txt

Configure::

  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

Internationalization::

  python manage.py makemessages
  django-admin makemessages -a
  django-admin makemessages -l de

  python manage.py compilemessages
  django-admin compilemessages

To Do:

- password reset
- change password
- user help
- testing
- document
