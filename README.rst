millipede
=========

.. image:: https://travis-ci.org/evadot/millipede.svg
           :target: https://travis-ci.org/evadot/millipede

.. image:: https://go-shields.herokuapp.com/license-MIT-blue.png

Print a beautifull millipede to send to your friends !!!

Basic usage::

 $ millipede 20 "Chaud devant! Mon mille-pattes doit passer!"
 
 Chaud devant! Mon mille-pattes doit passer!
 
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

  $ milliped 20 -t bocal 'Chaud devant! Mon beau mille-pattes doit passer!'
 
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

Test in a confined environment
==============================

::

 $ docker build -t millipede .
 $ docker run millipede
