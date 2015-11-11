__author__ = 'Naleen'

import pickle

def write_tl_file(dataArray, dataString, fileName):
    file = open(fileName, "w")
    classAttributes="val\t"
    dataAttributes=""
    for k in range (0, len(dataArray)):
        dataAttributes=dataAttributes+"data"+str(k)+"\t"

    classType="d\t"
    dataType=""
    for k in range (0, len(dataArray)):
        dataType=dataType+"c"+"\t"

    file.write(classAttributes+dataAttributes+"\n"+classType+dataType+"\nclass\n")
    file.write(dataString.encode("UTF-8"))
    file.close()


def write_label_file(LabelList, fileName):

    with open(fileName, 'wb') as f:
        pickle.dump(LabelList, f)


def read_label_file(file):

    with open(file, 'rb') as f:
        list = pickle.load(f)
        return list
