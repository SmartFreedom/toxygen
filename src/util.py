

def log(data):
    with open("logs.log", "a") as fl:
        fl.write(str(data))


def string_to_bin(tox_id):
    return tox_id.decode("hex")


def bin_to_string(raw_id):
    res = ''.join('{:02x}'.format(ord(x)) for x in raw_id)
    return res.upper()