# -*- coding: utf-8 -*-
# @Author: Yang Chen
# @Date:   2020-04-10 22:08:21
# @Last Modified by:   chenyang
# @Last Modified time: 2020-04-11 04:11:10

import json
import sys


def main(JSON_A_file, JSON_B_file):
	with open(JSON_A_file) as f:
	  JSON_A = json.load(f)

	NumLocker = []
	for k, v in JSON_A.items():
		x = k.split("_")
		numLocker = x[1]
		numLocker = int(numLocker)
		NumLocker.append(numLocker)

	NumLocker = list(set(NumLocker))
	NumLocker.sort()

	JSON_B = {}
	for i in NumLocker:
		JSON_B[i] = {}

	for k, v in JSON_A.items():
		x = k.split("_")
		for i in NumLocker:
			if x[1] == str(i):
				if x[2] == 'door':
					JSON_B[i]['door'] = v
				if x[2] == 'item':
					JSON_B[i]['item'] = v
				if x[2] == 'light':
					JSON_B[i]['light'] = v
				if x[2] == 'unlock':
					JSON_B[i]['unlock'] = v

	with open(JSON_B_file, 'w') as json_file:
	  json.dump(JSON_B, json_file, indent = 4, sort_keys=True) # Pretty Writing JSON string into a file

main(sys.argv[1], sys.argv[2])
