from django.shortcuts import render, redirect, get_object_or_404
from .models import Fibra


# NOVA IMPLEMENTAÇÃO

def home(request):
    return render(request, 'monitoramento/home.html')

def nova_medicao(request):
    if request.method == "POST":
        Fibra.objects.create(
            nome_cliente=request.POST["nome_cliente"],
            tipo_fibra=request.POST["tipo_fibra"],
            nivel_sinal=request.POST["nivel_sinal"],
            rua=request.POST.get("rua", ""),
            numero=request.POST.get("numero", ""),
            bairro=request.POST.get("bairro", ""),
            cidade=request.POST.get("cidade", ""),
            estado=request.POST.get("estado", ""),
            cep=request.POST.get("cep", ""),
        )
        return redirect("/lista/")
    return render(request, 'monitoramento/nova_medicao.html')


def lista_medicoes(request):
    medicoes = Fibra.objects.all()  # Pega todas as medições do banco de dados
    return render(request, 'monitoramento/lista_medicoes.html', {'medicoes': medicoes})


def editar_medicao(request, pk):
    # Obter o objeto Fibra pela pk
    medicao = get_object_or_404(Fibra, pk=pk)

    if request.method == "POST":
        # Atualizar os campos com os dados do formulário
        medicao.nome_cliente = request.POST["nome_cliente"]
        medicao.tipo_fibra = request.POST["tipo_fibra"]
        medicao.nivel_sinal = request.POST["nivel_sinal"]
        medicao.rua = request.POST.get("rua", "")
        medicao.numero = request.POST.get("numero", "")
        medicao.bairro = request.POST.get("bairro", "")
        medicao.cidade = request.POST.get("cidade", "")
        medicao.estado = request.POST.get("estado", "")
        medicao.cep = request.POST.get("cep", "")

        # Salvar as alterações
        medicao.save()

        # Redirecionar para a lista de medições
        return redirect("/lista/")


    return render(request, 'monitoramento/editar_medicao.html', {'medicao': medicao})


def deletar_medicao(request, pk):
    # Obter a medição pela PK
    medicao = get_object_or_404(Fibra, pk=pk)
    if request.method == "POST":
        medicao.delete()
        return redirect('lista_medicoes')  # ou sua view de lista
    return render(request, 'monitoramento/confirmar_delecao.html', {'medicao': medicao})
