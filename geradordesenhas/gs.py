import random, string

tamanho = int(input('Digite o tamanho da senha gerada: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%&()=+,.:/?'

rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))
