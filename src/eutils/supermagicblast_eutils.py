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


import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../'))
from rest import link_requester
from rest import fetch_requester
from . import fetch_mrna_ids


from wrapper import make_blast_db #  import MakeBlastDB
import os, base64, shutil


class SupermagicblastEUtils:

  def __init__(self, email):
    self.email = email
    self.session_id = base64.b64encode(os.urandom(16)).decode("utf-8")
    self.path = os.path.join('/tmp', self.session_id)
    self.protein_path = os.path.join(self.path , 'proteins.fa')
    self.mrna_path = os.path.join(self.path , 'mrnas.fa')
    print(self.path)
    os.mkdir(self.path)

  def link(self, accs_list, dbfrom='protein', dbto='nuccore'):
    lr = link_requester.NcbiLinkRequester(dbfrom, dbto, self.email)
    p = fetch_mrna_ids.EUtilsParser(self.email)
    lr.request(accs_list, p)
    p.WriteMrnasFasta(self.mrna_path)
    p.WriteProteinsFasta(self.protein_path)
    makeblastdb = make_blast_db.MakeBlastDB(self.protein_path,self.session_id,self.path)
    makeblastdb.make()

  def release(self):
    shutil.rmtree(self.path)
