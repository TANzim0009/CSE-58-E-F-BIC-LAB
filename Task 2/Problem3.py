DNA = "AAAACCCGGT"
complement = ({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})
revers_complement = ' '.join(complement[nuc] for nuc in reversed(DNA))
print(revers_complement)
