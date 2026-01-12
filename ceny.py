# nový parameter sadzba_dph
def spocitaj_s_dph(cena, sadzba_dph):
    return cena * (1 + sadzba_dph)

# nový parameter percento
def vypocitaj_zlavu(cena, percento):
    return cena * (1 - percento)
