Resolvendo problemas de acentuação módulo Shutil - Python
=========================================================

:date: 2012-09-20 18:20
:tags: python
:category: Python
:author: The Clanks

Após muito sofrimento e horas de tortura com um problema de acentuação, encontrei
uma solução válida para utilização do módulo shuitil com arquivos que possuem acentução.
Utilizando a função .encode("utf-8")

Segue o Erro gerado antes da função:

* UnicodeDecodeError: 'ascii' codec can't decode byte

.. code-block:: python

    import shutil
        shutil.move(origem, destino.encode("utf-8"))
