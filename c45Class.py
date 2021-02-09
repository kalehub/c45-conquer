# contekan pemabahasan https://www.ilmuskripsi.com/2016/07/algoritma-c45.html
import csv
import math


class C45:
    def __init__(self, csv_file):
        self.dataset = self.read_dataset(csv_file)
        self.cls = self.find_classes(self.dataset)
        self.jml_kasus_total = len(self.dataset)

        # langkah 1 : cari akar
        self.akar = self.cari_akar(
            self.dataset, self.cls, self.jml_kasus_total)

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
                    kls_count += 1
            occur_kelas[kls] = kls_count

        # hitung entropi
        entr = 0
        for item in occur_kelas.values():
            temp = -((item/jml_kasus)*math.log((item/jml_kasus), 2))
            entr += temp

        return entr

    def hitung_entropy(self, dataset, kelas, kolom):
        jml_kasus_atribut = dict()
        unique_list = list()
        last_item = list()
        occur_dict = dict()
        occur_kls = list()

        # mencari atribut unik
        for data in dataset:
            if data[kolom] not in unique_list:
                unique_list.append(data[kolom])
                last_item.append(data[-1])

        # mencari jml kasus atribut
        for u in unique_list:
            u_counter = 0
            for data in dataset:
                if data[kolom] == u:
                    u_counter += 1
            jml_kasus_atribut[u] = u_counter
        print('Jml kasus atribut ', jml_kasus_atribut)

        # mencari kemunculan atribut dalam kolom
        for unik in unique_list:
            occur_kls = list()
            for kls in kelas:
                kls_counter = 0
                for data in dataset:
                    if data[kolom] == unik:
                        if data[-1] == kls:
                            kls_counter += 1

                occur_kls.append(kls_counter)
            # print(unik, occur_kls)
            occur_dict[unik] = occur_kls
        print('Kemunculan sub atribut dalam kolom : ')
        print(occur_dict)

        entro_res = dict()
        for key in occur_dict:
            key_entro = 0
            for value in occur_dict[key]:
                try:
                    temp = (-(value/jml_kasus_atribut[key])) * \
                        math.log2(value/jml_kasus_atribut[key])
                    key_entro += temp
                except ValueError:
                    key_entro += 0
            # print(key_entro)
            entro_res[key] = key_entro

        return entro_res

    def cari_akar(self, dataset, kelas, jml_kasus):
        jml_kolom = len(dataset[0])
        entropi_total = self.cari_entropi_root(dataset, kelas, jml_kasus)

        # cari entropi per kolom
        entropi_kolom = list()

        for i in range(0, jml_kolom-1):
            _col = i
            # entr_atr = self.hitung_entropy(dataset, kelas, _col)
            entro = self.hitung_entropy(dataset, kelas, _col)
            entropi_kolom.append(entro)

        print(entropi_kolom)
