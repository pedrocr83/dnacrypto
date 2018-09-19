from random import shuffle

def dnacrypto():

    DNA = 'ATGC'
    codons = [(l1+l2+l3) for l1 in DNA for l2 in DNA for l3 in DNA]
    letters = 'ABCÇDEFGHIJKLMNOPQRSTUVYWZabcçdefghijklmnopqrstuvywz1234567890. '
    dicio = [letter for letter in letters]

    shuffle(codons)
    shuffle(dicio)

    cryptodna = dict(zip(codons,dicio))
    return cryptodna


def codify(text, cryptodna):
    
    codedmessage = ''
    codedmessage = [codon for i in text for codon, letter in cryptodna.items() if i == letter]
    codedmessage = ''.join(codedmessage)
    return codedmessage


def uncodify(codedmessage, cryptodna):
    
    uncodedmessage = ''
    messagelist = [codedmessage[i:i+3] for i in range(0,len(codedmessage),3)]
    uncodedmessage = [cryptodna[codon] for i in messagelist for codon in cryptodna.keys() if i == codon]
    uncodedmessage = ''.join(uncodedmessage)
    return uncodedmessage


cypher = dnacrypto()

cmessage = codify(input(),cypher)

message = uncodify(cmessage, cypher)

