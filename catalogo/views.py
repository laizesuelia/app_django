from django.shortcuts import render

# Create your views here.

obras = [
    {
        "id": 1,
        "titulo": "Interestelar",
        "tipo": "Filme",
        "ano": 2014,
        "genero": "ficcao",
        "descricao": "Astronauta viajando a Lua",
    },
    {
        "id": 2,
        "titulo": "GoT",
        "tipo": "Série",
        "ano": 2014,
        "genero": "ação",
        "descricao": "Familias brigando por tronos",
    }
]


def index(request):
    contexto = {
        "obras": obras,
    }
    return render(request, "catalogo/index.html", contexto)


def detalhes(request, id):
    obra_encontrada = None

    for obra in obras:
        if obra["id"] == id:
            obra_encontrada = obra
            break

    contexto = {
        "obra": obra_encontrada,
    }

    return render(request, "catalogo/detalhes.html", contexto)