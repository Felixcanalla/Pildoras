from django.http import HttpResponse
import datetime

documento= """<html>
<body>
<h1>
Primera pagina de DJANGO
</h1>
</body>
</html>"""

def saludo(request): #Primera VIsta
    return HttpResponse(documento)



def despedida(request): #Segunda VIsta
    return HttpResponse("Hasta la proxima")


def damefecha(request):

                 fecha_actual=datetime.datetime.now()

                 documento="""<html>
                 <body>
                 <h1>
                          Fecha y hora actuales %s
                 </h1>
                 </body>
                 </html>""" % fecha_actual 

               
               
               
                 
                 return HttpResponse(documento)