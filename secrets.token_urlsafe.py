import secrets

url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()
print(url)
# secrets.token_hex
token1 = secrets.token_hex(16)
token2 = secrets.token_hex(9)
print(token1)
print(token2)
# secrets.token_bytes
token1 = secrets.token_bytes()
token2 = secrets.token_bytes(10)
print(token1)
print(token2)
# secrets.randbits
passwd = secrets.randbits(7)
print(passwd)
# secrets.randbelow
passwd = secrets.randbelow(20)
print(passwd)
