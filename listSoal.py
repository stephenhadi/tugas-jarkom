import random
from SoalModel import SoalModel


class listSoal:
    def __init__(self):
        self.arrOfSoal = []
        self.number = random.sample(range(1,6),4)
        self.number.sort()

    def fetchSoal(self):
        f = open("soal.txt", "r")
        i = 0
        line = f.readline()
        while line:
            temp = line[0 : 1]
            if self.number.__len__() <= i:
                break
            if temp == str(self.number[i]):
                i+=1
                soal = line[2:].lstrip()
                pilihan = []
                line = f.readline()
                while line:
                    if line.find("--") != -1:
                        jawaban = line[0:1]
                        line = line.replace("--","")
                    pilihan.append(line.strip())
                    line = f.readline()
                    if line.strip() == '':
                        self.arrOfSoal.append(SoalModel(soal,pilihan,jawaban))
                        pilihan = []
                        break
            else:
                line = f.readline()

        return self.arrOfSoal


