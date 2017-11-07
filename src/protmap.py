#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  protmap.py
#
#  Copyright 2017 USYD
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

from eutils import link_requester
from eutils import fetch_requester

import sys
import argparse

class ProteinLinker:

  def __init__(self):
    pass

  def link(self, accs_list, dbfrom, dbto):
    lr = link_requester.NcbiLinkRequester(dbfrom, dbto)
    lr.request(accs_list)

class NucleotideFetcher:

  def __init__(self):
    pass

  def fetch(self, accs_list, db):
    fr = fetch_requester.NcbiFetchRequester()
    fr.request(accs_list, options={'db':'nuccore'})

def main():
  p = ProteinLinker()
  p.link(['XP_009311342', 'XP_006961367.1'], 'protein','nuccore')
  nf = NucleotideFetcher()
  nf.fetch(['686637792','589098688'], 'nuccore')
  return 0

if __name__ == '__main__':
  main()
