from Bio import SeqIO
ip = open("test.fasta","rU")

rnase_ind = []
import re
for record in SeqIO.parse(ip,"fasta"):
	regex = r'GAGGAA[ACGT]{2}TC[ACGT]{4}C[ACGT]{0,600}AG[ACGT]{4}AT[ACGT]{10,60}ACA[ACGT]AA[ACGT]{4}G[ACGT]{2}TA'
	m = re.finditer(regex,str(record.seq))
	for match in m:	
		print record.id,':',int(match.start()+1),int(match.end()+1)
ip.close()

