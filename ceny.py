# nový parameter sadzba_dph
def spocitaj_s_dph(cena, sadzba_dph):
    return cena * (1 + sadzba_dph)

def vypocitaj_zlavu(cena):
    return cena * 0.9   # zľava 10%
