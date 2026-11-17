
# 2-m
class Oquvchi:
    def __init__(self, ism, sinf):
        self.ism = ism
        self.sinf = sinf

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Sinf: {self.sinf}")


class It_Oquvchisi(Oquvchi):
    def __init__(self, ism, sinf, yonalish):
        super().__init__(ism, sinf)
        self.yonalish = yonalish

    def malumot(self):
        super().malumot()
        print(f"Yonalish: {self.yonalish}")

a = It_Oquvchisi('bunyod', 9, 'becend')
a.malumot()
