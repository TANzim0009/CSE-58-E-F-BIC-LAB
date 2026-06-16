def hamming_distance(s1, s2):
  count = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      count += 1 # Corrected indentation
  return count # Corrected indentation and logical placement

def approximate_pattern_matching(pattern, text, d):
  positions = []
  k = len(pattern)

  for i in range(len(text) - k + 1): # Corrected 'lwn' to 'len'
    substring = text[i:i+k]

    if hamming_distance(pattern, substring) <= d:
      positions.append(i)
  return positions # Corrected logical placement

#input
pattern = "ATTCTGGA"
text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
d = 3
result = approximate_pattern_matching(pattern, text, d) # Corrected function name typo
print(*result)
