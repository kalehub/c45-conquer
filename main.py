# decision tree using c45
import numpy as np
import csv
import math

def read_dataset(data):
    dataset = list()
    with open(data, 'r') as datas:
        reader = csv.reader(datas)
        for item in reader:
            dataset.append(item)
    return np.array(dataset)


def get_entro_all(datas):
    entrp_total = 0
    total = len(datas)
    value,count = np.unique(datas[:, -1], return_counts=True)

    for c in count:
        temp = -((c/total)*math.log2(c/total))
        entrp_total+=temp
    return entrp_total
        


def mod_dataset(data):
    # print(data[:, 0])
    for i in range(0, 3):
        # print(np.unique(data[:,i], return_counts=False))
        unique_ = np.unique(data[:,i], return_counts=False)
        data_ = data[:,i]
        for j in range(0, len(unique_)):
            data_ = np.where(data_ == unique_[j], int(j), data_) 
            data[:,i] = data_
    return data

def get_entro(data):
    amount = len(data) # 14
    label = np.unique(data[:,-1], return_counts=False)

    for m in range(0, (len(data[0])-1)):
        attr_case = list()
        uni_count = np.unique(data[:,m], return_counts=False)
        arr_ = data[:,m]
        # print(arr_[arr_ == uni_count[1]])
        for i in range(0, len(uni_count)):
            # print(arr_[arr_ == uni_count[i]]) # amount of cases
            _amount = arr_[arr_ == uni_count[i]]
            attr_case.append(len(arr_[arr_ == uni_count[i]]))
        print(attr_case)


    


def main():
   # read the dataset 
   DATASET_DIR = 'c45D.csv'
   dataset = read_dataset(DATASET_DIR)

   # clean and modify the dataset
   dataset = mod_dataset(dataset)
   print(dataset)

   # calculate total entrophy
   entro_all = get_entro_all(dataset)
   print('entrophy total :',entro_all)

   # entrophy per column
   my_root = get_entro(dataset)





if __name__ == '__main__':
    main()

