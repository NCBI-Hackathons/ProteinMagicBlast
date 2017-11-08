#  request.py
#
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

from . import requester

class NcbiRequest:
  """
  The base class for NCBI requests.
  """
  def __init__(self, resturl, wait=0.33):
    self.contact = None
    self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    self.tool = 'simbiontRequest'
    self.wait = wait
    self.max_retries = 9
    self.batchsize = 0
    self.requests = []
    self.url = self.base_url + '/' + resturl
    self.requester = requester.Requester(self.wait)
    self.expected_batches = 0
    self.expected_uids = 0
    self.total_fetched_uids = 0

  """
    Fetch requests for methods allowing several requests.
  """
  def fetch_requests(self, parser):
    total_fetched_uids = 0
    for i in self.requests:
      self.requester.request(i)
      parser.parse(i)
      #self.total_fetched_uids += parser.fetched_uids

  def prepare_batch(self, batch):
    batch.contact = self.contact
    batch.url =  self.url
    batch.tool = self.tool
    batch.db   = self.db
    batch.typ  = self.rettype
    batch.mode = self.retmode
