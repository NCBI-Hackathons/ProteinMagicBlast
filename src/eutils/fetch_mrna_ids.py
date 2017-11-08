import os
import sys
import xml.etree.ElementTree as ET
from collections import namedtuple
sys.path.insert(1, os.path.join(sys.path[0], '../'))
from rest import fetch_requester

Mrna = namedtuple('Mrna', ['gi', 'accession', 'sequence', 'prot_gi'])
Protein = namedtuple('Protein', ['gi', 'accession', 'sequence', 'mrna_gi'])

class EUtilsMrnaParser:

  def __init__(self, mrna_to_prot, mrnas):
    self.mrnas = mrnas
    self.mrna_to_prot = mrna_to_prot

  def parse(self, request):
    xmlstr = request.response.read().decode()
    xml = ET.fromstring(xmlstr)
    for seq in xml.findall('.//TSeq'):
      gi = seq.find('TSeq_gi').text
      accver = seq.find('TSeq_accver').text
      sequence = seq.find('TSeq_sequence').text
      self.mrnas.append(Mrna(gi, accver, sequence, self.mrna_to_prot[gi]))

class EUtilsProteinParser:

  def __init__(self, prot_to_mrna, proteins):
    self.proteins = proteins
    self.prot_to_mrna = prot_to_mrna

  def parse(self, request):
    xmlstr = request.response.read().decode()
    xml = ET.fromstring(xmlstr)
    for seq in xml.findall('.//TSeq'):
      gi = seq.find('TSeq_gi').text
      accver = seq.find('TSeq_accver').text
      sequence = seq.find('TSeq_sequence').text
      self.proteins.append(Protein(gi, accver, sequence, self.prot_to_mrna[gi]))

class EUtilsParser:
  def __init__(self, email):
    self.prot_to_mrna = dict()
    self.mrna_to_prot = dict()
    self.proteins = []
    self.mrnas = []
    self.email = email

  def parse(self, request):
    xmlstr = request.response.read().decode()
    xml = ET.fromstring(xmlstr)
    mrnas_list = []
    protein_ids = xml.findall('.//LinkSet/IdList/Id')
    mrna_ids = xml.findall('.//LinkSet/LinkSetDb/Link/Id')
    i = 0
    mrnas_list = []
    while i<len(protein_ids):
      self.prot_to_mrna[protein_ids[i].text] = mrna_ids[i].text
      self.mrna_to_prot[mrna_ids[i].text] = protein_ids[i].text
      mrnas_list.append(mrna_ids[i].text)
      #self.proteins.append(Protein(protein_ids[i].text, request.ids[i], mrna_ids[i].text))
      i = i+1
    mrna_nf = fetch_requester.NcbiFetchRequester(self.email)
    mrna_nf.request(mrnas_list, options={'db' : 'nuccore'}, parser=EUtilsMrnaParser(self.mrna_to_prot, self.mrnas))
    prot_nf = fetch_requester.NcbiFetchRequester(self.email)
    prot_nf.request(request.ids, options={'db' : 'protein'}, parser=EUtilsProteinParser(self.prot_to_mrna, self.proteins))
    #return mrnas_list



  def WriteMrnasFasta(self, path):
    f = open(path, 'w')
    for mrna in self.mrnas:
      seq = mrna.sequence
      chunks, chunk_size = len(seq), 80
      f.write('>'+mrna.accession+'\n')
      for line in [ seq[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]:
        f.write(line+'\n')
    f.close()

  def WriteProteinsFasta(self, path):
    f = open(path, 'w')
    for protein in self.proteins:
      seq = protein.sequence
      chunks, chunk_size = len(seq), 80
      f.write('>'+protein.accession+'\n')
      for line in [ seq[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]:
        f.write(line+'\n')
    f.close()

  def GetProteinsList(self):
    return self.proteins

  def GetMrnasList(self):
    return self.mrnas

  def GetMrna(self, mrna_id):
    for mrna in self.mrnas:
      if mrna.gi == mrna_id:
        return mrna
    return None

  def GetMrnaByProtId(self, prot_id):
    return self.GetMrna(self.prot_to_mrna[prot_id])


#accs = ['XP_009311342', 'NP_666218.2']
#mydoc = ElementTree(file='tst.xml')
#eutils = EUtilsParser(accs)
#prot_list = eutils.ParseIds(mydoc)
#print(prot_list)

#mydoc2 = ElementTree(file='sequence.fasta-1.xml')
#mrnas = eutils.ParseMrnaSeqs(mydoc2)
#print(mrnas)
#eutils.WriteMrnasFasta('test.fa')
