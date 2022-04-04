from File import *
from Solver import *
from time import perf_counter
x = True
while(x):
    print("====================")
    print("= 15-Puzzle-Solver =")
    print("====================")
    print("Pilih Metode: ")
    print("1. Input File")
    print("2. Randomizer")
    print("3. Exit")
    inputPilihan = int(input(">> "))

    if(inputPilihan == 1):
        print("contoh: test/puzzlex.txt")
        inputfile = input("Masukkan nama file : ")
        file = File()
        puzzle = file.txtToMatriks(inputfile)
        puzzle.printMatriks()
        waktuMulai = perf_counter()
        if (puzzle.isSolve()) :
            puzzle.printInversi()
            hasil = puzzle.hitungInversi()
            print("Nilai fungsi kurang untuk tiap ubin: ")
            print("Total : ", hasil)
            print("Total Kurang(i) + X = ", hasil + puzzle.cariX())
            print("Status: ")
            print("Puzzle bisa diselesaikan")
            temp = copy.deepcopy(puzzle)
            puzzle.simpul[tuple(puzzle.convert(puzzle.matriks))] = 'none'
            while (not puzzle.cost(puzzle.matriks) == 16):
                puzzle.BnB()
            temp.langkah = puzzle.langkah.split(" ")
            while (len(temp.langkah) != 1) :
                temp.navigasi()
                temp.printMatriks()
            print("Jumlah simpul yang dibangkitkan : " + str(len(puzzle.simpul) - 1))
        else :
            puzzle.printInversi()
            print("puzzle tidak bisa diselesaikan")
            hasil = puzzle.hitungInversi()
            print("Total : ", hasil)
            print("Total Kurang(i) + X = ", hasil + puzzle.cariX())
        waktuSelesai = perf_counter()
        print("waktu : " + str(waktuSelesai-waktuMulai) + " detik")
            
    elif(inputPilihan == 2):
        file = File()
        puzzle = file.randomizer()
        puzzle.printMatriks()
        waktuMulai = perf_counter()
        if (puzzle.isSolve()) :
            print("Nilai fungsi kurang untuk tiap ubin: ")
            puzzle.printInversi()
            hasil = puzzle.hitungInversi()
            print("Total : ", hasil)
            print("Total Kurang(i) + X = ", hasil + puzzle.cariX())
            print("Puzzle bisa diselesaikan")
            temp = copy.deepcopy(puzzle)
            puzzle.simpul[tuple(puzzle.convert(puzzle.matriks))] = 'none'
            while (not puzzle.cost(puzzle.matriks) == 16) :
                puzzle.BnB()
            temp.langkah = puzzle.langkah.split(" ")
            while (len(temp.langkah) != 1) :
                temp.navigasi()
                temp.printMatriks()
            print("Jumlah simpul yang dibangkitkan : " + str(len(puzzle.simpul) - 1))
        else :
            puzzle.printInversi()
            print("puzzle tidak bisa diselesaikan")
            hasil = puzzle.hitungInversi()
            print("Total : ", hasil)
            print("Total Kurang(i) + X = ", hasil + puzzle.cariX())
        waktuSelesai = perf_counter()
        print("waktu : " + str(waktuSelesai-waktuMulai) + " detik")

    elif(inputPilihan == 3):
        exit()
        
    endstate = input("Apakah anda ingin mencoba lagi? (y/n) : ")
    if(endstate == "n"):
        print("\n")
        print("==================================")
        print("==Terima Kasih sudah bermain !!!==")
        print("==================================")
        print("\n")
        x = False