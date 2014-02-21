# coding=utf-8

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from datos.models import Pregunta
from datos.models import Respuesta

def preguntas(request, id):
	pregunta = Pregunta.objects.get(id=id)
	print(pregunta.enunciado)

	casos = pregunta.caso_set.all()
	#print(casos)
	
	#print(len(casos))

	diccionarioSi = {'Vizcaya':0, 'Álava':0, 'Guipúzcoa':0}
	diccionarioNo = {'Vizcaya':0, 'Álava':0, 'Guipúzcoa':0}

	for caso in casos:
		provincia = caso.provincia.encode('utf-8')
		print(provincia)
		
		respuesta = caso.respuesta_set.filter(pregunta=pregunta)
		for r in respuesta:
			print(r.respuesta)
			if r.respuesta == '1':
				diccionarioSi[provincia] += 1
			if r.respuesta == '0':
				diccionarioNo[provincia] += 1
			
	print(diccionarioSi)
	print(diccionarioNo)

	totalVizcaya = diccionarioSi['Vizcaya'] + diccionarioNo['Vizcaya']
	totalGuipuzcoa = diccionarioSi['Guipúzcoa'] + diccionarioNo['Guipúzcoa']
	totalAlava = diccionarioSi['Álava'] + diccionarioNo['Álava']

	#print(totalVizcaya)

	porcentajeSiVizcaya = float(diccionarioSi['Vizcaya']) / totalVizcaya * 100
	porcentajeSiGuipuzcoa = float(diccionarioSi['Guipúzcoa']) / totalGuipuzcoa * 100
	porcentajeSiAlava = float(diccionarioSi['Álava']) / totalAlava * 100
	
	print('%s Vizcaya' % str(porcentajeSiVizcaya))
	print('%s Guipúzcoa' % str(porcentajeSiGuipuzcoa))
	print('%s Álava' % str(porcentajeSiAlava))

	colorVizcaya = porcentajeSiVizcaya * 255 / 100
	colorGuipuzcoa = porcentajeSiGuipuzcoa * 255 / 100	
	colorAlava = porcentajeSiAlava * 255 / 100

	print('%s ColorV' % str(colorVizcaya))
	print('%s ColorG' % str(colorGuipuzcoa))
	print('%s ColorA' % str(colorAlava))

	return HttpResponse("Mira la consola!")


