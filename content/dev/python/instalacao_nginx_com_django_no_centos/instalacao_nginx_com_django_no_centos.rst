Instalação Nginx com Django no CentOS 5
=======================================

:date: 2012-09-20 18:20
:tags: python
:category: Python
:author: The Clanks

Instalação Nginx
----------------

Para instalar o Nginx no Centos basta seguir o tutorial no site do projeto, ou
adicione o seguinte arquivo na lista de repositórios do Centos:

* /etc/yum.repos.d/nginx.repo

..  code-block:: ini

     [nginx]
     name=nginx repo
     baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
     gpgcheck=0
     enabled=1

Após isso instalar com o comando: yum install nginx.

Configurando Nginx
------------------

Após instalação crie um arquivo no seguinte diretório: /etc/nginx/conf.d/
com as seguintes linhas abaixo, lembrando que você pode configura-lo na porta
que desejar.

.. code-block:: nginx

    server {
        listen 8000;
        server_name projeto;
        access_log /var/log/nginx/projeto.access.log;
        error_log /var/log/nginx/projeto.error.log;

        location /static/ {
          alias /home/user/projeto/static/; # STATIC_ROOT
          expires 30d;
        }

        location /media/ {
           alias /home/user/projeto/media/; # MEDIA_ROOT
           expires 30d;
        }

        location / {
          include fastcgi_params;
          fastcgi_pass 127.0.0.1:8080;
          fastcgi_split_path_info ^()(.*)$;
        }
      }

Ativando o daemon do Django
---------------------------

Eu criei um script de inicialização feito para sistemas RedHat, aproveitando
o script utilizado no Celeryd. Embora você pode ativar o daemon quando quiser
com o comando:

* ./manage.py runfcgi method=prefork host=127.0.0.1 port=8080

.. code-block:: bash

    #!/bin/bash
    #
    # projeto
    # chkconfig: - 80 05
    # description: projeto daemon
    #

    ### BEGIN INIT INFO
    # Provides:          projeto
    # Required-Start:    $mysqld
    # Required-Stop:     $mysqld
    # Default-Start:
    # Default-Stop:
    # Description:       projeto daemon
    # Short-Description: Enable Django projeto
    ### END INIT INFO

    # config: /etc/sysconfig/projeto
    # pidfile: /var/run/projeto.pid

    # source function library
    . /etc/rc.d/init.d/functions

    # pull in sysconfig settings
    #[ -f /etc/sysconfig/projeto ] && . /etc/sysconfig/projeto

    RETVAL=0
    prog="projeto"

    DJANGO_PID_FILE="/var/run/projeto.pid"
    DJANGO_LOG_FILE="/var/log/projeto.log"
    DJANGO_LOG_LEVEL="INFO"
    DEFAULT_DJANGO="DJANGO"
    DJANGO_PROJECT_DIR="/home/user/projeto"
    PYTHON_PATH="/home/user/projeto/env/bin/python"
    DJANGO_PORT="8080"
    DJANGO_BIND="127.0.0.1"

    if [ -z "$DJANGO" ]; then
        if [ ! -z "$DJANGO_PROJECT_DIR" ]; then
            DJANGO="$PYTHON_PATH $DJANGO_PROJECT_DIR/manage.py"
            DJANGO_OPTS="runfcgi method=prefork host=$DJANGO_BIND port=$DJANGO_PORT pidfile=$DJANGO_PID_FILE"
        else
            DJANGO=$DEFAULT_DJANGO
        fi
    fi

    cd $DJANGO_PROJECT_DIR

    #DJANGO_OPTS="$DJANGO_OPTS -f $DJANGO_LOG_FILE -l $DJANGO_LOG_LEVEL"
    #if [ -n "$2" ]; then
    #    DJANGO_OPTS="$DJANGO_OPTS $2"
    #fi

    exec="$DJANGO $DJANGO_OPTS"

    start()
    {
            echo -n $"Starting $prog: "
            daemon --pidfile=${DJANGO_PID_FILE} $exec 2>/dev/null
            RETVAL=$?
            echo
            [ "$RETVAL" = 0 ] && touch /var/lock/subsys/projeto
            return $RETVAL
    }

    stop()
    {
            echo -n $"Stopping $prog: "
            killproc -d 10 $exec -TERM
            RETVAL=$?
            if [ "x$runlevel" = x0 -o "x$runlevel" = x6 ] ; then
                killall $exec 2>/dev/null
            fi
            echo
            [ "$RETVAL" = 0 ] && rm -f /var/lock/subsys/projeto /var/run/projeto /var/run/projeto.pid
            return $RETVAL
    }


    case "$1" in
            start)
                    start
                    ;;
            stop)
                    stop
                    ;;
            restart)
                    stop
                    start
                    ;;
            status)
                    status projeto -p $DJANGO_PID_FILE
                    RETVAL=$?
                    ;;
            \*)
                    echo $"Usage: $0 {start|stop|restart|status}"
                    RETVAL=1
    esac
    exit $RETVAL

Referências:

* Django and Nginx DjangoAndNginx_

  .. _DjangoAndNginx: https://code.djangoproject.com/wiki/DjangoAndNginx

