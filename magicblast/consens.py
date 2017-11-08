from pyfaidx import Fasta
import shutil
import pysam
import subprocess
import sys

def get_variations(vcf_stream):
    """Parse a VCF file and get tuple: reference accession, position,
    changed bases"""
    for line in vcf_stream:

        if line.startswith('#'):
            continue

        fields = line.rstrip().split()

        accession = fields[0]
        pos = int(fields[1])
        ref = fields[3]
        alt = fields[4]
        # currently only single nucleotide changes
        if  len(alt) == 1:
            yield (accession, pos, ref, alt)


def get_transcripts(reference_file, transcript_file, vcf_file):
    """Take a FASTA reference file and a VCF file, and generate a FASTA file
    with changes from the vcf file"""
    shutil.copyfile(reference_file, transcript_file)
    transcripts = Fasta(transcript_file, mutable=True)
    with open(vcf_file) as f:
        for (accession, pos, ref, alt) in get_variations(f):
            if accession not in transcripts:
                raise ValueError('VCF accession {0} not found in reference'.\
                                 format(accession))
            transcripts[accession][(pos - 1):pos] = alt

def sam2bam(samfile):
    """Convert SAM to BAM"""
    if samfile.endswith('.sam'):
        outname = samfile[:-4] + '.bam'
    else:
        outname = samfile + '.bam'
    infile = pysam.AlignmentFile(samfile, 'r')
    outfile = pysam.AlignmentFile(outname, 'wb', template=infile)
    for r in infile:
        outfile.write(r)
    infile.close()
    outfile.close()
    return outname

def sortbam(bamfile):
    """Sort a BAM file"""
    if bamfile.endswith('.bam'):
        outfile = bamfile[:-4] + '_sorted.bam'
    else:
        outfile = bamfile + '_sorted.bam'
    pysam.sort('-o', outfile, bamfile)
    return outfile

def call_snps(samfile, reference):
    """Call SNPs using a SAM file and a FASTA reference"""
    # Create faidx index
    s = Fasta(reference)
    bamfile = sam2bam(samfile)
    sorted_bamfile = sortbam(bamfile)
    if samfile.endswith('.sam'):
        vcffile = samfile[:-4] + '.vcf'
    else:
        vcffile = samfile + '.vcf'
    cmd = ['freebayes', '--fasta-reference', reference, sorted_bamfile]
    f = open(vcffile, 'w')
    try:
        subprocess.run(cmd, check=True, stdout=f)
    except:
        print('Problem running freebayes')
        f.close()
        sys.exit(-1)
    f.close()
    return vcffile

def assemble_transcripts(refseqs, outfile, samfile):
    """..."""
    vcffile = call_snps(samfile, refseqs)
    get_transcripts(refseqs, outfile, vcffile)


#if __name__ == '__main__':

    #assemble_transcripts('NC_014372.fa', 'aaa.fa', 'out.sam')
