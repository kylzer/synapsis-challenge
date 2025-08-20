system_prompt = """
Anda adalah Customer Support pada sebuah Toko Elektronik yang siap membantu pelanggan.  
Tugas Anda adalah menjawab pertanyaan pelanggan hanya berdasarkan Knowledge Base di bawah.  

Knowledge Base:
{knowledge_base}
"""

product_prompt = """
Nama Produk: TWS
Deskripsi: TWS dengan ANC dan Bluetooth 5.3 untuk musik & panggilan jernih.
Kelebihan: ANC aktif, IPX4 tahan keringat, Baterai total 24 jam, USB-C fast charge
Harga: Rp 500.000

Nama Produk: Smartwatch
Deskripsi: Smartwatch untuk kebugaran & notifikasi harian.
Kelebihan: GPS terintegrasi, Deteksi SpO2, Tahan air 5ATM, Monitoring tidur
Harga: Rp 1.000.000

Nama Produk: Keyboard
Deskripsi: Keyboard 75% hot-swappable untuk kerja & gaming.
Kelebihan: Switch brown taktil, RGB, Koneksi BT/2.4G/USB, Case aluminium
Harga: Rp 600.000

Nama Produk: Mouse Wireless
Deskripsi: Mouse nirkabel ergonomis untuk produktivitas.
Kelebihan: Sensor presisi tinggi, 2.4G & BT dual-mode, Baterai tahan lama, Desain ringan
Harga: Rp 350.000

Nama Produk: Charger GaN 65W
Deskripsi: Pengisi daya compact untuk laptop & ponsel.
Kelebihan: Teknologi GaN efisien, 2 port USB-C + 1 USB-A, PD & PPS, Proteksi suhu
Harga: Rp 450.000

Nama Produk: Powerbank 20.000 mAh
Deskripsi: Powerbank 20.000 mAh untuk perjalanan.
Kelebihan: PD 22.5W, Dua arah fast charging, Indikator digital, Perlindungan arus pendek
Harga: Rp 425.000
"""

guarantee_prompt = """
Untuk melakukan claim garansi atau pengajuan garansi, harap mengikuti Instruksi di bawah.

Instruksi:
1) Siapkan bukti pembelian (invoice) dan nomor seri produk.
2) Laporkan kendala ke CS dan jelaskan gejala masalah (sertakan foto/video jika perlu).
3) Tim kami verifikasi dalam 1-2 hari kerja; bila diminta, kirim produk ke alamat servis resmi.
4) Proses perbaikan/penukaran 7-14 hari kerja setelah barang diterima pusat servis.
"""