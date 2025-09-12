from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_barang, name='daftar_barang'),
    path('tambah/', views.tambah_barang, name='tambah_barang'),
    path('edit/<int:barang_id>/', views.edit_barang, name='edit_barang'),
    path('hapus/<int:barang_id>/', views.hapus_barang, name='hapus_barang'),
]