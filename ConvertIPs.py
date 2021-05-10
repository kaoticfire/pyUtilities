#  Copyright (c) 6/5/20, 1:31 AM.
#  Author 'Virgil Hoover'
#  License 'MIT License'


def convert_ip4_to_ip6() -> str:
    """ Convert an IPv4 address to an IPv6 address """
    ip6_octets = []
    ip4 = input('Enter the IPv4 address to convert: ')
    for i in ip4.split('.'):
        ip6_octets.append(hex(int(i)))
    final_string = ':'.join(ip6_octets).replace('0x', '')
    ip6 = final_string[:final_string.rfind(':')] + "::" + final_string[final_string.rfind(':') + 1:]
    return 'The IPv4 address is ' + ip4 + '\nThe IPv6 address is 2001:' + ip6


# noinspection PyStatementEffect
def create_local_link_ip(ip: str, cidr=64) -> str:
    """ Convert an IPv6 address into a unique Local Link IPv6 address """
    ip_list = []
    final_string = ''
    binary_string = ''
    for item in ip.split(':'):
        while len(item) < 4:
            item = '0' + item
        ip_list.append(item)
    binary_string += (convert_to_binary(ip_list[0: int(cidr / 16)][0]))
    if binary_string[6] != 1:
        binary_string[6] = 1
    for _ in [(binary_string[i:i + 4]) for i in range(0, len(binary_string), 4)]:
        final_string += _ + ':'
    return final_string


def convert_to_binary(character_string: str):
    """ Creates a binary string from a string of characters """
    return ''.join(format(ord(i), 'b') for i in character_string)


def format_mac(mac_address_string: str) -> str:
    """ Returns a formatted string of a MAC address for use in creating a Local Link IPv6 address """
    return mac_address_string.replace('-', '')


def binary_to_decimal(binary: list) -> int:
    """ Converts a binary number into a decimal number (Base2 into Base10) """
    decimal = 0
    for i in range(len(binary)):
        if binary.pop() == '1':
            decimal += pow(2, i)
    return decimal


def convert_to_string(binary_data: str) -> str:
    """ Some magic work with strings, most likely not needed or used anymore """
    str_data = ''
    for i in range(0, len(binary_data), 7):
        str_data += chr(binary_to_decimal(list(binary_data[i:i + 7])))
    return str_data


if __name__ == '__main__':
    ipv6 = input('Enter your IPv6 Address')
    mac_address = input('Enter your MAC Address: ')
    print(convert_ip4_to_ip6())
    print(convert_to_string(create_local_link_ip(cidr=64, ip=ipv6)))
    print(format_mac(mac_address_string=mac_address))
