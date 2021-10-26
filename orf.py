# Biomedical-DS
#Open Reading Frame
"""
A program that scans through a FASTA file of Human gene sequences. Finds the longest and shortes sequence in the file, then searches through the file for the longest
length of each Open reading frame in each sequence, searching through three different frames for the longest ORF. """

#!/opt/anaconda3/bin/python
import pandas as pd
human_file  = open("human.fa")
dna_file = open("dna.fasta")

seqs = {}
gene_seqs = ''
gene_symbol = ''
for i in dna_file:
        line = i.strip()
        if line[0] == '>':
                l = line.split()
                gene_symbol = l[0][1:]
                seqs[gene_symbol] = ''
        else:
                seqs[gene_symbol]+=line
		#print(gene_symbol,len(seqs[gene_symbol])) 

long_seq = 0
for name,sequence in seqs.items():
	if len(sequence) > long_seq:
		long_seq = len(sequence)
		long_name = name
	else:
		continue

print('%s has the longest sequence of length %d nucleotides'%(long_name,long_seq))

short_seq = long_seq
for name,sequence in seqs.items():
        if len(sequence) < short_seq:
                short_seq = len(sequence)
                short_name = name
        else:
                continue
print('%s has the shortest sequence of length %d nucleotides'%(short_name,short_seq))


stop_codon = ['TAA','TAG','TGA']
for name, sequence in seqs.items():
	frame1_list=[]
	frame2_list=[]
	frame3_list=[]
	orf = 0
	frame1 = 0
	frame2 = 1
	frame3 = 2
	count1 = 0
	count2 = 0
	count3 = 0
	for triplet in sequence[0::3]:
		trip =sequence[frame1:frame1+3]
		frame1_list.append(trip)
		frame1+=1

	orf_count=0
	for triplet in frame1_list:
		if triplet == 'ATG':
			for i in frame1_list[count1:]:
				if i not in stop_codon:
					orf_count+=3
				else:
					if orf_count>orf:
						orf = orf_count+3
						orf_final = str(orf)+ ' Frame 1'
						break
					else:
						break
					break
				
			count1+=1
			break
		else:
			count1+=1
	
	for triplet in sequence[0::3]:
		trip =sequence[frame2:frame2+3]
		frame2_list.append(trip)
		frame2+=1

	orf_count = 0
	for triplet in frame2_list:
		if triplet == 'ATG':
			for i in frame2_list[count2:]:
				if i not in stop_codon:
					orf_count+=3
				else:
					if orf_count>orf:
						orf = orf_count+3
						orf_final = str(orf)+ ' Frame 2'
						break
					else:
						break
					break
				
					
			count2+=1
			break
		else:
			count2+=1
		
	for triplet in sequence[0::3]:
		trip =sequence[frame3:frame3+3]
		frame3_list.append(trip)
		frame3+=1
	orf_count = 0
	for triplet in frame3_list:
		if triplet == 'ATG':
			for i in frame3_list[count3:]:
				if i not in stop_codon:
					orf_count+=3
				else:
					if orf_count>orf:
						orf = orf_count+3
						orf_final = str(orf)+ ' Frame 3'
						break
					else:
						break
					break
				
			count3+=1
			break
		else:
			count3+=1
			
		
	print(name,orf_final)
