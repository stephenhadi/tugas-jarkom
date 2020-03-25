import random
class listSoal:
    def __init__(self):
        self.arrOfSoal = []
        self.number = random.sample(range(1,6),4)
        self.number.sort()

    def fetchSoal(self):
        f = open("soal.txt", "r")
        n = "2."
        line = f.readline()
        while line:
            temp = line[0 : 2]
            if(temp == n):
                soal = line[2:].lstrip()
                pilihan = []
                line = f.readline()
                while line:
                    if(line.find('--')):
                        jawaban = line[0:2]
                        line = line.replace("--","")
                    pilihan.append(line.strip())
                    line = f.readline()
                    if line.strip() == '':
                        break
                print(pilihan,jawaban)
            else:
                line = f.readline()



