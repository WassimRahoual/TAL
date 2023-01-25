from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import re

def desambiguiser(input, output) : 
    # read in the text from the file
    with open(input, "r") as file:
        text = file.read()

    # tokenize the text
    tokens = word_tokenize(text)

    # perform POS tagging
    tagged_tokens = pos_tag(tokens)

    # write the result to a new file
    with open(output, "w") as file:
        for token, tag in tagged_tokens:
            file.write(token + "\t" + tag + "\n")

def universel(input1, input2, output1, output2):
   correspondences = {}
   # Charge les correspondances PTB <-> Universal
   with open('./data/POSTags_PTB_Universal_Linux.txt', 'r') as f:
        for line in f:
            ptb_tag, universal_tag = line.strip().split()
            correspondences[ptb_tag] = universal_tag
            
   # Ouvre les fichiers d'entrée et de sortie
   with open(input1, 'r') as infile, open(output1, 'w') as outfile:
   # Pour chaque ligne de l'entrée
        for line in infile:
            # Sépare le token et la référence PTB
            token, ptb_ref = line.strip().split("\t")
            # Calcule la référence Universal correspondante
            universal_ref = correspondences[ptb_ref]
            # Écrit la ligne de sortie
            outfile.write(f"{token}\t{universal_ref}\n")
    
    # Ouvre les fichiers d'entrée et de sortie
   with open(input2, 'r') as infile, open(output2, 'w') as outfile:
   # Pour chaque ligne de l'entrée
        for line in infile:
            # Sépare le token et la référence PTB
            token, ptb_ref = line.strip().split("\t")
            # Calcule la référence Universal correspondante
            universal_ref = correspondences[ptb_ref]
            # Écrit la ligne de sortie
            outfile.write(f"{token}\t{universal_ref}\n")