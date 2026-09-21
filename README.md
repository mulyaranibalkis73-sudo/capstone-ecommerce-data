# Capstone E-Commerce Data Collection

## 1. Deskripsi Proyek

Proyek ini merupakan implementasi data collection pipeline
untuk domain E-Commerce.

Data dikumpulkan dari dua sumber berbeda:

1. UCI Online Retail Dataset
2. Fake Store REST API

Data dikumpulkan secara otomatis menggunakan Python.

---

## 2. Sumber Data

### A. UCI Online Retail

Dataset transaksi penjualan online.

Sumber:
https://archive.ics.uci.edu/dataset/352/online+retail

Data akan dikonversi menjadi:

data/raw/online_retail.csv

### B. Fake Store API

REST API publik untuk data produk e-commerce.

Endpoint:

https://fakestoreapi.com/products

Data disimpan sebagai:

data/raw/products.json

---

## 3. Struktur Repository

capstone-ecommerce-data/

├── data/
│   └── raw/
│       ├── online_retail.csv
│       └── products.json
│
├── data_dictionary/
│   └── data_dictionary.csv
│
├── data_collection.py
├── requirements.txt
└── README.md

---

## 4. Instalasi

Pastikan Python sudah terinstall.

Install dependency:

pip install -r requirements.txt

---

## 5. Menjalankan Data Collection

Jalankan:

python data_collection.py

Script akan:

1. Membuat folder data/raw/
2. Mengambil dataset Online Retail
3. Mengubah dataset menjadi CSV
4. Mengambil data produk dari REST API
5. Menyimpan data ke folder data/raw/

---

## 6. Reproducibility

Pipeline dapat dijalankan kembali oleh anggota
kelompok lain menggunakan perintah:

python data_collection.py

Sehingga proses pengumpulan data tidak bergantung
pada proses manual.
