# Copywright (c) 2024 Kevin Dalli
 
import itertools
import hashlib

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
import hashlib

def anonymize_ip(ip):
    ip_hash = hashlib.md5(ip.encode()).hexdigest()
    ip_hash = ip_hash[:8]
    anonymized_ip = ''
    for char in ip_hash:
        if char.isdigit():
            anonymized_ip += chr(ord('a') + int(char))
        else:
            anonymized_ip += chr(ord('k') + ord(char) - ord('a'))

    return anonymized_ip

def validip(ip):
    # to differentiate between hostnames and IP addresses
    # if the text has three or more dots AND it has no letters, it's an IP address
    # if it is a valid IP, return true, if not, return false
    return ip.count('.') >= 3 and not any(c.isalpha() for c in ip)