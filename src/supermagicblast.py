#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  supermagicblast.py
#
#  Copyright 2017 USYD
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

import os
import sys
import json
import time
from shutil import copyfile
import argparse

from eutils import supermagicblast_eutils
from wrapper import run_blastx
from wrapper import magicblast
from consensus import consensus

def writeStatus(status):
  with open(statusFilePath, 'w') as outfile:
    json.dump(status, outfile)

def main(args):
  ### fetch mrnas
  try:
    sleepTime = 1
    writeStatus({'progress': 0, 'status': 'Starting..', 'finished': False })
    writeStatus({'progress': 1, 'status': 'Doing prepping sequences..', 'finished': False })
    eutils = supermagicblast_eutils.SupermagicblastEUtils(args.email)
    eutils.link(args.prot_accs)
    writeStatus({'progress': 33, 'status': 'Running magicblast..', 'finished': False })
    mb = magicblast.Magicblast()
    mapping = mb.run(args.srr[0], eutils.mrna_path)
    writeStatus({'progress': 60, 'status': 'Creating consensus..', 'finished': False })
    c = consensus.Consenter()
    c.add_ref(eutils.mrna_path)
    c.parse(mapping)
    writeStatus({'progress': 66, 'status': 'Creating alignments..', 'finished': False })
    bx = run_blastx.RunBlastX(db=eutils.protein_path)
    bx.run('result.out', c.make_consensus())
    writeStatus({'progress': 100, 'status': 'Finished..', 'finished': True })

    scriptPath = os.path.dirname(os.path.realpath(__file__))
    sampleOutputPath = os.path.join(scriptPath,  args.output)

  except Exception as e:
    writeStatus({'progress': 100, 'status': 'Error', 'finished': True, 'error': True})
    raise e
  return 0

try:
  if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Supermagicblast')
    ap.add_argument('-srr', nargs='*')
    ap.add_argument('-prot_accs', nargs='*')
    ap.add_argument('-statuspath', type=str, default='smb_status.json')
    ap.add_argument('-output', type=str, default='result.asn1')
    ap.add_argument('-email', type=str, required=True)
    args = ap.parse_args()
    statusFilePath = args.statuspath
    main(args)

except Exception as e:
  writeStatus({ 'progress': 100, 'status': 'Error', 'finished': True, 'error': True })
  raise e
