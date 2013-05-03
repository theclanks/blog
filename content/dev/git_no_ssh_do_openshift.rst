Git no ssh do Openshift
=======================

:date: 2012-09-10 18:20
:tags: python, git
:category: Misc
:author: The Clanks

Para utilizarmos o Git direto no servidor Openshift, precisamos trabalhar com
as variáveis:

* GIT_DIR “Diretório do git”
* GIT_WORK_TREE “Diretório raiz do projeto”

Você pode exporta-las para economizar comandos:

.. code-block:: bash

    $ export GIT_WORK_TREE=$HOME"/blog/repo/"
    $ export GIT_DIR=$HOME"/git/blog.git/"
