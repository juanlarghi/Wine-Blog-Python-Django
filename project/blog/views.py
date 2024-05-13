from django.shortcuts import render, redirect, HttpResponse
from . import models, forms

def home(request):
    blogs = models.Blog.objects.all().order_by('fecha')
    return render(request, 'blog/index.html', {'blogs': blogs})

def blog_create(request):
    if request.method == "POST":
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
    else:
        form = forms.BlogForm()
    return render(request, "blog/blog_create.html", context={"form":form})

#def blog_search(request):
#    query = models.Blog.objects.all()
#    if request.GET["consulta"]:
#        consulta = request.GET["consulta"]
#        query = models.Blog.objects.filter(consulta__icontains=consulta)
#        context = {"articulos": query}
#        return render(request, 'blog/index.html', context)
#    else:
#        query = models.Blog.objects.all()
#        return HttpResponse("No se encontro ningun titulo")