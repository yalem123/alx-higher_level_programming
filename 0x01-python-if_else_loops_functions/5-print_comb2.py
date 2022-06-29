#!/usr/bin/python3
for i in range(99):
   print("{:0>2}".format(i), ", " if i < 99 else "\n")
