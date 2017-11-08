#  request_batch.py
#
#  Author: Jan P Buchmann <jan.buchmann@sydney.edu.au>

class RequestBatch:

  def __init__(self):
    self.id = 0
    self.qry_url = ''
    self.tool = ''
    self.db = ''
    self.retmode = ''
    self.rettype = ''
    self.contact = ''
    self.request_error = ''
    self.response = ''
    self.size = 0

  def prepare_qry(self):
    return {
              'email'   : self.contact,
              'tool'    : self.tool,
              'db'      : self.db,
              'rettype' : self.rettype,
              'retmode' : self.retmode,
            }
