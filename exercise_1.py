file = open("input.txt")
output = open("trimmed.txt", "w")
for dna in file:
    trimmed_dna = dna[14:]
    output.write(trimmed_dna)
    print("processed sequence with length " + str(len(trimmed_dna)))

