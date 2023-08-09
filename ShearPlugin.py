# -*- coding:utf-8 -*-
import os
import sys
import string

#if len(sys.argv) < 4:
#	print ("Please input original file name, output file name, cutting length successively")
#	exit(0)

import PyPluMA
import PyIO

class ShearPlugin:
    def input(self, inputfile):
       self.parameters = PyIO.readParameters(inputfile)

    def run(self):
       pass

    def output(self, out_file):
       file_name = PyPluMA.prefix()+"/"+self.parameters["file_name"]
       cut_len = int(self.parameters["cut_len"])
       top = []
       lines = []
       with open (file_name,"r") as f:
        line1 = f.readlines()
        for e in line1:
           if e.startswith('>'):
              r = e.strip()
              top.append(r)	
           else:
              s = e.strip()
              lines.append(s)
        str1 = ''.join(lines)
       with open (out_file,'w+') as f_2:
        num = len(str1)//cut_len
        for i in range(num):
           f_2.write(">" + str(i+1) + "\n")
           f_2.write(str1[i*cut_len:(i+1)*cut_len] + "\n")
