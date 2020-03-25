class SoalModel:
    def __init__(self, soal, pilihan, jawaban):
        self.soal = soal
        self.pilihan = pilihan
        self.jawaban = jawaban

    def getSoal(self):
        return self.soal

    def getPilihan(self):
        return self.pilihan

    def getJawaban(self):
        return self.jawaban