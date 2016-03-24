zbar_ctypes
===========

This is libzbar python ctypes bindings, it should support python2 and python3.

I can not find a python3 version zbar library under raspberry pi, so i write this codes for it.
  
It should work under other platform only need replace the libzbar path.  

It only test under Raspbian (raspberry pi) now.


Usage
-----

- Install (on raspberry pi)  
    - install libzbar::
    
        audo apt-get install libzbar0  
    
    - install libzbar_ctypes::

        hg clone https://bitbucket.org/zaazbb/libzbar_ctypes
        cd libzbar_ctypes
        sudo python3 setup.py install  

- Example (on raspberry pi)  
    - install pillow  
        install Prerequisites packages. see http://pillow.readthedocs.org/en/latest/installation.html  
        download pillow source code (http://python-pillow.github.io/), and compile it.  
    
    - run the example script.
  
todo
----

Add all libzbar function bindings.

Contact
-------

by jf.  

zaazbb <zaazbb@163.com>
