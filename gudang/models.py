from django.db import models
from django.contrib.auth.models import User

class Barang(models.Model):
    nama = models.CharField(max_length=200, help_text="ContohL Indomie Goreng")
    tempat_produksi = models.CharField(max_length=200, help_text="Contoh: Pt Indofood")
    halal = models.BooleanField(default=False, help_text="Centang jika barang ini bersertifikat halal")
    tanggal_kadaluarsa = models. DateField(help_text="Pilih tanggal kadaluarsa Barang")
    stok = models.IntegerField(help_text="Masukkan jumlah stok barang")
    
    @property
    def kadaluarsa(self):
        from datetime import date
        return date.today() > self.tanggal_kadaluarsa
    
    def __str__(self):
        return self.nama
    
class UserProfile(models.Model):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('pekerja', 'Pekerja'),
        ('viewer', 'Viewer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='viewer')
    
    def __str__(self):
        return f"{self.user.username} ({self.role})"
# Create your models here.
