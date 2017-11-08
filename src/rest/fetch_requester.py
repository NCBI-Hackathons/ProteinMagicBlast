#  fetch_request.py
#
#  Author: Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0

import sys
import math
from . import request
from . import fetch_batch
from . import fetch_request_parser


class NcbiFetchRequester(request.NcbiRequest):

  def __init__(self, email, wait=0.3):
    super().__init__('efetch.fcgi', wait=wait)
    self.tool = 'supermagicFetch'
    self.db = 'sequences'
    self.retmode = 'xml'
    self.rettype = 'fasta'
    self.batch_size = 500
    self.contact = email

  def set_options(self, options):
    self.wait = options.pop('wait', self.wait)
    self.rettype  = options.pop('rettype', self.rettype)
    self.db   = options.pop('db', self.db)
    self.batch_size = options.pop('batch_size', self.batch_size)
    print("Mode: {0} :: Database: {1} :: Batch size: {2} :: Rettype: {3}".format(self.retmode,
           self.db, self.batch_size, self.rettype), file=sys.stderr)

  def request(self, uids, options={}, parser=None):
    self.set_options(options)
    self.expected_uids = len(uids)
    self.expected_batches = math.ceil(self.expected_uids/self.batch_size)
    start = 0
    batch_num = 0
    batch_size = self.batch_size
    for i in range(self.expected_batches):
      if start + batch_size  > self.expected_uids:
        batch_size = self.expected_uids - start
      b = fetch_batch.FetchRequestBatch(batch_num, uids, start, batch_size)
      batch_num += 1
      start += self.batch_size
      self.prepare_batch(b)
      self.requests.append(b)
    self.fetch_requests(parser)
