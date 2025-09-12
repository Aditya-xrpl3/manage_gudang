from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Barang
from .forms import BarangForm

@login_required
def daftar_barang(request):
    semua_barang= Barang.objects.all()
    barang_urut = sorted(semua_barang, key=lambda x: (x.kadaluarsa, x.tanggal_kadaluarsa))
    
    context = {
        'barang_list': barang_urut,
        'user_role' : request.user.userprofile.role
    }
    return render(request, 'gudang/daftar_barang.html', context)

@login_required
def tambah_barang(request):
    if request.user.userprofile.role != 'pekerja':
        return redirect('daftar_barang')
    
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_barang')
        else:
            form = BarangForm()
            
        return render(request, 'gudang/form_barang.html', {'form': form})
    
@login_required
def edit_barang(request, barang_id):
    if request.user.userprofile.role != 'pekerja':
        return redirect('daftar_barang')
    
    barang = get_object_or_404(Barang, id=barang_id)
    
    if request.method == 'POST':
        form = BarangForm(request.POST, instance=barang)
        if form.is_valid():
            form.save()
            return redirect('daftar_barang')
    else:
        form = BarangForm(instance=barang)
        
    return render(request, 'gudang/form_barang.html', {'form': form})

@login_required
def hapus_barang(request, barang_id):
    if request.user.userprofile.role != 'pekerja':
        return redirect('daftar_barang')
    
    barang = get_object_or_404(Barang, id=barang_id)
    barang.delete()
    return redirect('daftar_barang')
# Create your views here.
