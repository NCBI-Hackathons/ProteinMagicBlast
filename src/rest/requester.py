#  eutils.py
#
#  Copyright 2017 USYD
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0


import sys
import time
import urllib.parse
import urllib.request
import urllib.error

class Requester:

  def __init__(self, wait):
    self.wait = wait
    self.max_retries = 9
    self.timeout = 10

  def request(self, batch):
    retries = 0
    success = False
    while success == False:
      wait = self.wait
      try:
        data = urllib.parse.urlencode(batch.prepare_qry(), doseq=True).encode('utf-8')
        request = urllib.request.Request(batch.url, data=data)
        batch.qry_url = data.decode()
        print(batch.url, batch.qry_url, file=sys.stderr)
        batch.response = urllib.request.urlopen(request, timeout=self.timeout)
      except urllib.error.URLError as url_err:
        print("URL error:", url_err.reason, file=sys.stderr)
        wait = 2
      except urllib.error.HTTPError as http_err:
        print("HTTP error:", httperr.code, http_err.reason, file=sys.stderr)
        if retries > self.max_retries:
          batch.request_error = http_err
          print("HTTP error:", http_err.code, http_err.reason, file=sys.stderr)
          #sys.exit("Abort. Retrieving failed after: " + str(retries) + " tries.")
        retries += 1
        wait = 1
      else:
        success = True
      #print("Temporary check. Remove when happy. Sleeping: {0}s".format(wait), file=sys.stderr)
      time.sleep(wait)
