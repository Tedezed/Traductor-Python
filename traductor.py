#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from translate import Translator
from progress_bar import printProgress

# Definir idiomas
translator= Translator(from_lang="en", to_lang="es")

# Definir ficheros y convertir en cadena
f = open("files", 'r')
files_read = f.read()
f.close()
list_rst_files = files_read.split('\n')

for file_rst in list_rst_files:
	f = open(file_rst, 'r')
	f_read = f.read()
	f.close()

	print "Traduciendo %s" % (file_rst)
	# Separar cadena por linias e ignorar algunas
	list_file = f_read.split('\n')
	init_list = 0
	len_list = len(list_file) - 1
	printProgress(init_list, len_list, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
	for n,line in enumerate(list_file):
		if line[:3] not in (".. ", "   ", "* :", "", "===", "---"):
			text = translator.translate(line)
			if text.split(':')[0] == "MYMEMORY WARNING":
				raise Exception("MYMEMORY WARNING QUOTAREACHED: VISIT HTTP://MYMEMORY.TRANSLATED.NET/DOC/QUOTAREACHED")
			list_file[n] = text
		printProgress(n, len_list, prefix = 'Progreso:', suffix = 'Completado', barLength = 50)

	# Pasar de nuevo a cadena
	doc = ""
	for line in list_file:
		doc = doc +  " \n" + line

	# Guardar cadena
	f = open(file_rst, 'w')
	f.write(doc.encode('utf8'))
	f.close()
