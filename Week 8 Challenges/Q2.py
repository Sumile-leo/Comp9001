def dna(strand):
    mapping = {'A': 'T',
               'T': 'A',
               'G': 'C',
               'C': 'G',
               'a': 't',
               't': 'a',
               'g': 'c',
               'c': 'g'}
    return ''.join(mapping.get(b, 'x') for b in strand)

strand = input("Enter strand: ")
print()
if strand == '':
    print("No strand provided.")
else:
    complementary = dna(strand)
    print(f"Complementary strand is {dna(strand)}")
