#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  class2_wrapper.py
#
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

import io
import sys
import subprocess

class Class2:

  def __init__(self, path):
    self.threads = 10
    self.path = path
    self.cmd = [self.path]

  def run(self, samfile):
    self.cmd = self.cmd + ['-p', str(self.threads)]
    p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, universal_newlines=True)
    print(p.args)
    return p.stdout

def main():
  c = Class2('/home/jan/build/class2/CLASS-2.1.7/class')
  out = c.run('out.sam')
  print(io.StringIO(out))
  return 0

if __name__ == '__main__':
  main()
