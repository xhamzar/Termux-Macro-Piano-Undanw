# Termux-Macro-Piano-Undawn

Proyek ini adalah sebuah skrip Python yang digunakan untuk memainkan file MIDI pada game Undawn di perangkat Android melalui kontrol ADB dan dijalankan di Termux. Skrip ini memetakan not-not MIDI ke koordinat layar yang sesuai untuk mengetuk tombol piano pada aplikasi.

### Cara Menggunakan
1. Pastikan ADB telah terpasang di termux.
2. Jalankan skrip dengan memberikan jalur file MIDI sebagai argumen:
    ```bash
    python macro.py 'path/to/your/midi/file.mid' 0.5
    ```
4. Tekan Enter untuk memulai pemutaran.

### Dependencies
- `mido`: Digunakan untuk memproses file MIDI. Anda dapat menginstalnya dengan:
    ```bash
    pip install mido
    ```
- `adb`: Pastikan Android Debug Bridge (ADB) telah terpasang dan dapat diakses dari command line.

### Contoh Penggunaan
```bash
python macro.py 'path/to/your/midi/file.mid' 0.5
```

### Catatan
- Skrip ini menggunakan pemetaan koordinat layar yang spesifik. Anda mungkin perlu menyesuaikan koordinat tersebut sesuai dengan aplikasi piano yang Anda gunakan.
- Pemutaran MIDI dapat dihentikan kapan saja dengan menekan Ctrl+C.
