from django.shortcuts import render

from django.http import HttpResponse
import datetime

def calculadora(request, valor, num1, num2):
	if valor == 'suma':
		now = int(num1) + int(num2)    
	elif valor == 'resta':
		now = int(num1) - int(num2)
	elif valor == 'multiplicacion':
		now = int(num1) * int(num2)
	elif valor== 'division':
		now = int(num1) / int(num2)
	else :
		now = 'Error'

	html = "<html><body>El resultado es: %s.</body></html>" % now
	return render(request. 'index.html', locals())
    	

    
