Teste de Stress no Asterisk c/ SipP
===================================

:date: 2012-12-06 15:52
:tags: programacao, teste, asterisk
:category: Asterisk
:author: The Clanks


Teste simples de stress no Asterisk com a ferramenta SipP:

.. code-block:: bash

    sipp -sn uac -d 20000000 -s 701 192.168.0.244 -l 100 -mp 5606 -i "192.168.0.246" -r 300 -rp 3600
