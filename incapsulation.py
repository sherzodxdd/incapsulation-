class BankHisobi:
    def __init__(self, egasi, boshlangich_balans):
        self.__egasi = egasi
        self.__balans = boshlangich_balans

    def get_balans(self):
        return self.__balans

    def get_egasi(self):
        return self.__egasi

    def pul_qosh(self, miqdor):
        if miqdor <= 0:
            print("Noto'g'ri miqdor!")
            return
        else:
            self.__balans += miqdor

    def pul_yech(self, miqdor):
        if miqdor <= 0:
            print("Noto'g'ri miqdor!")
        elif miqdor > self.__balans:
            print("Mablag' yetarli emas!")
        else:
            self.__balans -= miqdor

hisob = BankHisobi("Sherzodbek", 1_000_000)
print(f"Egasi: {hisob.get_egasi()}")
print(f"Balans: {hisob.get_balans()} so'm!")

hisob.pul_qosh(200_000)
print(f"balans: {hisob.get_balans()} so'm!")

hisob.pul_yech(300_000)
print(f"balans: {hisob.get_balans()} so'm!")

hisob.pul_yech(1_100_000)
print(f"balans: {hisob.get_balans()} so'm!")
