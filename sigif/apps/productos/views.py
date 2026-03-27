from .models import Producto
from django.shortcuts import render, redirect, get_object_or_404
from .form import ProductoForm

# haidhasdhuyhasd
def productos(request):

    return render(request, "productos/productos.html")

def crear_producto(request): 
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_productos.html', {'form': form})


def listar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def actualizar_producto(request, id):
        product = get_object_or_404(Producto, id = id)
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
        else:
            form = ProductoForm()
        return render(request, 'productos/actualizar_productos.html', {'form': form})


def eliminar_producto(request, id):
    product = get_object_or_404(Producto, id = id)
    if request.method == "POST":
        product.delete()
        return redirect('listar_productos')
    else:
        return render(request, 'productos/eliminar_productos.html', {'producto': product})
