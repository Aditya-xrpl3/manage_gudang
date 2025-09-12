from django import forms
from .models import Barang

class BarangForm(form.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama', 'tempat_produksi', 'halal', 'tanggal_kadaluarsa','stok']
        widgets = {
            'tanggal_kadaluarsa': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'halal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama barang'}),
            'tempat_produksi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan tempat produksi'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan jumlah stok'}),  
        }