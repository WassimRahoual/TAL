import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

def extraction_entite_nommee(input, output, output_converted):
    # Charger le fichier wsj_0010_sample.txt
    with open(input, "r") as f:
        text = f.read()

    # Tokenizer le texte et assigner les étiquettes de partie de discours
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    # Extraire les entités nommées
    named_entities = ne_chunk(pos_tags)

    # Écrire les entités nommées dans un fichier
    with open(output, "w") as f:
        for chunk in named_entities:
            if hasattr(chunk, 'label'):
                f.write(chunk.label() + ": " + " ".join([i[0] for i in chunk]) + "\n")


    # ------ Question 3.2 --------
    # Initialiser une liste pour stocker les étiquettes converties
    my_dict = {"ORGANIZATION": "ORG", "PERSON": "PERS", "LOCATION": "LOC", "DATE": "MISC", "TIME": "MISC", "MONEY": "MISC", "PERCENT": "MISC", "FACILITY": "ORG", "GPE": "LOC"}

    # Enregistrer les étiquettes converties dans un fichier
    with open(output_converted, "w") as f:
        for chunk in named_entities:
            if hasattr(chunk, 'label'):
                f.write(my_dict[chunk.label()] + ": " + " ".join([i[0] for i in chunk]) + "\n")