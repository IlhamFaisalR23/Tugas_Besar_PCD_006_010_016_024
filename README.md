# 🕹️ Metal Slug Gesture Controller

Kontrol game **Metal Slug** menggunakan **gesture tangan dan gerakan tubuh** dengan deteksi real-time berbasis **MediaPipe**.

## ✨ Fitur Utama
- Deteksi gesture tangan dan kepala secara real-time dengan MediaPipe
- Antarmuka FastAPI dengan tampilan video langsung (live feed)
- Otomasi keyboard untuk mengontrol permainan
- Mendukung 7+ gesture interaktif untuk berbagai aksi

## 🎮 Tabel Gesture dan Mapping Keyboard

| Gesture           | Tombol           | Penjelasan                                                                 |
|-------------------|------------------|----------------------------------------------------------------------------|
| 🤚 Idle           | `None`           | Diam, tidak ada aksi                                                      |
| ✋ Jalan / Maju   | `Arrow Right`    | Angkat tangan kiri lurus ke depan                                         |
| 🫲 Arah Maju      | `-` (DPAD/Arrow) | Gerakan kepala ke kanan sebagai pelengkap arah maju                      |
| 🔫 Shoot          | `x`              | Tangan kanan mengarah ke depan seperti memegang pistol                    |
| 💣 Grenade        | `s`              | Gerakan melempar dari belakang ke depan dengan tangan kanan              |
| 🔫⬆️ Shoot Upward | `Arrow Up + x`   | Arahkan tangan kanan ke atas seperti menembak ke atas                    |
| 🔽 Crouch         | `Arrow Down`     | Kepala menunduk hingga hidung lebih rendah dari posisi telinga           |
| 🦘 Jump           | `z`              | Lompat hingga posisi pundak tidak terlihat dalam frame (melampaui batas) |

## 🧠 Deskripsi Gesture Singkat

- **Idle** → Tidak melakukan gestur, karakter tetap diam  
- **Maju (Run)** → Angkat tangan kiri ke depan untuk berjalan  
- **Arah Maju (Kepala)** → Gerakkan kepala ke kanan untuk mengarahkan karakter  
- **Tembak (Shoot)** → Angkat tangan kanan seolah memegang pistol  
- **Lempar Granat (Grenade)** → Buat gerakan lempar dari belakang ke depan dengan tangan kanan  
- **Tembak ke Atas (Shoot Upward)** → Arahkan tangan ke atas seperti menembak  
- **Menunduk (Crouch)** → Tundukkan kepala hingga posisi hidung lebih rendah dari telinga  
- **Lompat (Jump)** → Angkat kedua tangan hingga pundak keluar dari frame  

## 🚀 Instalasi

1. Klone repositori ini:  
   `git clone https://github.com/IlhamFaisalR23/Tugas_Besar_PCD_006_010_016_024.git`  

2. Masuk ke direktori hasil clone:  
   `cd Tugas_Besar_PCD_QuadroPipe-006_010_016_024`  

3. Pindah ke folder aplikasi utama:  
   `cd 02_FastAPI_Interface`  

4. (Opsional) Gunakan virtual environment, lalu install dependensi:  
   `pip install -r requirements.txt`  

5. Jalankan aplikasi:  
   `python main.py`  

---

💡 *Pastikan webcam berfungsi dan pencahayaan cukup untuk hasil deteksi gesture yang optimal.*
