import os
import json
import requests
import pandas as pd


# ==========================================================
# KONFIGURASI
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

# URL dataset Online Retail dari UCI
UCI_DATASET_URL = (
    "https://archive.ics.uci.edu/static/public/352/"
    "online+retail.zip"
)

# REST API Fake Store
API_URL = "https://fakestoreapi.com/products"


# ==========================================================
# MEMBUAT FOLDER DATA/RAW
# ==========================================================

def create_directories():
    os.makedirs(RAW_DIR, exist_ok=True)

    print("Folder data/raw/ berhasil disiapkan.")


# ==========================================================
# DOWNLOAD DATA ONLINE RETAIL
# ==========================================================

def download_online_retail():
    print("\n[1] Mengambil dataset Online Retail...")

    zip_path = os.path.join(RAW_DIR, "online_retail.zip")

    response = requests.get(
        UCI_DATASET_URL,
        timeout=60
    )

    response.raise_for_status()

    with open(zip_path, "wb") as file:
        file.write(response.content)

    print("Dataset Online Retail berhasil diunduh.")

    # Membaca file Excel dari ZIP
    import zipfile

    with zipfile.ZipFile(zip_path, "r") as zip_ref:

        files = zip_ref.namelist()

        print("Isi ZIP:")
        for file_name in files:
            print("-", file_name)

        excel_file = None

        for file_name in files:
            if file_name.lower().endswith(".xlsx"):
                excel_file = file_name
                break

        if excel_file is None:
            raise FileNotFoundError(
                "File Excel Online Retail tidak ditemukan."
            )

        zip_ref.extract(
            excel_file,
            RAW_DIR
        )

    excel_path = os.path.join(
        RAW_DIR,
        excel_file
    )

    print("Membaca dataset Excel...")

    df = pd.read_excel(
        excel_path
    )

    # Mengubah menjadi CSV
    csv_path = os.path.join(
        RAW_DIR,
        "online_retail.csv"
    )

    df.to_csv(
        csv_path,
        index=False
    )

    print(
        f"Data Online Retail berhasil disimpan: {csv_path}"
    )

    print(
        f"Jumlah baris: {len(df):,}"
    )

    # Menghapus file ZIP dan Excel agar raw lebih rapi
    if os.path.exists(zip_path):
        os.remove(zip_path)

    if os.path.exists(excel_path):
        os.remove(excel_path)

    print("File sementara berhasil dibersihkan.")


# ==========================================================
# MENGAMBIL DATA DARI REST API
# ==========================================================

def download_products_api():
    print("\n[2] Mengambil data produk dari REST API...")

    response = requests.get(
        API_URL,
        timeout=30
    )

    response.raise_for_status()

    products = response.json()

    json_path = os.path.join(
        RAW_DIR,
        "products.json"
    )

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            products,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"Data produk berhasil disimpan: {json_path}"
    )

    print(
        f"Jumlah produk: {len(products)}"
    )


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    print("=" * 60)
    print("DATA COLLECTION - CAPSTONE E-COMMERCE")
    print("=" * 60)

    try:

        create_directories()

        download_online_retail()

        download_products_api()

        print("\n" + "=" * 60)
        print("DATA COLLECTION SELESAI")
        print("=" * 60)

    except requests.exceptions.RequestException as error:

        print("\nTerjadi kesalahan koneksi:")
        print(error)

    except Exception as error:

        print("\nTerjadi kesalahan:")
        print(error)


if __name__ == "__main__":
    main()
