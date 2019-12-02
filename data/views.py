import json

from django.shortcuts import render
# , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import AkreditasiPt, Prodi, Dosen, Mahasiswa, PerguruanTinggi, PrestasiMhs


def index(request):
    list_akre_pt = AkreditasiPt.objects.all().order_by('-tgl_sk_akred_sp')
    paginator = Paginator(list_akre_pt, 20)
    page = request.GET.get('page')
    akre_pt = paginator.get_page(page)
    return render(request, 'data/index.html', {'akred': akre_pt})


def index_pt(request):
    list_akre_pt = AkreditasiPt.objects.all().order_by('tst_sk_akred_sp')
    paginator = Paginator(list_akre_pt, 20)
    page = request.GET.get('page')
    akre_pt = paginator.get_page(page)
    print(paginator.page_range)
    return render(request, 'data/index_pt.html', {'akred': akre_pt})


# Search PT
def cari_pt(request):
    data = request.GET
    cari = data.get('npsn')
    if cari:
        hasil = AkreditasiPt.objects.all().filter(npsn__icontains=cari)
        return render(request, 'data/show_pt.html', {'z': hasil})
    else:
        return render(request, 'data/cari_pt.html')


def detail_pt(request):
    np = request.GET.get('npsn')
    hasil = AkreditasiPt.objects.all().filter(npsn__icontains=np)
    return render(request, 'data/detail_pt.html', {'pt': hasil})

def detail_detail_pt(request):
    data = request.GET
    cari = data.get('kode_pt')
    if cari:
        hasil = Prodi.objects.all().filter(kode_pt__icontains=cari)
        hasil = hasil.order_by('-tgl_sk_akred_prodi')
        return render(request, 'data/detail_detail_pt.html',{'z': hasil})
    else:
        return render(request, 'data/cari_pt.html')

# Prodi
def cari_prodi(request):
    data = request.GET
    cari = data.get('kode_pt')
    if cari:
        hasil = Prodi.objects.all().filter(kode_pt__icontains=cari)
        hasil = hasil.order_by('-tgl_sk_akred_prodi')
        return render(request, 'data/show_prodi.html', {'z': hasil})
    else:
        return render(request, 'data/cari_prodi.html')


def prodi(request):
    list_prodi = Prodi.objects.all()
    list_prodi = list_prodi.order_by('-tgl_sk_akred_prodi')
    paginator = Paginator(list_prodi, 20)
    page = request.GET.get('page')
    prodi = paginator.get_page(page)
    print(paginator.page_range)
    return render(request, 'data/prodi.html', {'prodi': prodi})


# Dosen
def cari_dosen(request):
    data = request.GET
    cari = data.get('nm_sdm')
    print(cari)
    if cari:
        hasil = Dosen.objects.all().filter(nm_sdm__icontains=cari)
        return render(request, 'data/show_dosen.html', {'z': hasil})
    else:
        return render(request, 'data/cari_dosen.html')


def dosen(request):
    list_dosen = Dosen.objects.all()
    belum_jabfung = len(Dosen.objects.all().filter(nm_jabfung = ""))
    # & Dosen.objects.all().filter(nm_stat_aktif = "Aktif"))
    s1 = len(Dosen.objects.all().filter(nm_stat_aktif = "Aktif"))
    # & Dosen.objects.all().filter(pendidikan = "S1"))
    paginator = Paginator(list_dosen,10)
    page = request.GET.get('page')
    dosen = paginator.get_page(page)
    context = {
        'dosen': dosen,
        'jabfung': belum_jabfung,
        'dosen_s1' : s1
    }
    return render(request,'data/dosen.html', context)


def dosen_no_jabfung(request):
    list_dosen = Dosen.objects.all().filter(nm_jabfung = "")
    # & Dosen.objects.all().filter(nm_stat_aktif = "Aktif")
    belum_jabfung = len(Dosen.objects.all().filter(nm_jabfung = ""))
    # & Dosen.objects.all().filter(nm_stat_aktif = "Aktif"))
    paginator = Paginator(list_dosen,10)
    page = request.GET.get('page')
    dosen = paginator.get_page(page)
    context = {
        'dosen': dosen,
        'jabfung' : belum_jabfung,
    }
    return render(request,'data/dosen_no_jabfung.html', context)


def dosen_no_pasca(request):
    list_dosen = Dosen.objects.all().filter(nm_stat_aktif = "Aktif") & Dosen.objects.all().filter(pendidikan = "S1")
    s1 = len(Dosen.objects.all().filter(nm_stat_aktif = "Aktif") & Dosen.objects.all().filter(pendidikan = "S1"))
    paginator = Paginator(list_dosen,10)
    page = request.GET.get('page')
    dosen = paginator.get_page(page)
    context = {
        'dosen': dosen,
        'dosen_s1' : s1,
    }
    return render(request,'data/dosen_no_pasca.html', context)


# Mahasiswa
def mahasiswa(request):
    list_mahasiswa = Mahasiswa.objects.all().order_by('nipd')
    #list_mahasiswa = list_prodi.order_by('-tgl_sk_akred_prodi')
    list_prestasimhs = PrestasiMhs.objects.all()
    paginator = Paginator(list_mahasiswa, 10)
    page = request.GET.get('page')
    mahasiswa = paginator.get_page(page)
    return render(request, 'data/mahasiswa.html', {
        'mahasiswa': mahasiswa,
        'prestasimhs': list_prestasimhs
    })

# def cari_mhs(request):
#     data = request.GET
#     cari = data.get('nm_pd')
#     print(cari)
#     results = []
#     if cari:
#         results.append(user_json)
#     data = json.dumps(results)
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)


def auto_dosen(request):
    data = request.GET
    username = data.get("term")
    if username:
        users = Dosen.objects.filter(nm_sdm__icontains=username)
    else:
        users = Dosen.objects.all()
    results = []
    for user in users:
        user_json = {}
        user_json['id'] = user.id
        user_json['label'] = user.nm_sdm
        user_json['value'] = user.nm_sdm
        results.append(user_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def auto_mhs(request):
    data = request.GET
    username = data.get("term")
    if username:
        users = Mahasiswa.objects.filter(nm_pd__icontains=username)
    else:
        users = Mahasiswa.objects.all()
    results = []
    for user in users:
        user_json = {}
        user_json['id'] = user.id
        user_json['label'] = user.nm_pd
        user_json['value'] = user.nm_pd
        results.append(user_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

#cari detail_perguruan_tinggi

def cari_data_pt(request):
    data = request.GET
    cari = data.get('nm_lemb')
    if cari:
        hasil = PerguruanTinggi.objects.all().filter(nm_lemb__icontains=cari)
        return render(request, 'data/detail_data_pt.html', {'z': hasil})
    else:
        return render(request, 'data/cari_data_pt.html')

def detail_data_pt(request):
    np = request.GET.get('npsn')
    hasil = PerguruanTinggi.objects.all().filter(npsn__icontains=np)
    return render(request, 'data/detail_data_pt.html', {'datapt': hasil})

def auto_data_pt(request):
    data = request.GET
    username = data.get("term")
    if username:
        users = PerguruanTinggi.objects.filter(nm_lemb__icontains=username)
    else:
        users = PerguruanTinggi.objects.all()
    results = []
    for user in users:
        user_json = {}
        user_json['id'] = user.id_sp
        user_json['label'] = user.nm_lemb
        user_json['value'] = user.nm_lemb
        results.append(user_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)