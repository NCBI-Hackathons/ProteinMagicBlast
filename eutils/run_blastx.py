import subprocess
import os

class RunBlastX:
  def __init__(self, db):
    self.db = db

  def run(self, query_file, out_file):
    proc = subprocess.run(['blastx','-query',query_file,'-db',self.db,'-out',out_file,'-outfmt','15'], stdout=subprocess.PIPE )
    if (proc.returncode != 0):
       raise RuntimeError('Failed to run BlastX:\n' + proc.stdout)
