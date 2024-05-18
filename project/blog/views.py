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

def blog_search(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        query = models.Blog.objects.filter(titulo__icontains=consulta)
    else:
        query = models.Blog.objects.all()
        
    context = {"blogs": query}
    return render(request, "blog/index.html", context)

def blog_fullview(request, pk):
    query = models.Blog.objects.get(id=pk)
    return render(request, "blog/blog_fullview.html", {"blog": query})

def blog_update(request, pk: int):
    query = models.Blog.objects.get(id=pk)
    if request.method == "POST":
        form = forms.BlogForm(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect("blog:home")
    else:
        form = forms.BlogForm(instance=query)
    return render(request, "blog/blog_create.html", context={"form": form})