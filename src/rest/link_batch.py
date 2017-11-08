#  link_batch.py
#
#  Copyright 2017 The University of Sydney
#  Author: Jan P Buchmann <jan.buchmann@sydney.edu.au>

import sys
from . import request_batch

class NcbiLinkBatch(request_batch.RequestBatch):

  def __init__(self, batch_id, ids, dbfrom, db, start, size, command, useSubsets=False):
    super().__init__()
    self.id = 0
    self.ids = ids[start:start+size]
    self.dbfrom = dbfrom
    self.db = db
    self.retmode = 'xml'
    self.size = size
    self.name = "{0}_{1}_".format(self.dbfrom, self.db)
    self.useSubsets = useSubsets
    self.usehistory = False
    self.command = command

  def prepare_qry(self):
    req = {
            'email'   : self.contact,
            'tool'    : self.tool,
            'db'      : self.db,
            'dbfrom'  : self.dbfrom,
            'retmode' : self.mode,
            #'linkname' : self.name,protein_nuccore_mrna
            'linkname' : 'protein_nuccore_mrna',
            'cmd' :   self.command,
            'usehistory' : self.usehistory
          }
    if self.useSubsets == True:
      req['id'] = self.ids
    else:
      req['id'] = ','.join(x for x in self.ids)
    return req
