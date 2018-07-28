================================
Sphinx Version Warning Extension
================================


Sphinx Version Warning is a Sphinx_ extension that allows you to show a *Warning* banner at the top of your documentation.
The banner is shown based on the version that is displayed compared (using SemVer_) with the latest version on the server.

This extension was originally created to be compatible with `Read the Docs`_ API and currently it's the only backend that supports.

.. _Sphinx: http://www.sphinx-doc.org/
.. _SemVer: https://semver.org/
.. _Read the Docs: http://readthedocs.org/


How it works?
-------------

When visiting a page in Read the Docs that was built with this extension enabled,
an AJAX request is done to the Read the Docs servers to retrieve all the versions of the project.
These versions are compared against the one that we are reading and if it's an old version,
a red *Warning* banner appears at the top of the page.


Examples
--------

.. image:: warning-example.png

There is a live example living at Read the Docs:

- `latest`_ version doesn't show any kind of warning banner
- `0.0.1`_ version shows a custom and fixed message added at build time
- `0.0.2`_ version shows a warning banner saying that 0.0.3 is available (at the time of writing this docs)
- `0.0.3`_ version doesn't show any banner since it's the latest version (at the time of writing this docs)


.. _latest: https://sphinx-version-warning-example.readthedocs.io/en/latest/
.. _0.0.1: https://sphinx-version-warning-example.readthedocs.io/en/0.0.1/
.. _0.0.2: https://sphinx-version-warning-example.readthedocs.io/en/0.0.2/
.. _0.0.3: https://sphinx-version-warning-example.readthedocs.io/en/0.0.3/



Customization
-------------

Some customization can be done using the ``conf.py`` file of your Sphinx project:

versionwarning_enabled (bool)
   enable/disable version warning extension
versionwarning_default_admonition_type (string)
   type of admonition for the banner (warning, admonition or note)
versionwarning_default_message (string)
   default message for the warning banner
versionwarning_message (dict)
   mapping between versions and messages for its banners
versionwarning_message_placeholder (string)
   text to be replaced by the version number link from the message
versionwarning_project_slug (string)
   slug of the project under Read the Docs