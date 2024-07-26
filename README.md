# Termux-Macro-Piano-Undawn

## Deskripsi Proyek

Proyek ini adalah sebuah skrip Python yang digunakan untuk memainkan file MIDI pada aplikasi piano di perangkat Android melalui kontrol ADB dan dijalankan di Termux. Skrip ini memetakan not-not MIDI ke koordinat layar yang sesuai untuk mengetuk tombol piano pada aplikasi.

### Fitur Utama
- **Pemetaan Not**: Memetakan not piano ke koordinat layar yang sesuai.
- **Pemutaran MIDI**: Memainkan file MIDI dengan menggunakan kontrol ADB untuk mengetuk tombol pada aplikasi piano di perangkat Android.
- **Modulasi Pitch**: Menambahkan kemampuan modulasi pitch untuk menyesuaikan not MIDI.
- **Kontrol Pengguna**: Pengguna dapat memulai pemutaran MIDI dengan menekan Enter dan menghentikannya dengan Ctrl+C.

### Cara Menggunakan
1. Pastikan ADB telah terpasang dan perangkat Android Anda terhubung.
2. Jalankan skrip dengan memberikan jalur file MIDI sebagai argumen:
    ```bash
    python macro.py 'path/to/your/midi/file.mid'
    ```
3. Tekan Enter untuk memulai pemutaran.

### Dependencies
- `mido`: Digunakan untuk memproses file MIDI. Anda dapat menginstalnya dengan:
    ```bash
    pip install mido
    ```
- `adb`: Pastikan Android Debug Bridge (ADB) telah terpasang dan dapat diakses dari command line.

### Contoh Penggunaan
```bash
python macro.py 'path/to/your/midi/file.mid'
```

### Catatan
- Skrip ini menggunakan pemetaan koordinat layar yang spesifik. Anda mungkin perlu menyesuaikan koordinat tersebut sesuai dengan aplikasi piano yang Anda gunakan.
- Pemutaran MIDI dapat dihentikan kapan saja dengan menekan Ctrl+C.
