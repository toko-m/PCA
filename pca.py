#coding: UTF-8

import json
import numpy as np

label_name = []

class MtrxType():
	CORRELATION = "MTRX_TYPE_CORRELATION"
	VARIANCE_COVARIANCE = "MTRX_TYPE_VARIANCE_COVARIANCE"
	NORMARIZE = "MTRX_TYPE_NORMARIZE"

class PCA():
	def __init__(self, mtrx_type):
		self.InputData = InputData()
		self.eigen = []
		self.mtrx_type = mtrx_type

	def set_data_from_json(self, fp):
		self.InputData.create_data_from_json(fp)
		self.InputData.set_mtrx()

	def set_data_from_csv(self, fp):
		self.InputData.create_data_from_csv(fp)
		self.InputData.set_mtrx()

	def exist_inputdata(self):
		if self.InputData.origin.size:
			return True
		else:
			return False

	def calc_eigen_and_contr(self):
		if not self.exist_inputdata():
			raise Exception('InputData is null.')

		self.eigen = np.linalg.eigvals(self.InputData.origin)
		#print self.eigen
		contr = self.eigen / sum(self.eigen)
		#print contr 
		cum_contr = []
		cum_value = 0
		for contr_n in contr:
			cum_value = cum_value + contr_n
			cum_contr.append(cum_value)
		#print cum_contr

	def calc_coefficient(self):
		if not self.exist_inputdata():
			raise Exception('InputData is null.')

		print self.InputData.origin
		cnt = 0
		result = np.array([])
		for eigen_value in self.eigen:
			coef = []

			if self.mtrx_type is MtrxType.CORRELATION:
				print self.InputData.origin[:,cnt]
				coef = self.InputData.origin[:,cnt] * eigen_value
			elif self.mtrx_type is MtrxType.VARIANCE_COVARIANCE:
				print "var_covar"
			elif self.mtrx_type is MtrxType.NORMARIZE:
				coef = self.InputData.normarize[:,cnt] * eigen_value
			elif self.mtrx_type is None:
				raise Exception('mtrx_type is None.')
			else:
				raise Exception('Invalid mtrx_type %s.') % self.mtrx_type

			if result.size:
				cp_result = result
				result = np.vstack([cp_result, coef])
			else:
				result = coef
				
			cnt = cnt + 1

		print result

class InputData():
	def __init__(self):
		self.origin = np.array([])
		self.label_name = []
		self.correlation = np.array([])
		self.var_covar = np.array([])
		self.normarize = np.array([])

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
					
					if self.origin.size:
						cp_origin = self.origin
						self.origin = np.vstack([cp_origin, row])
					else:
						self.origin = np.array(row)
	
	def create_data_from_csv(self, input_file):
		f = open(input_file)
		csv_data = json.load(f)

	def set_mtrx(self):
		self.set_correration_mtrx()
		self.set_variance_covariance_mtrx()
		self.set_normarize_mtrx()

	def set_correration_mtrx(self):
		if not self.origin.size:
			raise Exception('Input data does not exist.')

	def set_variance_covariance_mtrx(self):
		if not self.origin.size:
			raise Exception('Input data does not exist.')

	def set_normarize_mtrx(self):
		if not self.origin.size:
			raise Exception('Input data does not exist.')

		average = np.mean(self.origin)
		inv_stddev = 1 / np.std(self.origin)

		self.normarize = (self.origin - average) * inv_stddev
		print self.normarize
		
if __name__ == '__main__':
	input_data = InputData()

	f = open("sample.json")
	PCA_instance = PCA(MtrxType.NORMARIZE)
	PCA_instance.set_data_from_json(f)
	PCA_instance.calc_eigen_and_contr()
	PCA_instance.calc_coefficient()
	f.close()