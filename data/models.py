from django.db import models

class AkreditasiPt(models.Model):
    nm_lemb = models.CharField(max_length=30, blank=False)
    npsn = models.CharField(max_length=6, blank=False)
    nm_akred = models.CharField(max_length=1, blank=False)
    sk_akred_sp = models.CharField(max_length=40, blank=False)
    tgl_sk_akred_sp = models.DateField()
    tst_sk_akred_sp = models.DateField()
    last_update = models.DateTimeField()
    soft_delete = models.BooleanField(default=0, null=False)

    def __str__(self):
        return self.npsn

class PerguruanTinggi(models.Model):
    id_sp = models.CharField(primary_key=True, max_length=50, blank=True)
    npsn = models.CharField(max_length=10, blank=True)
    nm_lemb = models.CharField(max_length=80, blank=True)
    provinsi_pt = models.CharField(max_length=60, blank=True)
    kabupaten_pt = models.CharField(max_length=60, blank=True)
    kecamatan_pt = models.CharField(max_length=60, blank=True)
    jln = models.CharField(max_length=200, blank=True)
    sk_pendirian_sp = models.CharField(max_length=60, blank=True)
    tgl_sk_pendirian_sp = models.DateField(null=True)
    stat_sp = models.CharField(max_length=6, blank=True)
    kode_pos = models.TextField(max_length=6, blank=True)
    nm_yayasan = models.CharField(max_length=60, blank=True)
    no_akta = models.CharField(max_length=30, blank=True)
    tgl_akta = models.DateField(null=True)
    last_update = models.DateTimeField()
    soft_delete = models.BooleanField(default=0, null=True)

    def __str__(self):
        return self.npsn

class Prodi(models.Model):
    kode_pt = models.TextField(max_length=7, blank=False)
    nama_pt = models.CharField(max_length=120, blank=False)
    nm_bp = models.CharField(max_length=50)
    stat_sp = models.CharField(max_length=6, blank=False)
    kode_prodi = models.TextField(max_length=10, blank=False)
    nm_prodi = models.CharField(max_length=200, blank=False)
    nm_jenj_didik = models.CharField(max_length=6, blank=False)
    nm_akred = models.CharField(max_length=20)
    sk_akred_prodi = models.CharField(max_length=100, blank=False)
    tgl_sk_akred_prodi = models.DateField()
    tst_sk_akred_prodi = models.DateField()
    last_update = models.DateTimeField()
    last_sync = models.DateTimeField()

    def __str__(self):
        return self.kode_pt

class DataProdi(models.Model):
    npsn = models.CharField(max_length=10, blank=True)
    nm_lemb = models.CharField(max_length=80, blank=True)
    provinsi_pt = models.CharField(max_length=60, blank=True)
    kabupaten_pt = models.CharField(max_length=60, blank=True)
    kecamatan_pt = models.CharField(max_length=60, blank=True)
    stat_sp = models.CharField(max_length=20, blank=True)
    soft_delete = models.BooleanField(default=0, null=True)
    kode_prodi = models.TextField(max_length=10, blank=True)
    nm_prodi = models.CharField(max_length=200, blank=True)
    nm_jenj_didik = models.CharField(max_length=6, blank=True)
    sk_selenggara = models.CharField(max_length=40, blank=True)
    tgl_berdiri_prodi = models.DateField()
    provinsi_prodi = models.CharField(max_length=60, blank=True)
    kab_kota_prodi = models.CharField(max_length=60, blank=True)
    kecamatan_prodi = models.CharField(max_length=60, blank=True)
    stat_prodi = models.CharField(max_length=20, blank=True)
    id_sp = models.CharField(max_length=50, blank=True)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.npsn

class Dosen(models.Model):
    nidn = models.CharField(max_length=15, blank=False)
    nm_sdm = models.CharField(max_length=30, blank=False)
    npsn = models.CharField(max_length=10, blank=False)
    kode_prodi = models.CharField(max_length=10, blank=False)
    tmt_sk_angkat = models.DateField()
    nm_ikatan_kerja = models.CharField(max_length=20, blank=False)
    nm_stat_aktif = models.CharField(max_length=20, blank=False)
    nm_pangkat = models.CharField(max_length=20, blank=False)
    nm_jabfung = models.CharField(max_length=20, blank=False)
    pendidikan = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.nidn

class Mahasiswa(models.Model):
    id_pd = models.CharField(max_length=60, blank=False)
    nm_pd = models.CharField(max_length=200, blank=True)
    nipd = models.CharField(max_length=36, blank=True)
    nm_stat_mhs = models.CharField(max_length=40, blank=True)
    nik = models.CharField(max_length=16, blank=True)
    tmpt_lahir = models.CharField(max_length=200, blank=True)
    tgl_lahir = models.DateField(null=True)
    nm_ibu_kandung = models.CharField(max_length=200, blank=True)
    mulai_smt = models.CharField(max_length=10, blank=True)
    id_smt = models.CharField(max_length=10, blank=True)
    nm_smt = models.CharField(max_length=20, blank=True)
    sks_smt = models.CharField(max_length=10, blank=True)
    ips = models.CharField(max_length=10, blank=True)
    sks_total = models.CharField(max_length=10, blank=True)
    ipk = models.CharField(max_length=10, blank=True)
    ipk_reg_pd = models.CharField(max_length=10, blank=True)
    tgl_masuk_sp = models.DateField(null=True)
    tgl_keluar = models.DateField(null=True)
    nm_jns_daftar = models.CharField(max_length=100, blank=True)
    ket_keluar = models.CharField(max_length=40, blank=True)
    nm_jenj_didik = models.CharField(max_length=5, blank=True)
    no_seri_ijazah = models.CharField(max_length=50, blank=True)
    sk_yudisium = models.CharField(max_length=200, blank=True)
    tgl_sk_yudisium = models.DateField(null=True)
    npsn = models.CharField(max_length=6, blank=True)
    nm_prodi = models.CharField(max_length=60, blank=True)
    stat_sp = models.CharField(max_length=1, blank=True)
    kode_prodi = models.CharField(max_length=6, blank=True)
    last_update = models.DateTimeField(null=True)
    nm_lemb = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nik

class PrestasiMhs(models.Model):
    id_prestasi = models.CharField(max_length=60, blank=True)
    id_jns_prestasi = models.CharField(max_length=5, blank=True)
    id_tkt_prestasi = models.CharField(max_length=5, blank=True)
    id_pd = models.CharField(max_length=60, blank=True)
    id_sp = models.CharField(max_length=60, blank=True)
    nm_prestasi = models.CharField(max_length=300, blank=True)
    thn_prestasi= models.CharField(max_length=10, blank=True)
    penyelenggara = models.CharField(max_length=200, blank=True)
    peringkat = models.CharField(max_length=10, blank=True)
    asal_data = models.CharField(max_length=10, blank=True)
    tgl_create = models.DateField(null=True)
    last_update = models.DateField(null=True)
    soft_delete = models.BooleanField(default=0, null=True)

    def __str__(self):
        return self.id_prestasi
