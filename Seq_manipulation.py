# Biomedical-DS
# Gene Sequence Manipulation
""" 
This Program takes a given sequence, finds the length of that sequence, seperates the sequence into a list of triplets, then finds the frequency of each triplet.
This frequency count is added as the value for each triplet in the trip_dict dictionary.
"""
#!/usr/bin/python

sequence = "ATTGGGGAGGAGGCGAGTTGAGCGGCGGCAGTTCGCCTGCGTGCGCTGCGCGGCGTCGACATCTGATCCGCACCATGGAAATCCCCGCTCAATCTTTGGAGCAGGGATGCGGGGCGATCAAGATGGGGATGCGGGATGGGGGCGACGGTGTATTTCCGCCAGAAGATTTCGCCGCGGGAGCTCGCGGTGCGTACGTGCATGTTCAAACGCACGGTGCGCGCATGGCAGTGGCAGACTGATCAACGCAGCTGGAAGCATCCGAAGCGCGCGGGCACGCGTGTCCTCGACGCGTGGCCTCACATGCTGTCGGGTCGGTTCAAGACCGAAAGCCACCGACCGACGCGCGAGCAATGCGCTACGCGGATCGCGTTCGACACGAGCCGCGCGCGAGGCAAGGCCGACGTATTCGATCTTCCAGAGGAAGCCTATTGGCTCGAGTCGTAGTGCTCGATATGGTAGAGCAACATGAATCCCGGGCTAAGTACAAGAAGTAACCCGGCAACGAGTGAGATTGCGACGAATAAACGCTTCACCATGATCGCGCTCCTGAGTTGGTTGAGGTGAATTGGAAAGTCGATTCCTGGGGGATCATTCCCGGCAAGGCGCGCAATCCCCGCATTGTTCTCAAGATCGCAACGCGATTCGTCAGGCCGATCTTCATGGGGTGTCTCGCTGGTAGTGATTCCGTCGTGGCCCGCGCATGTGCATGACGGCATCCGGGGAG"
print("1. The Length of the sequence is %i" %len(sequence))

count = 0
trip_dict = {}
trip_list = []
def question_2(seq):
	count = 0
	for i in sequence[0::3]:
		trip = seq[count:count+3]
		trip_list.append(trip)
		count+=1
	#print("this is : %s " % trip_list)
	for triplet in trip_list:
		if triplet not in trip_dict:
			trip_dict[triplet] = trip_list.count(triplet)
		else:
			continue
	return trip_dict

complement = []

def question_3(seq):
	for nucleotide in sequence:
		if nucleotide =='A':
			complement.append('T')
		elif nucleotide == 'G':
			complement.append('C')
		elif nucleotide == 'T':
			complement.append('A')
		else:
			complement.append('G')
	return complement

print("2. The count of each triplet is %s" %question_2(sequence))
print("3. The Complement of the given sequence is %s" %question_3(sequence))	
