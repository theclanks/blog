Descompilando PYC
#################

:date: 2012-09-28 18:20
:tags: python
:category: Python
:author: The Clanks

Solução simples para descompilar arquivos pyc

.. code-block:: bash

    git clone https://github.com/zrax/pycdc
    cd pycdc make
    ./bin/pycdc Example.pyc > Example.py
