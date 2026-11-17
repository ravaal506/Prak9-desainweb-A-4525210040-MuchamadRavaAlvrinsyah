# Selaras Coffee: One Page Website

Website company profile satu halaman untuk UMKM fiktif **Selaras Coffee**, dibuat dengan **Bootstrap 5** dan custom CSS sebagai tugas individu.

## Deskripsi

Selaras Coffee adalah UMKM kopi lokal yang menjual kopi susu gula aren, kopi seduh manual V60, dan biji kopi sangrai. Website ini dibuat untuk dipresentasikan kepada calon pelanggan dan mitra bisnis. Isinya informasi produk, notifikasi promo, detail produk dalam modal, dan form kontak.

## Struktur Folder

```
selaras-coffee/
├── index.html          # Halaman utama (struktur dan komponen Bootstrap)
├── css/
│   └── style.css       # Custom CSS untuk branding
├── js/
│   └── script.js       # Isi modal produk dan validasi form
├── img/
│   ├── logo.png
│   ├── favicon.png
│   ├── hero.png
│   ├── tentang.png
│   ├── produk-kopi-susu.png
│   ├── produk-v60.png
│   ├── produk-biji-kopi.png
│   └── _generate_images.py   # Script pembuat gambar (opsional)
└── README.md
```

## Cara Menjalankan

1. Ekstrak folder project.
2. Buka `index.html` di browser (Chrome, Edge, atau Firefox).
3. Pastikan perangkat terhubung ke internet, karena Bootstrap dan Google Fonts dimuat lewat CDN.

Tidak perlu instalasi atau server tambahan.

## Komponen yang Digunakan

| No | Komponen | Keterangan |
|----|----------|------------|
| 1 | Navbar responsif | `navbar-expand-lg` dengan tombol hamburger di layar kecil |
| 2 | Hero section | Judul, deskripsi singkat, dua tombol, dan gambar latte art |
| 3 | Card (3 buah) | Es Kopi Susu Gula Aren, Seduh Manual V60, Biji Kopi Sangrai 250 g |
| 4 | Alert | Alert promo di atas hero (bisa ditutup) dan alert sukses setelah form terkirim |
| 5 | Modal | Modal detail promo dan modal detail produk |
| 6 | Form kontak | Nama, email, keperluan, dan pesan dengan validasi Bootstrap |
| 7 | Footer | Informasi brand, tautan halaman, dan kontak |
| 8 | Custom CSS | Warna, font, motif, dan gaya komponen khas Selaras Coffee |

## Identitas Brand (Custom CSS)

**Palet warna**

| Nama | Hex | Pemakaian |
|------|-----|-----------|
| Pine | `#20443B` | Navbar, hero, tombol utama |
| Amber | `#D68A1F` | Aksen, tombol ajakan, harga |
| Paper | `#FAF8F3` | Latar halaman |
| Sage | `#E8EFE4` | Latar section produk |
| Espresso | `#2B1D16` | Teks dan footer |

**Tipografi**
- Judul: Young Serif
- Isi: DM Sans

**Motif visual:** lingkaran konsentris yang muncul di logo, latte art, dan latar gambar. Motif ini melambangkan arti "selaras", yaitu rasa yang seimbang.

**Ciri khas gaya:** card dan form memakai border tebal berwarna pine, dan card mendapat bayangan ambar saat di-hover. Tampilannya jadi berbeda dari gaya bawaan Bootstrap.

Semua warna dan font disimpan sebagai variabel CSS di `:root` pada `css/style.css`, sehingga mudah diganti.

## Cara Kerja Fitur Utama

**Modal produk dinamis.** Satu modal dipakai untuk tiga produk. Tombol "Detail" menyimpan data di atribut `data-nama`, `data-harga`, `data-gambar`, dan `data-deskripsi`. Saat modal dibuka (event `show.bs.modal`), `script.js` membaca data tersebut dan menampilkannya.

**Validasi form.** Form memakai atribut `required`, `minlength`, dan `type="email"`. Saat dikirim, `checkValidity()` memeriksa isian. Jika ada yang salah, kelas `was-validated` menampilkan pesan error Bootstrap. Jika benar, alert sukses ditampilkan dan form dikosongkan. Form ini belum terhubung ke server, jadi pesan tidak benar-benar terkirim.

**Responsif.** Grid Bootstrap membuat card tampil 3 kolom di desktop (`col-lg-4`), 2 kolom di tablet (`col-md-6`), dan 1 kolom di ponsel. Navbar berubah menjadi menu hamburger di layar kecil.

## Teknologi

- HTML5
- Bootstrap 5.3.3 (CDN)
- CSS3 (custom properties)
- JavaScript (vanilla)
- Google Fonts

## Cara Mengambil Screenshot

1. Buka `index.html` di browser, lalu tekan **F12**.
2. Aktifkan mode responsif dengan **Ctrl + Shift + M**.
3. Ambil screenshot pada lebar sekitar **1366 px** (desktop) dan **390 px** (mobile).

## Catatan

- Nama usaha, harga, alamat, dan nomor telepon adalah data contoh untuk keperluan tugas.
- Gambar dibuat sendiri dalam format PNG, bukan dari sumber berhak cipta.
- Tugas ini dikerjakan secara **individu**.

## Identitas Pembuat

- Nama: _Muchamad Rava Alviansyah_
- NIM: _4525210040_
- Kelas: _desain web A_
