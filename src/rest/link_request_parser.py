#  link_request_parser.py
#
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

import io

class NcbiLinkRequestParser:

  def __init__(self):
    pass

  def parse(self, request):
    print(request.url, request.qry_url)
    print(request.ids)
    response = io.StringIO(request.response.read().decode())
    for i in response:
      print(i.rstrip())
