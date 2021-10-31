from Crypto.Hash import keccak, MD5

entradaFrase = 'Contratos Inteligentes: Hands-on episódio sobre hash'
entradaPonto = '.'

kfrase = keccak.new(digest_bits=256)
kfrase.update(bytes(entradaFrase,'utf8'))
print("Keccak 256 da frase: ",kfrase.hexdigest())

kponto = keccak.new(digest_bits=256)
kponto.update(bytes(entradaPonto,'utf8'))
print("Keccak 256 do ponto: ", kponto.hexdigest())

h = MD5.new()
h.update(bytes(entradaFrase,'utf8'))
print("MD5 da frase: ",h.hexdigest())
