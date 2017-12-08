#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  samtoolsconsensus.py
#
#  Copyright 2017 USYD
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0


import sys
import time
import subprocess


class Samtools:

  def __init__(self, path='samtools'):
    self.path = path

  def to_bam(self, mb_ph):
    cmd = [self.path, 'view', '-b']
    ph = subprocess.Popen(cmd, stdin=mb_ph.stdout, stdout=subprocess.PIPE)
    return ph

  def sort_bam(self, bam, outf='out.bam'):
    cmd = [self.path, 'sort', '-o', outf]
    ph = subprocess.Popen(cmd, stdin=bam)
    while ph.poll() is None:
      time.sleep(1)
    return outf

class Bcftools:

    def __init__(self, path='bcftools'):
      self.path = path

    def mpileup(self, ref, sorted_bam):
      cmd = [self.path, 'mpileup', '-Ou', '-f', ref, sorted_bam]
      ph = subprocess.Popen(cmd, stdout=subprocess.PIPE)
      return ph

    def call(self, bcf, outf='out.vcf'):
      cmd = [self.path, 'call', '-vm', '-o', outf]
      ph = subprocess.Popen(cmd, stdin=bcf)
      while ph.poll() is None:
        time.sleep(1)
      return outf

class SamtoolsConsensus:

  def __init__(self):
    self.samtools = Samtools()
    self.bcftools = Bcftools()

  def sam_to_bam(self, sam):
    view = self.samtools.to_bam(sam)
    return self.samtools.sort_bam(view.stdout)

  def make_vcf(self, ref, sorted_bam):
    ph = self.bcftools.mpileup(ref, sorted_bam)
    return self.bcftools.call(ph.stdout)

  def make_consensus(self, ref, vcf):
    fh_ref = open(ref, 'r')
    fh_ref.close()
    fh_vcf = open(vcf, 'r')
    for i in fh_vcf:
      print(i.rstrip())
    fh_vcf.close()
    pass
