from datos.models import Pregunta, Caso, Respuesta

DATOS_FILE = '/home/mikel/open_data/deusto_barometro_social/datos.csv'

df = open(DATOS_FILE)

first = True
index = []
counter = 1

for line in df:
    sline = line.split(';')
    if first:
        for item in sline:
            index.append(item)
        first = False
    else:
        caso = Caso()
        i = 0
        for item in sline:
            if i == 0:
                caso.key = item
            elif i == 3:
                sitem = item.split(' ')
                date = sitem[0]
                time = sitem[1]
                datetime = '%s-%s-%s %s' % (date.split('/')[2], date.split('/')[1], date.split('/')[0], time)
                caso.startTime = datetime
            elif i == 4:
                sitem = item.split(' ')
                date = sitem[0]
                time = sitem[1]
                datetime = '%s-%s-%s %s' % (date.split('/')[2], date.split('/')[1], date.split('/')[0], time)
                caso.endTime = datetime
            elif i == 8:
                if item == 'Hombre':
                    caso.sexo = Caso.SEXO_CHOICES[0]
                else:
                    caso.sexo = Caso.SEXO_CHOICES[1]
            elif i == 9:
                caso.edad = int(item.split(',')[0])
            elif i == 10:
                if item == '18 - 24':
                    caso.edad_reco = Caso.EDAD_CHOICES[0]
                elif item == '25 - 34':
                    caso.edad_reco = Caso.EDAD_CHOICES[1]
                elif item == '35 - 44':
                    caso.edad_reco = Caso.EDAD_CHOICES[2]
                elif item == '45 - 54':
                    caso.edad_reco = Caso.EDAD_CHOICES[3]
                elif item == '55  y más':
                    caso.edad_reco = Caso.EDAD_CHOICES[4]
                    
            elif i == 11:
                if item == 'alta':
                    caso.clase_social = Caso.CLASE_CHOICES[0]
                elif item == 'media alta':
                    caso.clase_social = Caso.CLASE_CHOICES[1]
                elif item == 'media media':
                    caso.clase_social = Caso.CLASE_CHOICES[2]
                elif item == 'media baja':
                    caso.clase_social = Caso.CLASE_CHOICES[3]
                elif item == 'baja':
                    caso.clase_social = Caso.CLASE_CHOICES[4]
                elif item == 'no definida':
                    caso.clase_social = Caso.CLASE_CHOICES[5]
            elif i == 12:
                caso.provincia = item
            elif i == 13:
                if item == 'Castellano':
                    caso.idioma = Caso.IDIOMA_CHOICES[1]
                else:
                    caso.idioma = Caso.IDIOMA_CHOICES[0]
                caso.save()
            if i >= 14:
                clave_pregunta = index[i].replace('\n', '')
                #print 'Pregunta: %s.' % clave_pregunta
                pregunta = Pregunta.objects.get(clave=clave_pregunta)
                respuesta = Respuesta(caso=caso, pregunta=pregunta, respuesta=item)
                respuesta.save()
                
            i += 1
        print 'Caso %s insertado en BD.' % counter
        counter += 1
            

print 'fin'   
print index
