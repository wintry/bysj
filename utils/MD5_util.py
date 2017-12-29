import hashlib


def md5Encode(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()