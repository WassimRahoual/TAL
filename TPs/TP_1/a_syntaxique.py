import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser


def analyse_syntaxique(input, output, output_generalize):
    # Charger le fichier wsj_0010_sample.txt
    with open(input) as f:
        text = f.read()

    # Tokenizer le texte et assigner les étiquettes de partie de discours
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)


    #---------------- QUESTION 2.1 -----------------------
    # Définir la grammaire pour extraire les mots composés
    grammar = "Compound: {<DT>?<JJ>*<NN>}"
    chunk_parser = RegexpParser(grammar)

    # Extraire les mots composés
    compound_words = chunk_parser.parse(pos_tags)

    # Enregistrer les résultats dans le fichier wsj_0010_sample.txt.chk.nltk
    with open(output, "w") as f:
        f.write(str(compound_words))

    #---------------- QUESTION 2.2 -----------------------
    # Charger la grammaire déclarative à partir d'un fichier
    with open("./data/compound_word_grammar.cfg", "r") as f:
        grammar_generalize = f.read()

    chunk_parser_generalize = RegexpParser(grammar_generalize)

    # Extraire les mots composés
    compound_words_generalize = chunk_parser_generalize.parse(pos_tags)

    # Enregistrer les résultats dans le fichier wsj_0010_sample.txt.chk.nltk
    with open(output_generalize, "w") as f:
        f.write(str(compound_words_generalize))


