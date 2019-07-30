#/usr/bin/python
#coding=utf-8
import sys,os

#print(sys.version_info)
#python 版本
#print(sys.version_info[0])

if sys.version_info[0] != 3:
      sys.exit()
else:
      pass


import platform
print(help(platform))
print(platform.python_revision())
print(platform.version())
print(platform.uname())

import os




