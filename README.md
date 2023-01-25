TP1 - TAL
===============================================================
Wassim RAHOUAL & Adrien FORT 
===============================================================
ET5 INFO 
===============================================================
25/01/2023


Une fonction main est à disposition pour lancer tout les fichiers demander en resultat.

Commande : python main.py 

Chaque resultats pour chacune des parties :
--------------------------------------
	* PARTIE 1 : ./resultat/morpho_syntaxique
	* PARTIE 2 : ./resultat/analyse_syntaxique
	* PARTIE 3 : ./resultat/entite_nommee

Les scripts pour chacunes des parties :
--------------------------------------
	* PARTIE 1 : morpho_syntaxique.py
	* PARTIE 2 : a_syntaxique.py
	* PARTIE 3 : extraction_entites_nommees.py

# I) Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK 

### Q1.1

Ligne de commande :
python evaluate.py ./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.nltk ./data/wsj_0010_sample.pos.ref

Résultat de la fonction evaluate.py : 
--------------------------------------
 * Word precision: 0.9363636363636364
 * Word recall: 0.9363636363636364
 * Tag precision: 0.9363636363636364
 * Tag recall: 0.9363636363636364
 * Word F-measure: 0.9363636363636364
 * Tag F-measure: 0.9363636363636364

### Q1.2

Ligne de commande :

python evaluate.py ./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.univ.nltk ./resultat/morpho_syntaxique/wsj_0010_sample.txt.pos.univ.ref

Résultat de la fonction evaluate.py
-------------------------------------
* Word precision: 0.9545454545454546
* Word recall: 0.9545454545454546
* Tag precision: 0.9545454545454546
* Tag recall: 0.9545454545454546
* Word F-measure: 0.9545454545454546
* Tag F-measure: 0.9545454545454546

### Q1.3

La conclusion que l'on peut tirer de ces deux évaluations est que l'analyseur morpho-syntaxique de la plateforme NLTK se débrouille bien, avec une précision relativement élevée d'environ 93% 
lorsqu'il est évalué à l'aide des étiquettes Penn TreeBank (PTB) et d'environ 95% lorsqu'il est évalué à l'aide des étiquettes universelles. Cependant, il est important de noter que ces résultats 
sont basés sur un seul fichier d'échantillon, et les performances de l'analyseur peuvent varier en fonction du texte spécifique et de l'utilisation souhaitée.

Il est également important de noter que les performances de l'analyseur peuvent être améliorées en ajustant le modèle ou en utilisant une autre bibliothèque ou un autre modèle d'analyse morpho-syntaxique. 
En outre, le choix de l'ensemble d'étiquettes (PTB ou universel) peut également affecter les performances de l'analyseur, car certains modèles sont entraînés sur des ensembles d'étiquettes spécifiques 
et peuvent fonctionner mieux avec cet ensemble particulier.

Enfin, il est important de prendre en compte l'utilisation spécifique et l'impact des performances de l'analyseur sur les performances globales du système. 
Une précision plus faible peut être acceptable dans certains cas, tandis que dans d'autres cas une précision plus élevée est requise.

# II) Utilisation de la plateforme NLTK pour l’analyse syntaxique

### Q2.1
Voir a_syntaxique.py
Resultat :
---------------------------------------------------------------------------------------------------
	* wsj_0010_sample.txt.chk.nltk

### Q2.2
Pour généraliser le programme Python précédent pour extraire les mots composés (chunks),
nous avons crée un fichier  ./data/compound_word_grammar.cfg dans lequel on déclare les différentes structures syntaxiques.

Adjectif-Nom 
Nom-Nom 
Adjectif-Nom-Nom 
Adjectif-Adjectif-Nom

Resultat :
---------------------------------------------------------------------------------------------------
	* wsj_0010_sample.txt.generalize.nltk

## II) Utilisation de la plateforme NLTK pour l’extraction d’entités nommées

### Q3.1
Voir extraction_entites_nommees.py
Resultat :
---------------------------------------------------------------------------------------------------
	* wsj_0010_sample.txt.ne.nltk

### Q3.2
Nous avons pas bien compris s'il faut transformer par B-ORG ou seulement par ORG le tag initiale ORGANISATION. Nous avons donc effectuer suelement la deuxieme option.
Voir extraction_entites_nommees.py
Resultat :
---------------------------------------------------------------------------------------------------
	* wsj_0010_sample.txt.ne.converted.nltk

### Q3.3
Les résultats sont présent dans le dossier ./resultat/morpho_syntaxique

* formal-tst.NE.key.04oct95_sample.txt.ne.nltk => Fichier initiale
* formal-tst.NE.key.04oct95_sample.txt.ne.converted.nltk => Fichier convertis
