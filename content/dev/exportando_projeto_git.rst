Exportando seu projeto no GIT para tar.bz2
==========================================

:date: 2012-10-10 11:52
:tags: programacao, codigo, git
:category: Misc
:author: The Clanks

Para exportar seu projeto basta executar o comando abaixo na pasta raiz do
projeto:

.. code-block:: bash

    git archive --format tar master | bzip2 > ../../../projeto.tar.bz2
