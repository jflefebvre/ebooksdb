#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import string
import fnmatch
import os
import sys
import time

import argparse

extensions = ['pdf', 'epub', 'chm']
folders_path = [r'/Users/jeff/Downloads/ebooks', r'/Volumes/STUDIO/ebooks', r'/Volumes/Shawinigan/ebooks']
db_path = r'/opt/local/bin/ebooks.db'

parser = argparse.ArgumentParser(description="Allow to build or find ebooks")
parser.add_argument("-f", "--find", help="find ebook")
parser.add_argument("-b", "--build", help="build database",action="store_true")
args = parser.parse_args()
if args.build:

	def listFiles(dir):
	    rootdir = dir
	    for root, subFolders, files in os.walk(rootdir,topdown=False):
	        for file in files:
	            yield os.path.join(root,file)
	    return

	def addEbook(cur, dir):
	    c = 1
	    for f in listFiles(dir):
	        try:
	            base = os.path.basename(f)
	            base_dir = os.path.dirname(f)
	            filename_split = os.path.splitext(base)
	            ext = filename_split[1]
		    ext = string.replace(ext, '.', '')
	            filesize = os.path.getsize(f)
	            if ext in extensions:
	                c+=1
	                cur.execute("INSERT INTO ebooks(Name, Path, Ext, Filesize, CreationDate) VALUES(?,?,?,?,?)", (base, base_dir, ext, str(filesize),time.ctime(os.path.getctime(f)))) 
	        except OSError as e:
	            pass
		    # print "" #"I/O error({0}): {1}".format(e.errno, e.strerror)

	    print str(c) + " ebooks inserted"

	    return

	con = lite.connect(db_path)
	con.text_factory = str
	with con:
	    cur = con.cursor()   
	    cur.execute("DROP TABLE IF EXISTS ebooks") 
	    cur.execute("CREATE TABLE ebooks(Id INTEGER PRIMARY KEY, Name TEXT, Path TEXT, Ext Text, Filesize INT, CreationDate DateTime Text)")
	    for f in folders_path:	
		addEbook(cur, f)

else:
	if args.find:
		con = lite.connect(db_path)
		with con:    		    
		    cur = con.cursor()    
		    cur.execute("PRAGMA case_sensistive_like=ON;");
		    cur.execute("SELECT * FROM ebooks WHERE Name LIKE ? ORDER BY Name ASC", ['%'+args.find+'%'])

		    rows = cur.fetchall()

		    print string.ljust("FILENAME", 80) + ' ' + string.ljust("CREATION DATE", 25)  + ' ' + string.ljust("PATH", 100)
		    print ''.ljust(80, "-") + ' ' + ''.ljust(25, "-") + ' ' + ''.ljust(100, "-")
		    c = 0
		    for row in rows:
		        c += 1
		        print string.ljust(row[1].encode('utf-8')[0:75], 80) + ' ' + string.ljust(row[5].encode('utf-8'), 25)  + ' ' + row[2].encode('utf-8')
		    print "Found " + str(c) + " ebooks"

		#print "no build, we search for " + str(args.find)
	else:
		print parser.print_help()
