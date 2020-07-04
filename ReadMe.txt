1.	Explication du code :
Ce code prend en paramètre trois base de données sous forme de fichiers Excel (.csv). Il permet de consolider ces trois bases en une finale sous forme d’un fichier Excel. Le code contient un dictionnaire prédéfini mettant en relation les noms des colonnes des BDs contenant les mêmes informations. Par exemple, l’adresse en source_1 est nommé ‘Rue’, alors que dans la source_2 la même information est enregistrée sous le nom ‘adresse’. Ensuite, le code change les noms des colonnes de la source_1, qui se répète dans la source_2(stocké dans la liste D ?_ ?), afin qu’ils soient compatibles avec la fonction DataFrame.update(). Les colonnes qui restent sont stocké sont stocké dans les listes R?. On cherche aussi les relations qui peuvent exister entre les R?  Dès que le code applique cette démarche sur toutes les sources disponibles en respectant leurs priorité (le dernier traité est le prioritaire).
2.	Exécution du code :
Il suffit de chercher le fichier test_ff_ai.py et le lancer. Le code contient une interface qui vous guidera à choisir vos fichiers et l’emplacement de l’enregistrement du résultat. Il faut noter que j’assume que certaines bibliothèques Python sont déjà installées (pandas, numpy, tkinter)
Si vous avez un problème avec la Biblio Tkinter, vous pouvez exécuter le fichier test_ff_si.py sans interface, mais vous deverez changer le path dans la ligne 10, pour qu'il soit convenable à l'emplacement des fichiers source_i.csv.
3.	Commentaires sur mon code :
Je n’ai pas arrivé à ajouter une colonne présentant la source de l’information, car la consolidation était faite en utilisant des fonctions prédéfinies. L’ajout de cette colonne demandera une consolidation codée manuellement, afin que je puisse personnaliser les colonnes.
Vu que ce code n’est qu’une version Beta, il peut y avoir des problèmes soit au niveau de l’exécution et même de niveau de calcul. J’ai essayé de l’exécuter le plus de fois possibles pour trouver ses failles.
4.	Combien de temps :
Honnêtement, j’ai été un peu occupé cette semaine par des projets pédagogiques, alors je n’ai pas au beaucoup de temps pour coder.
J’ai commencé par une 1h30 d’importation des fichiers et les explorer. Au premier temps, J’ai eu quelques erreurs concernant le choix de l’« encoding » et le « delimiter » convenables.
Ensuite j’ai consacré entre deux et trois heures pour coder chaque jour dès le Jeudi, ce qui donne en totale 10 heures. Ensuite, l’interface m’a pris moins de deux heures. 
5.	Ce que je peux ajouter :
J’ai trouvé une méthode de String matching (Levenshtein), qui peut automatiser la généralisation des dictionnaires mettant en relation les colonnes de différents fichiers contenant les mêmes informations.
De plus, j’ajouterai la colonne de la source de l’information, qui prendra un peu de temps pour la coder.
