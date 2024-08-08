# Copywright (c) 2024 Kevin Dalli

import os
import socket
import struct
import time
import select
import argparse

from check import checksum

ICMP_ECHO_REQUEST = 8
VERSION = "1.1"

def create_packet(id, packet_size, pattern):
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, 0, id, 1)
    bytes_in_double = struct.calcsize('d')
    if pattern:
        data = pattern[:packet_size - bytes_in_double]
    else:
        data = (packet_size - bytes_in_double) * b'Q'

    data = struct.pack('d', time.time()) + data

    my_checksum = checksum(header + data)
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), id, 1)
    return header + data

def do_one_ping(dest_addr, timeout, ttl, packet_size, pattern):
    icmp = socket.getprotobyname("icmp")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
    except PermissionError as e:
        print("Operation not permitted. Run as root or higher level user.")
        return None

    my_id = os.getpid() & 0xFFFF
    packet = create_packet(my_id, packet_size, pattern)

    while packet:
        sent = sock.sendto(packet, (dest_addr, 1))
        packet = packet[sent:]

    delay = receive_one_ping(sock, my_id, time.time(), timeout, dest_addr)
    sock.close()
    return delay

def receive_one_ping(sock, id, time_sent, timeout, dest_addr):
    time_left = timeout
    while True:
        started_select = time.time()
        what_ready = select.select([sock], [], [], time_left)
        how_long_in_select = (time.time() - started_select)
        if what_ready[0] == []:
            return None

        time_received = time.time()
        rec_packet, addr = sock.recvfrom(1024)

        icmp_header = rec_packet[20:28]
        type, code, checksum, packet_id, sequence = struct.unpack('bbHHh', icmp_header)

        if packet_id == id:
            bytes_in_double = struct.calcsize('d')
            time_sent = struct.unpack('d', rec_packet[28:28 + bytes_in_double])[0]
            return time_received - time_sent

        time_left = time_left - how_long_in_select
        if time_left <= 0:
            return None

def ping(host, count, interval, interface, ttl, packet_size, timeout, quiet, audible, timestamp, numeric, pattern):
    dest = socket.gethostbyname(host)
    print(f'Pinging {dest} ({host}) > {packet_size} bytes of data:')
    
    if interface:
        print(f"Using interface: {interface}")

    sent_packets = 0
    received_packets = 0

    try:
        for i in range(count):
            sent_packets += 1
            delay = do_one_ping(dest, timeout, ttl, packet_size, pattern)
            if delay is None:
                if not quiet:
                    print(f'Ping to {dest} timed out')
            else:
                received_packets += 1
                delay = delay * 1000
                if not quiet:
                    line = f'Ping to {dest} took {delay:.2f} ms'
                    if timestamp:
                        line = f'[{time.time()}] {line}'
                    print(line)
                if audible:
                    print('\a', end='')

            time.sleep(interval)
        
        loss = sent_packets - received_packets
        print(f"Ping statistics for {dest}:")
        print(f"    Packets: Sent = {sent_packets}, Received = {received_packets}, Lost = {loss} ({(loss / sent_packets) * 100:.2f}% loss)")

        #if quiet:
        #    loss = sent_packets - received_packets
        #    print(f"Ping statistics for {dest}:")
        #    print(f"    Packets: Sent = {sent_packets}, Received = {received_packets}, Lost = {loss} ({(loss / sent_packets) * 100:.2f}% loss)")

    except KeyboardInterrupt:
        print("\nPing stopped.")
        loss = sent_packets - received_packets
        print(f"Ping statistics for {dest}:")
        print(f"    Packets: Sent = {sent_packets}, Received = {received_packets}, Lost = {loss} ({(loss / sent_packets) * 100:.2f}% loss)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ping a host.')
    parser.add_argument('host', type=str, nargs='?', help='The host to ping.')
    parser.add_argument('-c', '--count', type=int, default=4, help='Stop after sending (and receiving) count ECHO_RESPONSE packets.')
    parser.add_argument('-i', '--interval', type=int, default=1, help='Wait interval seconds between sending each packet.')
    parser.add_argument('-I', '--interface', type=str, help='Specify a network interface to use for sending packets.')
    parser.add_argument('-t', '--ttl', type=int, default=64, help='Set the IP Time to Live.')
    parser.add_argument('-s', '--packetsize', type=int, default=56, help='Specify the number of data bytes to be sent.')
    parser.add_argument('-W', '--timeout', type=int, default=1, help='Time to wait for a response, in seconds.')
    parser.add_argument('-q', '--quiet', action='store_true', help='Quiet output. Only summary lines at startup and finish will be printed.')
    parser.add_argument('-a', '--audible', action='store_true', help='Beep when a packet is received.')
    parser.add_argument('-V', '--version', action='store_true', help='Print version and exit.')
    parser.add_argument('-D', '--timestamp', action='store_true', help='Print timestamp before each line.')
    parser.add_argument('-n', '--numeric', action='store_true', help='Numeric output only. No attempt to lookup symbolic names for host addresses.')
    parser.add_argument('-p', '--pattern', type=str, help='Specify up to 16 pattern bytes to fill out the packet you send.')

    args = parser.parse_args()

    if args.version:
        print(f"Ping version {VERSION}")
    elif not args.host:
        parser.print_help()
    else:
        ping(args.host, args.count, args.interval, args.interface, args.ttl, args.packetsize, args.timeout, args.quiet, args.audible, args.timestamp, args.numeric, args.pattern.encode() if args.pattern else None)
