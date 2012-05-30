Django test autocompletion
==========================

This package provides a helpfull way to run specific tests within your project.

Agilizates the invocation of tests to run by providing autocompletion inside
test modules, listing its TestCases and also tests inside each TestCase.

This first release is a proof-of-concept, and in the "Future features" section
there is a list of possible improvements considered for next releases.


How does it work
----------------

In order to make a non-intrusive installation, instead of coupling this
autocompletion with the one provided by Django, we created a proxy command
named "djntest" which work is to redirect every call to itself to
"python manage.py test".

Later we defined our customized autocompletion for this new command.
Autocompletion is defined with a lightweight layer of bash code that it's
invoked each time the user triggers autocompletion (tipically by hitting the
<TAB> key). Based on the provided arguments, the bash layer decides to call the
helper python script get_testcases.py which in turn reads the provided .py
file, and parse it using the *ast* module.


How to use
----------

Located at the root of your django project, typing:

    $ djntest books_application/tests/test_book_creation.py:<TAB>

will list all classes defined in that file, in the standard bash way, ie:
 * if there is only 1 option, it will be automatically completed
 * if all the options at a given time have the same prefix, it's autocompleted
 * if you start typing the name of some TestCase after the colon, hitting <TAB>
   again will filter the offer to only those matching with what you are writting

After a TestCase name, if you a point and trigger autocompletion like this

    $ djntest books_application/tests/test_book_creation.py:TestStore.<TAB>

you will see listed all functions defined inside that class which name starts
with "test_", and again, with all the usual bash autocompletion features.


Disclaimer Notes:
-----------------

 * this autocompleter only facilitates the way of invoking the command for
   your running tests. Nothing related with PYTHONPATH is done here.


Installation Notes:
-------------------

In order to install this package you need to follow 2 steps:

1. First install the script

    $ sudo pip install django-test-autocomplete

Alternatively, you can install it from the source distribution:
Extract the tarball and run

    $ python setup.py install

2. For enabling the bash autocompletion you need to look for the
script djntest.sh located in the source distribution, and later:

 * load it inside your $HOME/.bashrc adding a line like this:

    source path/to/djntest.sh

 * copy the file into your bash configuration folder like this:

    $ copy path/to/djntest.sh /etc/bash_completion.d/


Extra:
For running tests you will have to install mock package first.


Future features:
----------------

 * Improve the python file parsing (done now with ast) for:
    - Detecting if defined clases are TestCases or not
    - Detect tests defined on parent TestCases
 * Clear integration with the usual way of running django tests (ie, avoid the need of
   "proxy" command djntest)
 * Try it out with not-only django projects
 * Support for some other shells (zsh will probably be the next)


Tested with:
------------
 * GNU bash, version 4.2.10
 * Django 1.3
 * I'm using together with django-nose without problems. I see no reason for
   have it not working without nose