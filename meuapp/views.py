from django.shortcuts import render

def index(request):
    print(request.method)
    nome = request.GET.get("nome")
    contexto = {
        "nome": nome
    }
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def aluno(request, id_aluno):
    contexto = {
        "id_aluno": id_aluno,
    }
    return render(request, "aluno.html", contexto)

# Create your views here.
