'''
1)	Figure out what each read contains:
    a.	Find the 5’ promoter region
        i.	Check to see if it’s in the reverse compliment
    b.	Find the 5’ barcode+promoter region and the 3’ constant region + 3’ barcode
        i.	This assigns the read to a pool
            1.	If no promoter, the pool is ‘no prom’
            2.	If no barcode matches, the pool is ‘no barc’
    c.	Translate the read from the start methionine through the end of the read
        i.	If the first codon is not a met, check other reading frames for the longest read that starts with a met


2)	Store the info
    a.	Count how many times a protein seq has shown up in a pool
    b.	Count how many times a dna seq has shown up in a pool (and store what that translates to as well)
'''




extract_reads()

for each read 

    reorient the read 
    translate the read into protein
    in one dataframe, assign the protein to the matching pools
    in another dataframe, assign the DNA to the matching pools 

assign_each_read_to_matching_pools_or_update_count()


