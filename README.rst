millipede |build-status|
========================

Print a beautifull millipede to send to your friends !!!

Basic usage::

 $ millipede 20 "Chaud devant! Mon millepatte doit passer!"
 
 Chaud devant! Mon millepatte doit passer!
 
     ╚⊙ ⊙╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝
    ╚═(███)═╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝
    ╚═(███)═╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝

There's also a very convenient `-r` option to reverse the millipede::
 
 $ millipede -r 20 'Aaah, il est passé !'
 
  ╔═(███)═╗
   ╔═(███)═╗
    ╔═(███)═╗
     ╔═(███)═╗
     ╔═(███)═╗
    ╔═(███)═╗
   ╔═(███)═╗
  ╔═(███)═╗
 ╔═(███)═╗
  ╔═(███)═╗
   ╔═(███)═╗
    ╔═(███)═╗
     ╔═(███)═╗
     ╔═(███)═╗
    ╔═(███)═╗
   ╔═(███)═╗
  ╔═(███)═╗
 ╔═(███)═╗
  ╔═(███)═╗
   ╔═(███)═╗
     ╔⊙ ⊙╗
 
 Aaah, il est passé !

Customize the millipede::

  $ milliped 20 -t bocal 'Chaud devant! Mon beau millepatte doit passer!'
 
     ╚⊙ ⊙╝
   ╚═(🐟🐟🐟)═╝
  ╚═(🐟🐟🐟)═╝
 ╚═(🐟🐟🐟)═╝
  ╚═(🐟🐟🐟)═╝
   ╚═(🐟🐟🐟)═╝
    ╚═(🐟🐟🐟)═╝
     ╚═(🐟🐟🐟)═╝
     ╚═(🐟🐟🐟)═╝
    ╚═(🐟🐟🐟)═╝
   ╚═(🐟🐟🐟)═╝
  ╚═(🐟🐟🐟)═╝
 ╚═(🐟🐟🐟)═╝
  ╚═(🐟🐟🐟)═╝
   ╚═(🐟🐟🐟)═╝
    ╚═(🐟🐟🐟)═╝
     ╚═(🐟🐟🐟)═╝
     ╚═(🐟🐟🐟)═╝
    ╚═(🐟🐟🐟)═╝
   ╚═(🐟🐟🐟)═╝
  ╚═(🐟🐟🐟)═╝
 

HTTP Post
=========

You can send the millipede as POST data to a HTTP server::

  millipede 10 --http-host=http://localhost:5000/ --http-name message

Using --http-auth you can specify a username/password for authentication::

 millipede 10 --http-host=http://localhost:5000/ --http-name message --http_auth=user:pass

And using --http-data key=value to can add more variables::

 millipede 10 --http-host=http://localhost:5000/ --http-name message --http-auth=user:pass --http-data myvar=mydata

RCFile
======

Some default settings can be set from a rcfile.

Here is a sample of a rcfile::

 # set default size to 10
 size 10
 comment I'm the millipede!
 reverse true
 opposite false
 template default
 # position 3

The millipede looks for the following files::

  ${HOME}/.millipederc
  /usr/local/etc/millipederc
  /etc/millipederc

Installation from sources
==========================

::

 # create a virtualenv
 $> virtualenv myenv
 $> source myenv/bin/activate
 
 # install (for developement)
 $> pip install -e .
 # Or, to install dependencies to send SMS
 $> pip install -e .[sms]
 
 # install (for production)
 $> pip install .

Run millipede on your Scaleway C1 server
========================================

::

 # Install Scaleway CLI
 $> curl -L https://github.com/scaleway/scaleway-cli/releases/download/v1.1.0/scw-`uname -s`-`uname -m` > /usr/local/bin/scw
 chmod +x /usr/local/bin/scw

 # Login
 $> scw login --token=<your_token> --organization=<your_organization>

 # Run millipede on your C1 server
 $> ./millipede.scw scw run --name=milliped ubuntu-trusty
 $> ./millipede.scw
 [+] Creating your millipede server...
 [+] Server created: 77b531d8-b954-405f-988e-82e79486acf7
 [+] Booting...
 [+] Server is booted
 [+] Installing millipede...
 [+] Running millipede
 My millipede is magnificent
     ╚⊙ ⊙╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝
     ╚═(███)═╝
     ╚═(███)═╝
    ╚═(███)═╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝
     ╚═(███)═╝
     ╚═(███)═╝
    ╚═(███)═╝
   ╚═(███)═╝
  ╚═(███)═╝
 [+] Stopping the server
 [+] Server stopped
 [+] Deleting server
 [+] Server deleted

Test in a confined environment
==============================

::

 $ docker build -t millipede .
 $ docker run millipede


.. |build-status| image:: https://travis-ci.org/getmillipede/millipede-python.svg
   :target: https://travis-ci.org/getmillipede/millipede-python
