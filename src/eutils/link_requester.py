#  link_request.py
#
#  Description:
#  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=nuccore&db=taxonomy&id=%27NC_025895.1%27&id=%27NC_035450.1%27&id=%27NC_031005.1%27&cmd=neighbor&retmode=json
#  Version: 0


import sys
import math
from . import request
from . import link_batch
from . import link_request_parser

class NcbiLinkRequester(request.NcbiRequest):
  def __init__(self, fromdb, db, command='neighbor', useSubsets=False, wait=0.3):
    super().__init__('elink.fcgi', wait=wait)
    self.tool = 'supermagicLinker'
    self.retmode = 'xml'
    self.batch_size = 500
    self.useSubsets = useSubsets
    self.fromdb = fromdb
    self.db = db
    self.command = command

  def set_options(self, options):
    print("Mode: {0} :: Batch size: {1} :: Use subsets {2}".format(self.retmode,
          self.batch_size, self.useSubsets), file=sys.stderr)

  def request(self, uids, options={}, parser=link_request_parser.NcbiLinkRequestParser()):
    self.set_options(options)
    self.expected_uids = len(uids)
    self.expected_batches = math.ceil(self.expected_uids/self.batch_size)
    start = 0
    batch_num = 0
    batch_size = self.batch_size
    for i in range(self.expected_batches):
      if start + batch_size  > self.expected_uids:
        batch_size = self.expected_uids - start
      b = link_batch.NcbiLinkBatch(batch_num, uids, self.fromdb, self.db, start, batch_size, self.command, useSubsets=self.useSubsets)
      batch_num += 1
      start += self.batch_size
      self.prepare_batch(b)
      self.requests.append(b)
    self.fetch_requests(parser)

  def prepare_batch(self, batch):
    batch.contact = self.contact
    batch.url =  self.url
    batch.tool = self.tool
    batch.mode = self.retmode
