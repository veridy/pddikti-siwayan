SELECT
	dbo.v_satuan_pendidikan.id_sp,
	dbo.v_satuan_pendidikan.npsn,
	dbo.v_satuan_pendidikan.nm_lemb,
CASE
		
		WHEN w.id_level_wil = 3 THEN
		w2.nm_wil 
		WHEN w.id_level_wil = 2 THEN
		w1.nm_wil ELSE w.nm_wil 
	END AS provinsi_pt,
CASE
		
		WHEN w.id_level_wil = 3 THEN
		w1.nm_wil ELSE w.nm_wil 
	END AS kabupaten_pt,
CASE
		
		WHEN w.id_level_wil = 3 THEN
		w.nm_wil 
	END AS kecamatan_pt,
	dbo.v_satuan_pendidikan.jln,
	dbo.v_satuan_pendidikan.sk_pendirian_sp,
	dbo.v_satuan_pendidikan.tgl_sk_pendirian_sp,
	dbo.v_satuan_pendidikan.stat_sp,
	dbo.v_satuan_pendidikan.kode_pos,
	dbo.v_yayasan.nm_lemb,
	dbo.v_kepemilikan_sp.no_akta,
	dbo.v_kepemilikan_sp.tgl_akta,
	dbo.v_satuan_pendidikan.last_update,
	dbo.v_satuan_pendidikan.soft_delete 
FROM
	dbo.v_satuan_pendidikan
	LEFT JOIN dbo.v_kepemilikan_sp ON dbo.v_satuan_pendidikan.id_sp = dbo.v_kepemilikan_sp.id_sp
	LEFT JOIN dbo.v_yayasan ON dbo.v_kepemilikan_sp.id_yayasan = dbo.v_yayasan.id_yayasan
	LEFT JOIN ref.wilayah w ON v_satuan_pendidikan.id_wil= w.id_wil
	LEFT JOIN ref.wilayah w1 ON w.id_induk_wilayah = w1.id_wil
	LEFT JOIN ref.wilayah w2 ON w1.id_induk_wilayah = w2.id_wil