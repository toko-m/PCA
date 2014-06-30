#coding: UTF-8

import json
import numpy as np

label_name = []

def mva_main():
	print "hoge"

class PCA():
	def __init__(self):
		self.InputData = InputData()

	def set_data_from_json(self, fp):
		self.InputData.create_data_from_json(fp)

	def set_data_from_csv(self, fp):
		self.InputData.create_data_from_csv(fp)

	def eigen_and_contr(self):
		eigen = np.linalg.eigvals(self.InputData.mtrx_data)
		print eigen
		contr = eigen / sum(eigen)
		print contr 


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
	PCA_instance = PCA()
	PCA_instance.set_data_from_json(f)
	PCA_instance.eigen()
	f.close()