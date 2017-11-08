import subprocess
import os

class MakeBlastDB:
  def __init__(self, fasta_path, title, session_path):
    self.fasta_path = fasta_path
    self.title = title
    self.session_path = session_path

  def make(self):
    cwd = os.getcwd()
    os.chdir(self.session_path)
    proc = subprocess.run(['makeblastdb', '-dbtype','prot', '-in', self.fasta_path, '-input_type', 'fasta', '-title', self.title ], stdout=subprocess.PIPE )
    if (proc.returncode != 0):
       raise RuntimeError('Failed to generate BlastDB:\n' + proc.stdout)
    os.chdir(cwd)
