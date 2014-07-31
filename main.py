#!/usr/bin/python

import cgi
import cgitb
import pca
import os

cgitb.enable()


if os.environ['REQUEST_METHOD'] != "POST":
	raise Exception ('Request must be post.')

rcv_data = cgi.FieldStorage()
PCA_instance = None

if rcv_data is None:
	raise Exception ('Receive data is none.')

PCA_instance = rcv_data.getvalue("PCA_type")
input_data = rcv_data.getvalue("PCA_input")

print "Content-type:text/html\n\n"
print "hogee"