# contekan pemabahasan https://www.ilmuskripsi.com/2016/07/algoritma-c45.html
import csv
import math

class C45:
    def __init__(self, csv_file):
        self.dataset = self.read_dataset(csv_file)
        self.cls = self.find_classes(self.dataset)
        self.jml_kasus_total = len(self.dataset)

        # langkah 1 : cari akar
        self.akar = self.cari_akar( self.dataset, self.cls, self.jml_kasus_total)

        

    
    def read_dataset(self, csv_file):
        _list = list()
        with open(csv_file, 'r') as _file:
            reader = csv.reader(_file)
            for item in reader:
                _list.append(item)
        return _list
    
    def find_classes(self, ds):
        class_list = list()
        for item in ds:
            if item[-1] not in class_list:
                class_list.append(item[-1])
        
        return class_list
    
    def cari_entropi_root(self, dataset, kelas, jml_kasus):
        # rumus entropi : sigma -pi*log2pi
        # cari masing2 nilai dari kelas yang tersedia
        occur_kelas = dict()

        for kls in kelas:
            kls_count = 0
            for item in dataset:
                if item[-1] == kls:
                    kls_count+=1
            occur_kelas[kls] = kls_count
        
        # hitung entropi
        entr = 0
        for item in occur_kelas.values():
            temp = -((item/jml_kasus)*math.log((item/jml_kasus),2))
            entr+=temp
        
        return entr




    
    def cari_akar(self, dataset, kelas, jml_kasus):
        entropi_total = self.cari_entropi_root(dataset, kelas, jml_kasus)

        # cari entropi per kolom
        entropi_kolom = list()

        for item in dataset:
            pass # bisa dioper per kolom

