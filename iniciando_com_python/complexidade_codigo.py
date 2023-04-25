velocidade = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_acima_velocidade = velocidade > RADAR_1

carro_multado_no_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_acima_velocidade:
    print('Velocidade do carro está acima do limite')

if carro_multado_no_radar_1 and carro_acima_velocidade:
    print('Carro multado em radar 1')
