#!/usr/bin/env python

import sys
import os
import xml.etree.ElementTree as ET
import localizable

if len(sys.argv) < 4:
	print("%s source_android_strings.xml reference_lproj_dir dest_lproj_dir" % sys.argv[0])
	sys.exit(-1)

source_strings = sys.argv[1]
ref_lproj = sys.argv[2]
dest_lproj = sys.argv[3]

def load_strings(strings):
	result = dict()
	resources = ET.parse(strings).getroot()
	for string in resources:
		result[string.attrib['name']] = string.text
	return result

def load_lproj_strings(strings):
	result = dict()
	strings = localizable.parse_strings(filename=strings)
	for entry in strings:
		result[entry['key']] = entry['value']
	return result

def save_lproj_strings(filename, strings):
	with open(filename, "w") as file:
		for key in strings.keys():
			file.write(("\"%s\" = \"%s\";\n" % (key, strings[key])).encode('utf-8'))
		file.close()

def convert(android):
	return android.replace("%s", "%@");

source = load_strings(source_strings)

for file in os.listdir(ref_lproj):
	ref_lproj_strings = load_lproj_strings(ref_lproj + '/' + file)

	result = {}
	for item in ref_lproj_strings.keys():
		key = ref_lproj_strings[item]
		try:
			result[item] = convert(source[key])
		except:
			result[item] = key

	save_lproj_strings(dest_lproj + '/' + file, result)
