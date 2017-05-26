#!/usr/bin/env python


def str_to_hex(string):
    return "-".join("{:02x}".format(ord(c)) for c in str(string))


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

delimiter = '%-12345X@PJL'
enable_wifi = '@PJL DEFAULT OBJBRNET="459138.2:1"'
flush_data = '@PJL DEFAULT OBJBRNET="458865:1"'


def wifi_mode(mode):
    if mode == 'infrastructure':
        bit = 1

    elif mode == 'adhoc':
        bit = 2

    return '@PJL DEFAULT OBJBRNET="458878:%s"' % bit


def encryption_type(mode):
    if mode == 'open':
        bit = 1

    elif mode == 'wep':
        bit = 1

    elif mode == 'wpa2':
        bit = 3

    return '@PJL DEFAULT OBJBRNET="458881:%s"' % bit


def encryption_mode(mode):
    if mode == 'none':
        bit = 1

    elif mode == 'wep':
        bit = 2

    elif mode == 'tkip':
        bit = 3

    elif mode == 'aes':
        bit = 4

    return '@PJL DEFAULT OBJBRNET="458880:%s"' % bit


def ip_mode(mode):
    if mode == 'auto':
        bit = 0

    elif mode == 'dhcp':
        bit = 3

    elif mode == 'static':
        #todo: need to figure out how to assign static address info
        bit = 7

    return '@PJL DEFAULT OBJBRNET="458970.2:%s"' % bit


#todo: figure out what this is for? is it required to set the net info? or is it just used to change the printer name?
def node_name(name):
    return '@PJL DEFAULT OBJBRNET="458961.2:%s"' % str(name)


def psk(key):
    output = []
    if len(key) <= 32:
        output.append('@PJL DEFAULT OBJBRNET="458890:%s"' % str_to_hex(key))
    elif len(key) >= 32:
        first = False
        for chunk in chunks(key, 32):
            if not first:
                first = True

            if first:
                output.append('@PJL DEFAULT OBJBRNET="458890:%s="' % str_to_hex(chunk))
            else:
                output.append('@PJL DEFAULT OBJBRNET="458890:=-%s"' % str_to_hex(chunk))

    return "\n".join(output)


def set_ssid(ssid):
    return '@PJL DEFAULT OBJBRNET="458877:%s"' % str_to_hex(ssid)


def generate_commands(ssid, enc_key, enc_type='wpa2', enc_mode='aes'):
    commands = [
            delimiter,
            enable_wifi,
            set_ssid(ssid),
            wifi_mode('infrastructure'),
            encryption_type(enc_type),
            encryption_mode(enc_mode),
            ip_mode('dhcp'),
            psk(enc_key),
            flush_data,
            delimiter,
            ]

    return "\r\n".join(commands)
