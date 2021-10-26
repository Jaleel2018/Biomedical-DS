# parse.py
A program written to parse a Human genome Fasta file for gene names, compare them with genes in a database and write them to a new file with the database information.
#!/opt/anaconda3/bin/python
import pandas as pd
human_file  = open("human.fa")
protein_file =  pd.read_table('protein-coding_gene.txt', header = 0)
hw3 = open("hw3.fa",'a')
symbol = list(protein_file['Approved Symbol'][:])
name = list(protein_file['Approved Name'][:])
synonyms = list(protein_file['Synonyms'][:])
location = list(protein_file['Chromosome'][:])

protein_gene = {}
seqs = {}
gene_seqs = ''
gene_symbol = ''
for i in human_file:
	line = i.strip()
	if line[0] == '>': 
		l = line.split()
		gene_symbol = l[0][1:]
		seqs[gene_symbol] = ''
	else:
		seqs[gene_symbol]+=line

for sym,des in seqs.items():	
	if sym in symbol:
		index = symbol.index(sym)
		class gene:
			
			gene_name = name[index]
			gene_synonyms = synonyms[index]
			gene_location = location[index]
		identifier = '>'+str(sym)+'|'+str(gene.gene_name)+'|'+str(gene.gene_synonyms)+'|'+str(gene.gene_location)
		hw3.write(identifier+'\n')
		hw3.write(des[:60]+'\n')
		hw3.write(des[60:120]+'\n')
		hw3.write(des[120:180]+'\n')
		hw3.write(des[180:240]+'\n')
		hw3.write(des[240:300]+'\n')
		hw3.write(des[300:360]+'\n')
		hw3.write(des[360:420]+'\n')
		hw3.write(des[500:560]+'\n')
		hw3.write(des[560:620]+'\n')
		hw3.write(des[620:680]+'\n')
		hw3.write(des[680:740]+'\n')
		hw3.write(des[740:800]+'\n')
		hw3.write(des[800:860]+'\n')
		hw3.write(des[920:980]+'\n')
		
	else:
		identifier = '>'+str(sym)+'|'+'gene symbol not found in file' 
		hw3.write(identifier+'\n')
		hw3.write(des[0:60]+'\n')
		hw3.write(des[60:120]+'\n')
		hw3.write(des[120:180]+'\n')
		hw3.write(des[180:240]+'\n')
		hw3.write(des[240:300]+'\n')
		hw3.write(des[300:360]+'\n')
		hw3.write(des[360:420]+'\n')
		hw3.write(des[500:]+'\n')
human_file.close()
hw3.close()
