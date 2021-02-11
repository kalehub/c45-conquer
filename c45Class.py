# contekan pemabahasan https://www.ilmuskripsi.com/2016/07/algoritma-c45.html
import csv
import math
import operator


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

        return entro_res, jml_kasus_atribut

    def find_gain(self, entro_kol, kasus, total):
        gain_dict = dict()
        for i in range(0, len(kasus)):
            active_key = None
            final_gain = 0
            for key in kasus[i]:
                active_key = key
                # print('key : {} : {} : {}'.format(
                #     key, kasus[i][active_key], entro_kol[i][active_key]))
                k_ = kasus[i][active_key]
                e_ = entro_kol[i][active_key]
                t_gain = (k_/self.jml_kasus_total)*e_
                # print(t_gain)
                final_gain += t_gain
            # print(total-final_gain)
            gain_dict[i] = total-final_gain
            # final_gain = total-temp_gain
            # print(final_gain)
        return gain_dict

    def cari_akar(self, dataset, kelas, jml_kasus):
        jml_kolom = len(dataset[0])
        entropi_total = self.cari_entropi_root(dataset, kelas, jml_kasus)

        # cari entropi per kolom
        entropi_kolom = list()
        occ_ = list()

        for i in range(0, jml_kolom-1):
            _col = i
            # entr_atr = self.hitung_entropy(dataset, kelas, _col)
            entro, occ = self.hitung_entropy(dataset, kelas, _col)
            entropi_kolom.append(entro)
            occ_.append(occ)

        # print(entropi_kolom)
        # print(occ_)

        # hitung gain
        atr_gain = self.find_gain(entropi_kolom, occ_, entropi_total)

        print(atr_gain)
        # mengambil key dari nilai terbesar
        root = max(atr_gain.items(), key=operator.itemgetter(1))[0]
        return root
