# python_basics
===============
This project is just for python beginners.  
I am also learning, so please pardon me for any errors.  
I am trying to share the codes I wrote when I was learning python.   
Thanks to the amazing work of Harrison, see <http://pythonprogramming.net>

This is the first part \-\- 
## basic python programming skills

The project contains a sery of codes:

## start.py

Start to play

## class.py 

A calulator class defining 'addition', 'subtraction', 'multiplication', and 'devision'. No \_\_init\_\_ added in this script.

## os_module.py

Introduce how to some directory manipulation methods:
  
 * os.mkdir:  make a new folder  
 * os.rename: rename a folder  
 * os.remdir: remove a folder

### examplecsv.py 
How to read a csv file in python

### matplotlib_module.py
plot a line/bar/scatter from data or csv/text file

### regex_module.py
Basci knowledge of regular expression

### subprocess_modelu.py
Call a command of shell in python script

### ftplib_module.py
Retreive and store a file from or on a ftp server  
If you want to run this code, fulfill in your domain name and server ip

### urllib_module.py & website_parsing.py
Use urllib and urllib2 package to read a url directly or through a request and scrap data from the website.

### threading_module.py
Use Queue and threading to fake a multiple thread process

### sockets_module.py
A low-level networking interface

### tkinter_makingwindows.py
The Tkinter module's purpose is to generate GUIs.  
A window with buttons and some functions is easily implemented.

### oop-example.py
This is a code using Tkinter module to demonstrate the object oriented programming power of python. This code is a littile bit difficult to totally understand. Just get a  general idea.

### setup.py
In this script, we use cx_Freeze to build a excutable for  an exsiting python script. In our case, *website_parsing.py* is used
Open the shell and run: (mind the directory of the setup.py locates in)

	python setup.py build

### pickle_module.py
Pickle is used to store objects.

### eval_module.py
The idea of eval is to evaluate an expression in the form of a string and return the value. 

### exec_module.py
exec built_in function can excute a lot of things directly. Kind of magic.

******************

**P.S.** All the above codes are written in python2

There is a simple way transfering python2 scripts to python3. Just do it in the command shell

	2to3 python2ugliness.py
	
or

	2to3 -w python2ugliness.py
	
With the additional -w (standing for write), we are able to write the changes to the file. You should also see a .bak file, which is a backup of the original file.
