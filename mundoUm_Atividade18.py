import math
ang = float(input('Digite o ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O ângulo de {}, tem o seno {}, cosseno {} e tangente {}'.format(ang, sen, cos, tang))