import cgi
import cgitb
import pca

cgitb.enable(display=0, logdir="./log")

rcv_data = cgi.FieldStorage()
PCA_instance = None

if rcv_data is not None:
	PCA_instance = rcv_data.getvalue("PCA_type")
	input_data = rcv_data.getvalue("PCA_input")