import copy

class Solver:
    def __init__(self):
        self.matriks = [[0 for i in range(4)] for i in range(4)]
        self.queue = []
        self.langkah = ""
        self.depth = 0
        self.kurang = []
        self.simpul = {}
        
    # fungsi untuk menampilkan Puzzle
    def printMatriks(self):
        print("=============")
        for i in range(4):
            for j in range(4):
                print("|",end="")
                if (self.matriks[i][j] != 16):
                    print(self.matriks[i][j], end="")
                    if(self.matriks[i][j] < 10):
                        print(" ", end="")
                else:
                    print("X ", end="")
            print("|")
            if(i != 3):
                print("=============")
        print("=============")
            
    # fungsi untuk mengubah dari bentuk matriks (per-empat bagian)
    # ke bentuk list (satu bagian saja)
    def convert(self,matriks):
        matrix = [0 for i in range(16)]
        a = 0
        for i in range(4):
            for j in range(4):
                matrix[a] = matriks[i][j]
                a += 1
        return matrix
    
    # fungsi untuk mencari ubin yang kosong
    def cariUbinKosong(self):
        i = 0
        ketemu = False
        while(not ketemu and i < 4):
            j = 0
            while(not ketemu and j < 4):
                if(self.matriks[i][j] == 16):
                    ketemu = True
                j = j + 1
            i = i + 1
        return [i-1,j-1]
    
    #fungsi untuk mendapatkan nilai X
    def cariX(self):
        i,j = self.cariUbinKosong()[0], self.cariUbinKosong()[1]
        hasil = (i+j+2) % 2
        if(hasil == 0):
            return 0
        else:
            return 1
        
    # fungsi untuk menghitung nilai cost
    def cost(self,matriks):
        total = 0
        count = 1
        for i in range(4):
            for j in range(4):
                if(matriks[i][j] == count):
                    total += 1
                count += 1
        return total
    
    # fungsi untuk mengecek apakah puzzle bisa diselesaikan atau tidak
    def isSolve(self):
        hasil = self.hitungInversi() + self.cariX()
        if(hasil % 2 != 0):
            return False
        else:
            return True
    
    #fungsi untuk mengecek apakah sudah dalam bentuk akhir
    def isFinal(self):
        if(self.cost(self.matriks) != 16):
            return False
        else:
            return True

    #fungsi untuk menghitung nilai "Kurang" dari puzzle
    def hitungInversi(self):
        matriks = []
        for i in range(4):
            for j in range(4):
                matriks.append(self.matriks[i][j])
        total = 0
        for i in range(16):
            inversi = 0
            for j in range(i,16):
                if(matriks[j] < matriks[i]):
                    total += 1
                    inversi += 1
            self.kurang.append([i+1,inversi])
        inversi = self.kurang
        inversi.sort(key=lambda x: x[1])
        return total
    
    # fungsi untuk menampilkan nilai kurang pada setiap ubin
    def printInversi(self):
        for i in range (16):
            print("ubin ke-" + str(i+1) + " : " + str(self.kurang[i][1]))
    
    # fungsi untuk mengecek setiap pergerakan ubin
    def validasiGerak(self, matriks):
        x = self.cariUbinKosong()[0]
        y = self.cariUbinKosong()[1]
        if(matriks[1] == "bawah"):
            if(x+1 == 4):
                return False
        elif(matriks[1] == "atas"):
            if(x+1 == 1):
                return False
        elif(matriks[1] == "kanan"):
            if(y+1 == 4):
                return False
        elif(matriks[1] == "kiri"):
            if(y+1 == 1):
                return False
        return True
    
    #fungsi untuk menggerakkan ubin
    def gerak(self,matriks):
        x = self.cariUbinKosong()[0]
        y = self.cariUbinKosong()[1]
        i,j = x, y
        if(self.validasiGerak(matriks)):
            if(matriks[1] == "bawah"):
                self.swapper(matriks, 0, i, j, i+1, j)
            elif(matriks[1] == "atas"):
                self.swapper(matriks, 0, i, j, i-1, j)
            elif(matriks[1] == "kanan"):
                self.swapper(matriks, 0, i, j, i, j+1)
            if(matriks[1] == "kiri"):
                self.swapper(matriks, 0, i, j, i, j-1)
        return matriks
    
    # fungsi untuk swap nilai pada matriks karena adanya pergerakan
    def swapper(self,matriks, a, i, j, x, y):
        matriks[a][i][j] = matriks[a][x][y]
        matriks[a][x][y] = 16
    
    #fungsi untuk menampilkan keterangan navigasi pergerakan
    def navigasi(self):
        now = self.langkah.pop(0)
        if (now == 'keatas') :
            self.gerak([self.matriks, 'atas'])
            print(">> Atas")
        elif (now == 'kebawah') :
            self.gerak([self.matriks, 'bawah'])
            print(">> Bawah")
        elif (now == 'kekiri') :
            self.gerak([self.matriks, 'kiri'])
            print(">> Kiri")
        elif (now == 'kekanan') :
            self.gerak([self.matriks, 'kanan'])
            print(">> Kanan")
        else :
            pass
    
    #fungsi untuk mengalokasikan queue
    def alokasiQueue(self, posisi, gerak, command, arah):
        posisi = 16 - self.cost(gerak[0]) + self.depth
        self.simpul[tuple(self.convert(gerak[0]))] = command
        self.queue.append([posisi,self.depth,self.langkah + arah, self.convert(gerak[0])])
    
    #fungsi untuk menyalin matriks pada setiap arah
    def copyMatriks(self,matriks,command):
        posisi = []
        if(command == 'atas'):
            posisi = [copy.deepcopy(matriks), command]
        if(command == 'bawah'):
            posisi = [copy.deepcopy(matriks), command]
        if(command == 'kiri'):
            posisi = [copy.deepcopy(matriks), command]
        if(command == 'kanan'):
            posisi = [copy.deepcopy(matriks), command]
        return posisi
    
    #algoritma Branch and Bound
    def BnB(self):
        posUp = 0
        atas = self.copyMatriks(self.matriks,'atas')
        self.gerak(atas)
        posbawah = 0
        bawah = self.copyMatriks(self.matriks,'bawah')
        self.gerak(bawah)
        poskiri = 0
        kiri = self.copyMatriks(self.matriks,'kiri')
        self.gerak(kiri)
        poskanan = 0
        kanan = self.copyMatriks(self.matriks,'kanan')
        self.gerak(kanan)
        self.depth += 1
        if(tuple(self.convert(bawah[0])) not in self.simpul):
            self.alokasiQueue(posbawah, bawah, 'bawah', 'kebawah ')
        if(tuple(self.convert(atas[0])) not in self.simpul):
            self.alokasiQueue(posUp, atas, 'atas', 'keatas ')
        if(tuple(self.convert(kanan[0])) not in self.simpul):
            self.alokasiQueue(poskanan, kanan, 'kanan', 'kekanan ')
        if(tuple(self.convert(kiri[0])) not in self.simpul):
            self.alokasiQueue(poskiri, kiri, 'kiri', 'kekiri ')
        self.queue.sort()
        pop = self.queue.pop(0)
        self.depth,self.langkah = pop[1],pop[2]
        newMatriks = [[0 for i in range (4)] for i in range(4)]
        a = 0
        for i in range(4):
            for j in range(4):
                newMatriks[i][j] = pop[3][a]
                a+=1
        self.matriks = newMatriks