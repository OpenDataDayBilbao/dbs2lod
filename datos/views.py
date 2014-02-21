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

	return HttpResponse("Mira la consola!")


