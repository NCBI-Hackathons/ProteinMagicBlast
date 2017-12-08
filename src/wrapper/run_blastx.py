import subprocess
import os
import time

class RunBlastX:
  def __init__(self, db):
    self.db = db

  def run(self, out_file, query):
    #proc = subprocess.run(['blastx','-query',query_file,'-db',self.db,'-out',out_file,'-outfmt','15'], stdout=subprocess.PIPE )
    cmd = ['blastx','-db',self.db,'-out',out_file,'-outfmt','15']
    print(cmd )
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    proc.stdin.write(query.encode())
    proc.stdin.close()
    while proc.poll() is None:
      time.sleep(1)
    if proc.returncode != 0:
      for i in proc.stdout:
        print(i.decode())
      raise RuntimeError('Failed to run BlastX')
    else:
      print("=> Finished. Results written to {}".format(out_file))
