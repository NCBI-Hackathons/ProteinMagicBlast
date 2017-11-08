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
import argparse

#sys.path.insert(1, os.path.join(sys.path[0], 'eutils'))
from eutils import protmap
from eutils import run_blastx
from magicblast import consens
from magicblast import magicblast


def main():
  ap = argparse.ArgumentParser(description='Supermagicblast')
  ap.add_argument('-srr', nargs='*')
  ap.add_argument('-prot_accs', nargs='*')

  args = ap.parse_args()
  ## fetch mrnas
  eutils = protmap.ProteinLinker()
  eutils.link(args.prot_accs)
  mb = magicblast.Magicblast()
  mb.run(args.srr[0], eutils.mrna_path)
  consens.assemble_transcripts(eutils.mrna_path, 'testrun.fa', 'out.sam')
  bx = run_blastx.RunBlastX(db=eutils.protein_path)
  bx.run(eutils.mrna_path, 'result.out')
  return 0

if __name__ == '__main__':
  main()
