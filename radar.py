velocidade=60
local_carro=99

RADAR1=60
LOCAL_1=100
RADAR_RANGE=1

if velocidade>RADAR1:
    print('Velocidade Ultrapassada')

if local_carro >=(LOCAL_1-RADAR_RANGE) and\
        local_carro<=(LOCAL_1+RADAR_RANGE) and\
            velocidade>= RADAR1:
    print('Carro multado')
