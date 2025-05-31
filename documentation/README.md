# Challenge Test - Programming Solutions

Repositori ini berisi solusi untuk Challenge Test yang terdiri dari 5 soal pemrograman Python dan Arduino.

## Struktur Direktori

```
project_root/
├── soal_python/
│   ├── soal1/
│   │   └── main.py
│   ├── soal2/
│   │   └── flask_api.py
│   ├── soal3/
│   │   └── weather_sampling.py
│   ├── soal4/
│   │   └── mqtt_publisher_app.py
│   ├── log/
│   │   ├── data_weather.json
│   │   └── mqtt_log_DDMMYY.csv
│   └── function/
│       ├── statistical_functions.py
│       ├── grade_processor.py
│       ├── weather_sampler.py
│       └── mqtt_publisher.py
├── soal_wokwi/
│   └── link.txt
└── documentation/
    ├── README.md
    ├── requirements.txt
    └── video/
```

## Setup dan Requirements

### 1. Virtual Environment (Sangat Direkomendasikan)

**PENTING**: Sangat disarankan untuk menggunakan virtual environment, terutama untuk soal 2-4 yang menggunakan library eksternal.

**Windows:**
```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate

# Untuk deaktivasi (setelah selesai)
deactivate
```

**Linux/macOS:**
```bash
# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment
source venv/bin/activate

# Untuk deaktivasi (setelah selesai)
deactivate
```

### 2. Install Dependencies

Pastikan virtual environment sudah aktif, kemudian install dependencies:

```bash
pip install -r requirements.txt
```

**⚠️ CATATAN PENTING**: 
- Untuk soal 1: Virtual environment opsional (tidak menggunakan library eksternal)
- Untuk soal 2-4: **WAJIB** mengaktifkan virtual environment terlebih dahulu
- Pastikan prompt terminal menunjukkan `(venv)` sebelum menjalankan program

## Cara Menjalankan Program

### Soal 1 - Statistical Functions

Program untuk menghitung nilai maksimum, minimum, rata-rata, dan modus dari list 10 angka.

```bash
cd soal_python/soal1
python main.py
```

### Soal 2 - Flask REST API

**⚠️ PASTIKAN VIRTUAL ENVIRONMENT AKTIF!**

REST API untuk mengkonversi nilai numerik menjadi nilai huruf dengan status kelulusan.

```bash
# Aktifkan venv terlebih dahulu
venv\Scripts\activate  # Windows
# atau
source venv/bin/activate  # Linux/macOS

cd soal_python/soal2
python flask_api.py
```

**Contoh Request:**
```bash
curl -X POST http://localhost:8080/api/bram \
  -H "Content-Type: application/json" \
  -d '{"nilai": 85}'
```

**Contoh Response:**
```json
{
  "nama": "bram",
  "nilai": "A",
  "status": "lulus"
}
```

### Soal 3 - Weather Data Sampling

**⚠️ PASTIKAN VIRTUAL ENVIRONMENT AKTIF!**

Program untuk sampling data cuaca menggunakan OpenWeatherMap API.

**Penting:** Sebelum menjalankan program, ganti `your_api_key_here` di file `function/weather_sampler.py` dengan API key yang valid dari OpenWeatherMap.

```bash
# Aktifkan venv terlebih dahulu
venv\Scripts\activate  # Windows
# atau
source venv/bin/activate  # Linux/macOS

cd soal_python/soal3
python weather_sampling.py
```

Program akan meminta input interval sampling dalam detik, kemudian akan terus melakukan sampling sesuai interval yang ditentukan.

### Soal 4 - MQTT Publisher

**⚠️ PASTIKAN VIRTUAL ENVIRONMENT AKTIF!**

Program untuk mengirim data sensor ke MQTT broker dengan logging ke file CSV.

**Penting:** Ganti variabel `candidate_name` di file `mqtt_publisher_app.py` dengan nama kandidat yang sesuai.

```bash
# Aktifkan venv terlebih dahulu
venv\Scripts\activate  # Windows
# atau
source venv/bin/activate  # Linux/macOS

cd soal_python/soal4
python mqtt_publisher_app.py
```

Program akan:
- Mengambil data temperature dan humidity dari file `data_weather.json` (hasil soal 3)
- Generate random data untuk sensor lainnya
- Publish ke MQTT broker `test.mosquitto.org`
- Log semua aktivitas ke file CSV

### Soal 5 - ESP32-S3 Arduino (Wokwi)

Kode Arduino untuk ESP32-S3 yang membaca sensor DHT22 dan RTC DS1307, kemudian mengirim data via MQTT.

**File:** `soal_wokwi/link.txt` berisi link project Wokwi

**Komponen yang digunakan:**
- ESP32-S3
- DHT22 (Temperature & Humidity Sensor)
- DS1307 (Real Time Clock)

**Koneksi:**
- DHT22 Data Pin → GPIO 21
- DS1307 SDA → GPIO 8
- DS1307 SCL → GPIO 9

## Catatan Penting

1. **Virtual Environment**: **WAJIB** untuk soal 2-4. Pastikan prompt terminal menunjukkan `(venv)` sebelum menjalankan program.

2. **Internet Connection**: Soal 3, 4, dan 5 memerlukan koneksi internet untuk mengakses API dan MQTT broker.

3. **File Dependencies**: Soal 4 bergantung pada file JSON yang dihasilkan oleh soal 3.

## Format Logging

### Weather Data (data_weather.json)
```json
{
    "temperature": 28.5,
    "humidity": 65,
    "timestamp": "2025-05-31 14:30:00",
    "unit_temperature": "Celsius",
    "unit_humidity": "Percent"
}
```

### MQTT Log (mqtt_log_DDMMYY.csv)
```
timestamp;sensor1;sensor2;sensor3;sensor4;sensor5;status
2025-05-31 14:30:00;45;678.32;true;28.5;65;Success
```

## Troubleshooting

1. **Virtual Environment Error**: Pastikan virtual environment sudah dibuat dan diaktifkan dengan benar
2. **Import Error**: Pastikan semua dependencies telah terinstall dengan benar dalam virtual environment
3. **API Connection Error**: Periksa koneksi internet dan validitas API key
4. **MQTT Connection Error**: Pastikan dapat mengakses test.mosquitto.org (port 1883)
5. **File Not Found**: Pastikan struktur direktori sesuai dengan yang dijelaskan
6. **ModuleNotFoundError**: Pastikan virtual environment aktif dan dependencies sudah terinstall

## Video Demo

Video demonstrasi untuk setiap soal tersimpan dalam direktori `documentation/video/`:
- `soal1_demo.mkv`
- `soal2_demo.mkv`
- `soal3_demo.mkv`
- `soal4_demo.mkv`
- `soal5_demo.mkv`