#  magicblast.py
#
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

import os
import sys
import subprocess

sys.path.insert(1, os.path.join(sys.path[0], '../../'))


class Magicblast:

  def __init__(self, path='magicblast'):
    self.path = path
    self.num_threads = 10
    self.outfmt = 'sam'
    self.out = 'out.sam'
    self.word_size = 20
    self.perc_identity = 60

  def run(self, srr, subject):
    cmd = [self.path, '-subject',  subject,
                      '-sra', srr,
                      '-num_threads', str(self.num_threads),
                      '-outfmt', self.outfmt,
                      '-out', self.out]
    print(cmd)
    subprocess.call(cmd)
