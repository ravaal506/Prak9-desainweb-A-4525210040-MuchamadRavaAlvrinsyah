// 1) Isi modal produk sesuai tombol "Detail" yang diklik
const modalProduk = document.getElementById('modalProduk');
modalProduk.addEventListener('show.bs.modal', (event) => {
  const tombol = event.relatedTarget;           // tombol yang membuka modal
  document.getElementById('namaProduk').textContent = tombol.dataset.nama;
  document.getElementById('hargaProduk').textContent = tombol.dataset.harga;
  document.getElementById('deskripsiProduk').textContent = tombol.dataset.deskripsi;
  const gambar = document.getElementById('gambarProduk');
  gambar.src = tombol.dataset.gambar;
  gambar.alt = tombol.dataset.nama;
});

// 2) Validasi form kontak memakai validasi bawaan Bootstrap
const form = document.getElementById('formKontak');
const notif = document.getElementById('notifKirim');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!form.checkValidity()) {
    event.stopPropagation();
    form.classList.add('was-validated');
    return;
  }
  const nama = document.getElementById('nama').value.trim();
  notif.innerHTML = `
    <div class="alert alert-success alert-dismissible fade show" role="alert">
      Terima kasih, ${nama.replace(/[<>&]/g, '')}. Pesan Anda sudah kami terima dan akan dibalas dalam 1 hari kerja.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Tutup"></button>
    </div>`;
  form.reset();
  form.classList.remove('was-validated');
});
