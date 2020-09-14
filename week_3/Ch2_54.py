waveLength = input('Please input the wavelength(nm): ')
try:
    waveLength = float(waveLength)
    if waveLength < 380:
        print('The wavelength is lower than the visible light')
    elif 380 <= waveLength < 450:
        print('Violet')
    elif 450 <= waveLength < 495:
        print('Blue')
    elif 495 <= waveLength < 570:
        print('Green')
    elif 570 <= waveLength < 590:
        print('Yellow')
    elif 590 <= waveLength < 620:
        print('Orange')
    elif 620 <= waveLength <= 750:
        print('Red')
    else:
        print('The wavelength is higher than the visible light')
except:
    print('Please input the "WAVELENGTH"!!!')