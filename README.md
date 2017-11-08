# ProteinMagicBlast
![Workflow](/bc073254-b7d4-4648-912f-a346c63b585f.png?raw=true "logo.png")

## Pitch
Biologists are interested in studying variation on a protein level. Does a mutation change an amino acid in a protein. Does the changed protein have the same function? ProteinMagicBlast answers these questions. All it needs is a list of SRA accessions and Refseq proteins. It reports differences between sequenced mRNAs and provided proteins.

## Introduction
The purpose of this approach is to provide answers to questions raised by scientific community
in regard to changes in the protein sequences when compared with SRA data using Magic Blast 
tool and supporting software. The main question answered is given the genomic sequences if it
has sequences related with a given protein and also if any changes in protein has occurred. 
The software will provide the protein alignments and changes in amino acids will be displayed on the viewer.  

## What's the problem? 
ProteinMagicBlast solves the problem of user when finding relationship of given sequence 
data with interested proteins. User wants to know if in the new genome(sequences) are interested 
protein sequences be found? if yes, are there any significant changes related with interested protein? 
Has the amino acid changed at any of the positions?  

## Why should we solve it? 
Amino acid point mutations (nsSNPs) may change protein structure and function. 
The second approach lets us identify the changes and the magnitude may vary depending on how similar or dissimilar
the replaced amino acids are, as well as on their position in the sequence or the structure.  
   
# What is <this software>?

Overview Diagram
![Workflow](/MAGICBLAST-flow.jpg?raw=true "MAGICBLAST-flow.jpg")

# How to use <this software>
In the simplest form ProteinMagicBlast requires only two inputs: PROTEIN Accession and SRR Accession.
For Example:

```
python webui/manage.py run server
```

``` supermagicblast.py -prot_accs NP_066251.1  -srr SRR5150787 ```

 The output is standard blastx output in json format.
    
## Installation options:

We provide two options for installing ProteinMagicBlast: Docker or directly from Github.

### Docker

The Docker image contains ProteinMagicBlast as well as a webserver and FTP server in case you want to deploy the FTP server. It does also contain a web server for testing the <this software> main website (but should only be used for debug purposes).

1. `docker pull ncbihackathons/<this software>` command to pull the image from the DockerHub
2. `docker run ncbihackathons/<this software>` Run the docker image from the master shell script
3. Edit the configuration files as below

### Installing ProteinMagicBlast from Github
Clone github repository:

 `git clone https://github.com/NCBI-Hackathons/ProteinMagicBlast.git`

Install dependencies:

[Magic-BLAST](https://ncbi.github.io/magicblast)

[BLAST+](https://blast.ncbi.nlm.nih.gov)

[freebayes](https://github.com/ekg/freebayes)

Python packages from requirements.txt file:

`pip install -r requirements.txt`
 
 ## Project Team:

1. Grzegorz M Boratyn
2. Monika Bihan
3. Karina Zile
4. Yevhen I Krasichkov
5. Vladislav I Evgeniev
6. Jan Piotr Buchmann

## Future Development Plans

1. Expand it use on annotated whole genome sequences. 
2. Extending it to large protein databases.
3. Expand it to take more than one SRR or Refseq accession input
4. Improve the speed of the analysis, especially the assembly of the consensus sequence. 

https://youtu.be/mk0GjJ8v-7A 
  
