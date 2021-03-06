#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, sys

class Config(object):
	def __init__(self):
		self.input_folder = sys.argv[1]
		self.output_folder = sys.argv[2]
		if len(sys.argv) > 3:
		  self.extension = sys.argv[3]
		else:
		  self.extension = None
		
def create_dir(config, ext):
	if not os.path.exists(config.output_folder + ext):
		os.makedirs(config.output_folder + ext)
		
def move_internal(config, extension, f):
  destination = config.output_folder + extension  + '/' + f
  source = (config.input_folder + f)
  print '\tMoving [' + f + '] from ' + source + ' to ' + destination
  os.rename(source, destination)
		
def move(config):
	files = os.listdir(config.input_folder)
	
	for f in files:
		extension = os.path.splitext(f)[1][1:].lower()

		if os.path.isfile(config.input_folder + f):
			create_dir(config, extension)
	
			if config.extension == extension:
			  move_internal(config, extension, f)
			elif config.extension == None:
			  move_internal(config, extension, f)

def main():
	config = Config()
	move(config)

if __name__ == '__main__':
	main()




