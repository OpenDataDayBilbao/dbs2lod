import sqlite3


file1 = open('Contratos_sexo_y_edad.csv','r')
edades = file1.readline().split('\t')
con = sqlite3.connect('contratos_sexo_edad.db')
con.text_factory = str
cursor = con.cursor()
temp = []
for i in range(1,10):
    if i%2 == 1:
        temp.append(edades[i])
edades = temp
num_linea = 0
for line in file1.readlines():
    dataline=1
    print line
    num_linea += 1
    if num_linea > 1:
        data = line.split('\t')
        entrada = ["","","",""]
        entrada[0] = str(data[0])
        for edad in edades:
            entrada[1] = str(edad)
            entrada[2] = "h"
            entrada[3] = int(data[dataline])
            print entrada
            cursor.execute('INSERT INTO datos VALUES(?,?,?,?)',entrada)
            con.commit()
            dataline +=1
            entrada[1] = str(edad)
            entrada[2] = "m"
            entrada[3] = int(data[dataline])
            print entrada
            cursor.execute('INSERT INTO datos VALUES(?,?,?,?)',entrada)
            con.commit()
            dataline +=1
con.close()
            
    
