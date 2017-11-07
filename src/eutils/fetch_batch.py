#  fetch_batch.py
#
#  Author: Jan P Buchmann <jan.buchmann@sydney.edu.au>

from . import request_batch

class FetchRequestBatch(request_batch.RequestBatch):

  def __init__(self, batch_id, uids, start, size):
    super().__init__()
    self.id = batch_id
    self.uids = ','.join(x for x in uids[start:start+size])
    self.size = size

  def prepare_qry(self):
    return {
              'email'   : self.contact,
              'tool'    : self.tool,
              'db'      : self.db,
              'rettype' : self.typ,
              'retmode' : self.mode,
              'id'      : self.uids
            }
