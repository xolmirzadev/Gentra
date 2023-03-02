class Gentra:
    def __init__(self):
        self.dvigatel = Dvigatel()
        self.boshqarish = Boshqarish()
        self.tormozlar = Tormozlar()

    def tezlanish(self):
        self.dvigatel.tezlashtirish()

    def tormoz(self):
        self.tormozlar.tormoz_pedalini_bosmoq()

    def burilish(self, yonalish):
        self.boshqarish.burilish(yonalish)


class Dvigatel:
    def __init__(self):
        self.dv = 0

    def tezlashtirish(self):
        self.dv += 10


class Boshqarish:
    def __init__(self):
        self.rul = 0

    def burilish(self, yonalish):
        if yonalish == "chap":
            self.rul -= 1
        elif yonalish == "o'ng":
            self.rul += 1


class Tormozlar:
    def __init__(self):
        self.bosish = 0

    def tormoz_pedalini_bosmoq(self):
        self.bosish += 2
