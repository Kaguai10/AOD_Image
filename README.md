<div align=center>
<img src="https://readme-typing-svg.herokuapp.com?size=30&color=1830ba&center=true&vCenter=true&width=600&lines=Art+Of+Data+Image+Format">
</div>

# 🖼 AOD - *Art Of Data* Image Format

**AOD** adalah format gambar eksperimental yang menggunakan struktur file berbasis *chunk*, dirancang untuk menyimpan data gambar dalam bentuk mentah (*raw*) atau terkompresi, dengan dukungan metadata opsional. Format ini terinspirasi dari PNG namun disederhanakan dan dimodifikasi untuk tujuan edukasi dan penelitian forensik.

---

## 📦 Struktur File AOD

| Offset | Ukuran   | Field                | Deskripsi                                           |
|--------|----------|----------------------|-----------------------------------------------------|
| 0      | 4 byte   | `AOD1`               | Magic number + versi format                         |
| 4      | 4 byte   | `HDRC`               | ID *chunk* header                                   |
| 8      | 4 byte   | Width (big-endian)   | Lebar gambar                                        |
| 12     | 4 byte   | Height (big-endian)  | Tinggi gambar                                       |
| 16     | 1 byte   | Kedalaman warna      | 3 = RGB, 4 = RGBA                                   |
| 17     | 1 byte   | Flag kompresi        | 0 = Tidak ada, 1 = zlib kompresi                   |
| 18     | n byte   | *Chunk* `META` (ops) | Metadata opsional (penulis, deskripsi, dll.)        |
| ??     | 4 byte   | `PXDT`               | ID *chunk* untuk data piksel                        |
| ??     | 4 byte   | Panjang data         | Panjang data piksel (terkompresi atau mentah)       |
| ??     | n byte   | Data gambar          | Data gambar sebenarnya                              |
| ??     | 4 byte   | `FOOT`               | ID *chunk* penutup                                  |
| ??     | 4 byte   | CRC32                | CRC checksum dari data gambar                      |

---

## 🛠 Encoder

Script `encode_aod.py` digunakan untuk mengubah file `.png` menjadi file `.aod`.

### 🔧 Penggunaan

```bash
python encode_aod.py
```

### ✅ Fitur:
- Kompresi data piksel opsional menggunakan zlib  
- Menyisipkan metadata seperti `Author`  
- Mendukung gambar RGB dan RGBA  
- Secara otomatis menghasilkan checksum CRC32

---

## 🔎 Decoder

Script `decode_aod.py` digunakan untuk membaca dan mengekstrak file `.aod` kembali menjadi `.png`.

### 🔧 Penggunaan

```bash
python decode_aod.py
```

### ✅ Fitur:
- Memvalidasi magic number dan struktur *chunk*  
- Secara otomatis mendekompresi data jika terkompresi  
- Mengekstrak metadata yang disisipkan  
- Memverifikasi CRC untuk mendeteksi file yang rusak

---

## 📋 Format Metadata yang Didukung

Metadata disimpan dalam *chunk* `META` dengan format sederhana:

| Tipe (2 byte) | Panjang (2 byte) | Nilai (n byte) |
|---------------|------------------|----------------|
| `0x01`        | panjang           | Penulis        |
| `0x02`        | panjang           | Deskripsi      |
| …             | …                 | …              |

Kamu bisa mendefinisikan tag sendiri selama mengikuti struktur yang sama.

---

## 💡 Kenapa AOD?

AOD bukan hanya sekadar format gambar — ini adalah *format edukatif dan analitis*. AOD dibuat untuk:
- Mengajarkan bagaimana format file berbasis *chunk* bekerja  
- Digunakan dalam tantangan Capture The Flag (CTF), misalnya untuk encoding atau steganografi  
- Menjadi alternatif ringan dan sepenuhnya terkontrol dibandingkan PNG

---

## 🔐 Catatan Keamanan

- Tidak ditujukan untuk penggunaan produksi  
- Tidak mendukung fitur lanjutan seperti transparansi atau animasi  
- Ideal untuk riset, pelatihan, dan tantangan keamanan
