from django.shortcuts import render

def home(request):
<<<<<<< HEAD
    return render(request, 'usuario/index.html')
=======
    consulta_usuarios = models.Usuario.objects.all()
    context = {'usuarios': consulta_usuarios}
    return render(request, 'usuario/index.html', context)
>>>>>>> test
