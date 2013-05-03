Python 2.7 no Centos 5
======================

:date: 2012-09-20 18:20
:tags: python
:category: Python
:author: The Clanks

Parece algo bem fácil, mas é uma dor de cabeça, principalmente em versões de SO
muito antigas instalar mais de uma versão do Python para utilizar o nosso amigo
virtualenv, segue as instruções abaixo:

Instalando Python
-----------------

.. code-block:: bash

    $ wget http://www.python.org/ftp/python/2.7/Python-2.7.tgz
    $ tar xvzf Python-2.7.tgz
    $ cd Python-2.7
    $ ./configure --prefix=/usr/local
    $ make && make altinstall

O truque é utilizar altinstall, uma vez que o mesmo não vai influênciar a
versão atual instalada no SO.


Compilando o Setuptools e instalando pip e virtualenv
-----------------------------------------------------

.. code-block:: bash

    $ wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz#md5=7df2a529a074f613b509fb44feefe74e
    $ tar -xvf setuptools-0.6c11.tar.gz
    $ cd setuptools-0.6c11
    $ python2.7 setup.py install
    $ easy_install-2.7 install pip
    $ pip-2.7 install virtualenv

Novamente o segredo é utilizar nosso novo python2.7 na hora de compilar o
setuptools, caso contrário na hora de executar o virtualenv, o mesmo vai utilizar a
versão padrão do SO.
