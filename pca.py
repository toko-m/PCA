#coding: UTF-8

import json
import numpy as np

label_name = []

def mva_main():
	print "hoge"

class mva():

	def hoge():
		print "dammy"

class InputData():
	def __init__(self):
		self.mtrx_data = np.array([])
		self.label_name = []

	def create_data_from_json(self, input_json):
		json_list = json.load(input_json)

		for json_data in json_list:
			for name in json_data:
				value = json_data[name]
				if name == "name":
					label_name.append(value)
				elif name == "data":
					row = []
					for label in value:
						row.append(value[label])
					
					if self.mtrx_data.size:
						cp_mtrx_data = self.mtrx_data
						self.mtrx_data = np.vstack([cp_mtrx_data, row])
					else:
						self.mtrx_data = np.array(row)
		
	def create_data_from_csv(self, input_file):
		f = open(input_file)
		csv_data = json.load(f)

if __name__ == '__main__':
	input_data = InputData()

	f = open("sample.json")
	input_data.create_data_from_json(f)
	f.close()