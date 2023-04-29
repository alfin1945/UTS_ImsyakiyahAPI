from django.urls import path
from . import views


app_name = 'jadwalImsyakiyahRamadhan_1444H_Sumbawa'


urlpatterns = [
    path('', views.readjadwal),
    path('alamat/<int:id>', views.readjadwallol),
    path('buat/', views.createjadwal),
    path('edit/<int:id>', views.updatejadwal),
    path('hapus/<int:id>', views.deletejadwal),
]
