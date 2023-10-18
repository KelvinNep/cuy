import socket
import ssl
import time


class ServerConnection:
    def __init__(self, ip, port, use_tls=False):
        self.ip = ip
        self.port = port
        self.use_tls = use_tls
        self.ssl_client_socket = None

    def open_connection(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if self.use_tls:
                context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                self.ssl_client_socket = context.wrap_socket(
                    self.client_socket, server_hostname=self.ip
                )
            else:
                self.ssl_client_socket = self.client_socket

            self.ssl_client_socket.connect((self.ip, self.port))
            print(
                f"Terhubung ke {self.ip}:{self.port} dengan SSL/TLS"
                if self.use_tls
                else f"Terhubung ke {self.ip}:{self.port}"
            )

        except Exception as e:
            print(
                f"Gagal terhubung ke {self.ip}:{self.port} dengan SSL/TLS. Kesalahan: {str(e)}"
            )

    def send_data(self, data, repeat=1):
        try:
            for i in range(repeat):
                # Mengirim data ke server
                self.ssl_client_socket.send(data.encode("utf-8"))

                # Menerima data dari server
                received_data = self.ssl_client_socket.recv(1024).decode("utf-8")
                print(f"Data yang diterima dari server: {received_data}")

        except Exception as e:
            print(
                f"Gagal mengirim atau menerima data ke/dari {self.ip}:{self.port}. Kesalahan: {str(e)}"
            )

    def close_connection(self):
        self.ssl_client_socket.close()
        print(
            f"Koneksi ke {self.ip}:{self.port} dengan SSL/TLS ditutup"
            if self.use_tls
            else f"Koneksi ke {self.ip}:{self.port} ditutup"
        )


def main():
    ip = input("Masukkan alamat IP target: ")
    port = int(input("Masukkan port target: "))
    use_tls = input("Gunakan TLS (y/n)? ").strip().lower() == "y"
    data_to_send = input("Masukkan data yang ingin dikirim: ")
    repeat = int(input("Berapa kali data akan dikirim: "))

    server_connection = ServerConnection(ip, port, use_tls)
    server_connection.open_connection()

    try:
        while True:
            server_connection.send_data(data_to_send, repeat)
            time.sleep(1)  # Menunggu 1 detik sebelum mengirim lagi
    except KeyboardInterrupt:
        # Tangani jika pengguna menekan Ctrl+C
        pass
    finally:
        server_connection.close_connection()


if __name__ == "__main__":
    main()
