from tkinter.filedialog import askopenfilename

print("Ce code permet de consolider 3 bases de données sous forme d'un fichier csv. \n le fichier final sera de même sous forme d'un fichier csv, sa forme sera compatible avec la source 2. \n Si la même information se repète entre les 3 sources, celle dans la source 3 est priorisée sur eux, et celle de la source 1 est priorisée sur celle de la source 2")

input('Cliquer sur Entrer pour choisir la source 1')
filename1 = askopenfilename(title = 'choisissez la premiere source' , filetypes = [("Fichiers Excel csv ","*.csv")])


input('Cliquer sur Entrer pour choisir la source 2')
filename2 = askopenfilename(title = 'choisissez la deuxième source' , filetypes = [("Fichiers Excel csv ","*.csv")])


input('Cliquer sur Entrer pour choisir la source 3')
filename3 = askopenfilename(title = 'choisissez la troisième source' , filetypes = [("Fichiers Excel csv ","*.csv")])


print("1 : ",filename1)
print("2 : ",filename2)
print("3 : ",filename3)

input('Exit ? ')
