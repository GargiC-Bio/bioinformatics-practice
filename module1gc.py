#This is my first Python program
# get DNA sequence:
dna=input("Enter a DNA sequence, please:") 
no_c = dna.count('c') # count C's in DNA sequence
no_g = dna.count('g') # count G's in DNA sequence
dna_length = len(dna) # get the length of the DNA sequence 
gc_percent = (no_c+no_g)*100/dna_length # compute GC percentage
print("The DNA sequence's GC content is %5.4f%%:"%gc_percent) # print GC% to screen
