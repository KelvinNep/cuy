import requests

# URL tujuan untuk mengirim file
url = "https://smkn4-tanjungpinang.sch.id/"

# Buat data file yang akan dikirim
files = {
    "file": open("nama_file_anda.pdf", "rb")
}  # Ganti 'nama_file_anda.pdf' dengan nama file yang sesuai

# Kirim file ke website
response = requests.post(url, files=files)

# Periksa respons dari server
if response.status_code == 200:
    print("File berhasil terkirim!")
else:
    print("Terjadi kesalahan saat mengirim file. Kode status:", response.status_code)
