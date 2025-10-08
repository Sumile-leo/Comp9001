import re

def splice_rna(rna):
    return re.sub(r'GUGU.*?AGAG', '', rna)


strand = input("Input strand: ")
print()
if strand == '':
    print("No strand provided.")
else:
    print(f"Output is {splice_rna(strand)}")