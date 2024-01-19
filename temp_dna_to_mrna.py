temp_dna_orig=[]
temp_dna_new=[]
temp_dna_three=[]
AA_chain=[]
input_dna=input("Please input the template dna strand without spaces")
temp_dna_orig.extend(input_dna)
for i in temp_dna_orig:
    if i=="C":
        temp_dna_new.extend("G")
    if i=="G":
        temp_dna_new.extend("C")
    if i=="T":
        temp_dna_new.extend("A")
    if i=="A":
        temp_dna_new.extend("U")


temp_dna_three=[temp_dna_new[i:i+3] for i in range(0, len(temp_dna_new), 3)]
for i in temp_dna_three:
    if i==['A','U','G']:
        AA_chain.append("Met")
    if i==['A','U','U'] or i==['A','U','C'] or i==['A','U','A']:
        AA_chain.append("Ile")
    if i==['U','U','U'] or i==['U','U','C']:
        AA_chain.append("Phe")
    if i==['U','U','A'] or i==['U','U','G']:
        AA_chain.append("Leu")
    if i==['U','C','U'] or i==['U','C','C'] or i==['U','C','A'] or i==['U','C','G']:
        AA_chain.append("Ser")
    if i==['U','A','U'] or i==['U','A','C']:
        AA_chain.append("Tyr")
    if i==['U','G','G']:
        AA_chain.append("Trp")
    if i==['U','A','A'] or i==['U','A','G'] or i==['U','G','A']:
        AA_chain.append("Stop")
    if i==['C','U','U'] or i==['C','U','A'] or i==['C','U','C'] or i==['C','U','G']:
        AA_chain.append("Leu")
    elif i in (['C', 'C', 'U'], ['C', 'C', 'C'], ['C', 'C', 'A'], ['C', 'C', 'G']):
        AA_chain.append("Pro")
    elif i in (['C', 'A', 'U'], ['C', 'A', 'C']):
        AA_chain.append("His")
    elif i in (['C', 'A', 'A'], ['C', 'A', 'G']):
        AA_chain.append("Gln")
    elif i in (['C', 'G', 'U'], ['C', 'G', 'C'], ['C', 'G', 'A'], ['C', 'G', 'G']):
        AA_chain.append("Arg")
    elif i in (['A', 'C', 'U'], ['A', 'C', 'C'], ['A', 'C', 'A'], ['A', 'C', 'G']):
        AA_chain.append("Thr")
    elif i in (['A', 'A', 'U'], ['A', 'A', 'C']):
        AA_chain.append("Asn")
    elif i in (['A', 'A', 'A'], ['A', 'A', 'G']):
        AA_chain.append("Lys")
    elif i in (['A', 'G', 'U'], ['A', 'G', 'C']):
        AA_chain.append("Ser")
    elif i in (['G', 'U', 'U'], ['G', 'U', 'C'], ['G', 'U', 'A'], ['G', 'U', 'G']):
        AA_chain.append("Val")
    elif i in (['G', 'C', 'U'], ['G', 'C', 'C'], ['G', 'C', 'A'], ['G', 'C', 'G']):
        AA_chain.append("Ala")
    elif i in (['G', 'A', 'U'], ['G', 'A', 'C']):
        AA_chain.append("Asp")
    elif i in (['G', 'A', 'A'], ['G', 'A', 'G']):
        AA_chain.append("Glu")
    elif i in (['G', 'G', 'U'], ['G', 'G', 'C'], ['G', 'G', 'A'], ['G', 'G', 'G']):
        AA_chain.append("Gly")



print("The amino acid chain is", AA_chain, "The mRNA codons are",temp_dna_three )



    