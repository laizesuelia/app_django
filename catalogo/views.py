from django.shortcuts import render

# Create your views here.

def index(request):
    obras = [
        {
            "id": 1, 
            "titulo": "Interestelar",
            "tipo": "Filme",
        },
        {
            
            "id": 2, 
            "titulo": "GoT",
            "tipo": "Série",
        }
    ]
    contexto = {
        "obras": obras,
    }
    return render(request, "catalogo/index.html", contexto)