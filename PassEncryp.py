import hashlib

# El texto que queremos encriptar lo pasamos a bytes dentro del método md5()
result = hashlib.md5(b"pass123")
# al resultado le llamaremos la función hexdigest(), que retorna una encriptación en hexadecimal
print(result.hexdigest())