"""PDDIKTI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
# from .views import PtAutocomplete

urlpatterns = [
    path('', views.index, name='index'),
    path('cari_pt/', views.cari_pt, name='cari_pt'),
    path('detail_detail_pt/', views.detail_detail_pt, name='detail_detail_pt'),
    # path('auto/', views.auto, name='auto'),
    path('detail_pt/', views.detail_pt, name='detail_pt'),
    path('dosen/', views.dosen, name='dosen'),
    path('dosen_no_jabfung/', views.dosen_no_jabfung, name='dosen_no_jabfung'),
    path('dosen_no_pasca/', views.dosen_no_pasca, name='dosen_no_pasca'),
    path('cari_prodi/', views.cari_prodi, name='cari_prodi'),
    path('prodi/', views.prodi, name="prodi"),
    path('cari_dosen/', views.cari_dosen, name='cari_dosen'),
    path('auto_dosen/', views.auto_dosen, name='auto_dosen'),
    # path('cari_mhs/', views.cari_mhs, name='cari_mhs'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    path('auto_mhs/', views.auto_mhs, name='auto_mhs'),
    path('index_pt/', views.index_pt, name='index_pt'),
    path('detail_data_pt/', views.detail_data_pt, name='detail_data_pt'),
    path('cari_data_pt/', views.cari_data_pt, name='cari_data_pt'),
    path('auto_data_pt/', views.auto_data_pt, name='auto_data_pt'),
    # path('validate_cari/', views.validate_cari, name='validate_cari'),
    # path('pt_autocomplete', PtAutocomplete.as_view(), name='pt_autocomplete'),
]
