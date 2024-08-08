# Copywright (c) 2024 Kevin Dalli
 
import itertools

def checksum(source_string):
    sum = 0
    countTo = (len(source_string) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = source_string[count + 1] * 256 + source_string[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2

    if countTo < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def xor_encrypt_decrypt(data, key):
    return bytes(a ^ b for a, b in zip(data, itertools.cycle(key.encode())))

def anonymize_ip(ip):
    parts = ip.split('.')
    return '.'.join(['x' if i % 2 == 0 else 'y' for i in range(len(parts))])