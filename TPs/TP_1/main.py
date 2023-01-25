from a_syntaxique import analyse_syntaxique
from extraction_entites_nommees import extraction_entite_nommee
from morpho_syntaxique import *

# 1. Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK

desambiguiser("./data/wsj_0010_sample.txt", "./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.nltk")
universel("./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.nltk", "./data/wsj_0010_sample.pos.ref", "./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.univ.nltk", "./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.univ.ref" )

# 2. Utilisation de la plateforme NLTK pour l’analyse syntaxique 
# Premiere outpout Q2.1 et la deuxieme output Q2.2 dans le dossier analyse_syntaxique
analyse_syntaxique("./data/wsj_0010_sample.txt", "./resultat/analyse_syntaxique/wsj_0010_sample.txt.chk.nltk", "./resultat/analyse_syntaxique/wsj_0010_sample.txt.chk.generalize.nltk" )

# 3. Utilisation de la plateforme NLTK pour l’extraction d’entités nommées
# Premiere outpout Q3.1 et la deuxieme output Q3.2 dans le dossier entite_nommee
extraction_entite_nommee("./data/wsj_0010_sample.txt", "./resultat/entite_nommee/wsj_0010_sample.txt.ne.nltk" ,"./resultat/entite_nommee/wsj_0010_sample.txt.ne.converted.nltk" )
#Q3.3 pour le fichier formal-tst.NE.key.04oct95_sample.txt
extraction_entite_nommee("./data/formal-tst.NE.key.04oct95_sample.txt", "./resultat/entite_nommee/formal-tst.NE.key.04oct95_sample.txt.ne.nltk" ,"./resultat/entite_nommee/formal-tst.NE.key.04oct95_sample.txt.ne.converted.nltk" )