Translation management and generation of static content with Transifex + Sphinx 
===============================================================================

:date: 2013-05-03 12:08
:tags: programacao, codigo, traducao
:category: Misc
:author: The Clanks

Hi, my name is Luis Carlos Otte Junior, I’m Brazilian and live at São Carlos, São Paulo.

The proposed project is at two parts, considering time and difficulty level: 

#. Website static generation with translations – 4 weeks – Easy

 #. Re-write the HTML pages for the Sphinx format (.rst file).

 #. Use sphinx-build to generate the .pot files and translate them in Transifex.

 #. After generating .mo translated file use the sphinx-build to generate the pages in each language. .. [#]_

 #. Use python-fabric to implement the deploy process (copying, compiling translation files, and build static files). [#]_

 #. Create a html template for sphinx with Language auto-selection.

#. Provide translated versions of images and screenshots – 8 weeks – Moderate

 #. Create an add-on for Transifex, reuse your classes (Project, user permission, and language) and implement the upload/export of the images according to the language.

 #. Create an extension in the Sphinx, to manage the correctly images at the generate static pages for each language. [#]_


 
Why do you want to work on this project?
----------------------------------------

I would like to work in this project because a wish learn more skills, working with international project, learn more English, relate with people from other countries, and, mainly, contribute to the open source community.

 
Why should we choose you?
-------------------------

I like to work and study in all that is necessary, specially Linux, Python, and PHP. Nowadays, I’m working with open source projects in a corporation. And I would like to be useful in anything.

 
Please list relevant academic, industry and/or open source experience
---------------------------------------------------------------------

I’m a graduate student of analysis and systems development and a developer on Virgos Co. (www.virgos.com.br) and work with Python/Django, C, and PHP development. Currently, I’m working in a data mining project with Django and Selenium RC, and others telecom projects using Asterisk, C programming and Python.


Example of .rst file
--------------------

.. include:: example.rst
   :literal:
   :code: rst
 

.. rubric:: References:

.. [#] Sphinx Internationalization: http://sphinx-doc.org/latest/intl.html
.. [#] python-Fabric: http://docs.fabfile.org/en/1.6/
.. [#] Sphinx Extensions: http://sphinx-doc.org/extensions.html
