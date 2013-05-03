Removendo diretórios .svn redundantes pós commit
================================================

:date: 2013-02-04 13:53
:tags: git, svn
:category: Misc
:author: The Clanks


Abaixo alguns comandos para corrigir essa "praga" que ocorre no svn, quando esses malditos .svn em sub-diretórios conseguem escapar pelo commit do git-svn e vão parar no repositório do servidor.

Para quem utiliza git-svn não há problema, mas se alguém quiser rodar o checkout pelo svn puro, o mesmo se perde e não sabe o que fazer com esses diretório causando um erro e interrompendo o checkout, resultado você quebrou o repositório. ;)

Segue a seqüência que deve ser feita no servidor ou local do repositório svn:

1. Precisamos realizar um dump do repositório para backup e para trabalharmos nele posteriomente, para utilizamos o comando svnadmin:

.. code-block:: bash

    svnadmin dump /svnroot/foo > /root/foo

2. Agora vamos "filtrar" as pragas isso mesmo, esse é o grande truque, podendo especificar mais de um .svn se for o caso:

.. code-block:: bash

    svndumpfilter exclude "trunk/php/common/css/theme/images/.svn" "trunk/php/common/css/theme/.svn" < /root/foo > /root/foo-filtered

Deu certo?, se mostrar os arquivos removidos "dropeds" sim!, lembrando que se você estiver utilizando uma versão mais nova do svn, esse comando tem suporte a pattern, não foi meu caso, para variar.

3. Remova o respositório atual:

.. code-block:: bash

    rm -rf /svnroot/foo

4. Vamos criar um novo:

.. code-block:: bash

    svnadmin create /svnroot/foo

5. Agora é só importar o dump filtrado para seu novo repositório:

.. code-block:: bash

    svnadmin load /svnroot/foo < /root/foo-filtered


