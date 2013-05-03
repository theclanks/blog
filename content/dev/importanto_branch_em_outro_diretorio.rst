Importando um branch qualquer em sub-diretório no Master
========================================================

:date: 2013-02-04 11:33
:tags: git, svn
:category: Misc
:author: The Clanks
:email: jrluiscarlos@yahoo.com.br

Com nosso amigo Git, é possível importarmos um branch qualquer, em um sub-diretório dentro do branch Master. Mas para que isso? Oras é uma boa solução para quem trabalha com svn (infelizmente) e se depara com aquelas pastas branch, trunk e tag e não quer colocar isso tudo no seu repositório só git e as vezes remoto, por exemplo.

Abaixo a seqüência do processo bem simples com o comando git read-tree:

Vamos começar por exemplo com um repositório remoto dentro de um repositório
git-svn, vou adicionar ele em um branch:

.. code-block:: bash

    git remote add remote_foo https://theclanks@bitbucket.org/theclanks/foo.git
    git fetch remote_foo
    git checkout -b remote_foo remote_foo/master

Agora temos um branch com nosso projeto git puro, próximo passo vem o
read-tree apontando para pasta trunk do svn:

.. code-block:: bash

    git checkout master
    git read-tree --prefix=trunk/projeto/codigo_fonte/ -u remote_foo
    git merge --squash -s subtree --no-commit remote_foo

Pronto, nosso projeto está pronto para um commit:

.. code-block:: bash

    git commit -m "Projeto: Inclusao codigo no repositorio"
    git svn dcommit

Para maiores informações, segue a página do manual git: http://git-scm.com/book/ch6-7.html

