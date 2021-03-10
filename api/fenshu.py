class FenShu():
    def __init__(self, fenzi, fenmu):
        self.fenzi = fenzi
        self.fenmu = fenmu


class F():
    def __init__(self, fenshua, fenshub, fuhao):
        self.fenshua = fenshua
        self.fenshub = fenshub
        self.fuhao = fuhao

    def myyuefen(self, fenzi, fenmu):
        end = fenzi if fenzi <= fenmu else fenmu
        for i in range(2, end+1):
            if fenzi % i == 0 and fenmu % i == 0:
                fenzi = fenzi // i
                fenmu = fenmu // i
        if fenzi % fenmu == 0:
            return fenzi / fenmu
        else:
            return [fenzi, fenmu]

    def get_fenzi_fenmu(self):
        if self.fuhao is '+':
            if self.fenshua.fenmu == self.fenshub.fenmu:
                fenmu = self.fenshua.fenmu
                fenzi = self.fenshua.fenzi + self.fenshub.fenzi
            else:
                fenmu = self.fenshua.fenzi * self.fenshub.fenzi
                fenzi = self.fenshua.fenmu * self.fenshub.fenzi + self.fenshub.fenmu * self.fenshua.fenzi
        elif self.fuhao is '-':
            if self.fenshua.fenmu == self.fenshub.fenmu:
                fenmu = self.fenshua.fenmu
                fenzi = self.fenshua.fenzi - self.fenshub.fenzi
            else:
                fenmu = self.fenshua.fenzi * self.fenshub.fenzi
                fenzi = self.fenshua.fenmu * self.fenshub.fenzi - self.fenshub.fenmu * self.fenshua.fenzi
        elif self.fuhao is '*':
            fenmu = self.fenshua.fenmu * self.fenshub.fenmu
            fenzi = self.fenshua.fenzi * self.fenshub.fenzi
        elif self.fuhao is '\\':
            fenmu = self.fenshua.fenmu * self.fenshub.fenzi
            fenzi = self.fenshua.fenzi * self.fenshub.fenmu
        return [fenzi, fenmu]

    def run(self):
        fenzi, fenmu = self.get_fenzi_fenmu()
        ret = self.myyuefen(fenzi, fenmu)
        return ret

a = FenShu(3,2)
b = FenShu(1,2)
f = F(a, b, '\\')
ret = f.run()

print(ret)
