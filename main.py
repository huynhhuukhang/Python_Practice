from abc import ABC, abstractmethod
class ho_nha_meo(ABC):
    def __init__(self,ten,loai,maulong,khuvuc,tuoi):
        self.ten=ten
        self.loai=loai
        self.maulong=maulong
        self.khuvuc=khuvuc
        self.tuoi=tuoi
    def location(self):
        print(f"loai nay song o {self.khuvuc}")
        
    @abstractmethod
    def mongvuot(self):
        pass
        
    def an(self):
        print("anthit")

    def sanmoi(self):
        if self.loai=="Lion":
            print("san moi theo dan")
        else:
            print("san moi mot minh")

    def keu(self):
        print("make a sound!")

class tiger(ho_nha_meo):
    def __init__(self, ten, loai, maulong, khuvuc, tuoi, can_nang):
        super().__init__(ten, loai, maulong, khuvuc, tuoi)
        self.can_nang=can_nang
    def keu(self):
        print("ROARRR")

    def mongvuot(self):
        print("Ho bengan co mong vuot de tan cong")


class baotuyet(ho_nha_meo):
    def __init__(self, ten, loai, maulong, khuvuc, tuoi, can_nang):
        super().__init__(ten, loai, maulong, khuvuc, tuoi)
        self.can_nang=can_nang

    def keu(self):
        print("Maowwwwwww")

    def mongvuot(self):
        print("Bao tuyet dung mong vuot de leo vach da")

class Lion(ho_nha_meo):
    def __init__(self, ten, loai, maulong, khuvuc, tuoi, can_nang):
        super().__init__(ten, loai, maulong, khuvuc, tuoi)
        self.can_nang=can_nang

    def keu(self):
        print("Grrrrrrrrrr")

    def mongvuot(self):
        print("Su tu dung mong vuot de xe xac doi thu")

        
lion1=Lion("Kara","Lion","mac dinh","savana",2,200)
baotuyet1=baotuyet("tailuing","bao tuyet","mau mac dinh", "vung nui tuyet",3,50)      
tiger1=tiger("zaka","Ho bengan","trang","rung ngap man an do",2,300)

animals = [tiger1, baotuyet1,lion1]

for animal in animals:
    animal.mongvuot()

