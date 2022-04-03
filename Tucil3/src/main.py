from copy import deepcopy
import random
import numpy as np
from Graph import *
from time import time
import sys
import tkinter

def randomPuzzle():
# Membuat random puzzle
    array = [i for i in range(1,17)]
    random.shuffle(array)
    puzzle = np.array(array, dtype='int8').reshape(4,4) 
    return puzzle

def readFile(filename):
# Membaca input file
    array = []

    f = open(filename,'r')
    lines = f.readlines()
    
    for line in lines:
        array.append(line.replace('\n','').replace(' ','').split(','))
    f.close()

    for i in range(4):
        for j in range(4):
            if (array[i][j] != ''):
                array[i][j] = int(array[i][j])
            else:
                array[i][j] = 16
    
    return np.array(array, dtype='int8')

def kurang(m, row, col):
# Realisasi Fungsi KURANG(i)
    count = 0
    e = m[row, col]
    while (row < 4):
        while (col < 4):
            if (e > m[row, col]):
                count += 1
            col += 1
        row += 1
        col = 0
    return count

def achievable(m):
# Memeriksa apakah goal state dapat dicapai dan mengembalikan nilai dari fungsi Kurang(i) untuk setiap ubin
    sum = 0
    array = np.zeros(16, dtype='int8')
    for row in range(4):
        for col in range(4):
            array[m[row, col] - 1] = kurang(m, row, col)
            sum += array[m[row,col]-1]
            if (m[row, col] == 16 and (row+col) % 2 == 1):
                sum += 1
    return (sum % 2 == 0), sum, array

def searchBlank(m):
# Mencari blok yang kosong pada puzzle
    for i in range(4):
        for j in range(4):
            if (m[i,j] == 16):
                return i,j

def g(m):
# Menghitung jumlah ubin tak kosong yang tidak terdapat pada susunan akhir
    count = 0
    for i in range(4):
        for j in range(4):
            if (m[i,j] != 16 and m[i,j] != i*4+j+1):
                count += 1
    return count

def swap(m, row1, col1, row2, col2):
# Menukar posisi elemen matriks
    mcopy = deepcopy(m)
    mcopy[row1, col1] = m[row2, col2]
    mcopy[row2, col2] = m[row1,col1]
    return mcopy

def checkNode(matrix, array):
# Memeriksa apakah matrix sudah ada di array
    for puzzle in array:
        if ((matrix==puzzle).all()):
            return True
    return False

def Play():
    global pace
    if (pace != 0):
        pace = 0
    Play1()

def Play1():
    global pace
    play['state'] = 'disabled'
    next['state'] = 'disabled'
    prev['state'] = 'disabled'
    if (pace < len(steps) - 1):
        Next()
        main_windows.after(1000,Play1)
    else:
        play['state'] = 'normal'
        next['state'] = 'normal'
        prev['state'] = 'normal'
    

def Next():
    global pace
    if (pace < len(steps) - 1):
        pace  += 1
        puzzle = steps[pace].puzzle
        label1.config(text=puzzle[0][0], background='#7ea098')
        label2.config(text=puzzle[0][1], background='#7ea098')
        label3.config(text=puzzle[0][2], background='#7ea098')
        label4.config(text=puzzle[0][3], background='#7ea098')
        label5.config(text=puzzle[1][0], background='#7ea098')
        label6.config(text=puzzle[1][1], background='#7ea098')
        label7.config(text=puzzle[1][2], background='#7ea098')
        label8.config(text=puzzle[1][3], background='#7ea098')
        label9.config(text=puzzle[2][0], background='#7ea098')
        label10.config(text=puzzle[2][1], background='#7ea098')
        label11.config(text=puzzle[2][2], background='#7ea098')
        label12.config(text=puzzle[2][3], background='#7ea098')
        label13.config(text=puzzle[3][0], background='#7ea098')
        label14.config(text=puzzle[3][1], background='#7ea098')
        label15.config(text=puzzle[3][2], background='#7ea098')
        label16.config(text=puzzle[3][3], background='#7ea098')

        i, j = steps[pace].blank
        if (i == 0 and j == 0):
            label1.config(text='', background="white")
        elif (i == 0 and j == 1):
            label2.config(text='', background="white")
        elif (i == 0 and j == 2):
            label3.config(text='', background="white")
        elif (i == 0 and j == 3):
            label4.config(text='', background="white")
        elif (i == 1 and j == 0):
            label5.config(text='', background="white")
        elif (i == 1 and j == 1):
            label6.config(text='', background="white")
        elif (i == 1 and j == 2):
            label7.config(text='', background="white")
        elif (i == 1 and j == 3):
            label8.config(text='', background="white")
        elif (i == 2 and j == 0):
            label9.config(text='', background="white")
        elif (i == 2 and j == 1):
            label10.config(text='', background="white")
        elif (i == 2 and j == 2):
            label11.config(text='', background="white")
        elif (i == 2 and j == 3):
            label12.config(text='', background="white")
        elif (i == 3 and j == 0):
            label13.config(text='', background="white")
        elif (i == 3 and j == 1):
            label14.config(text='', background="white")
        elif (i == 3 and j == 2):
            label15.config(text='', background="white")
        elif (i == 3 and j == 3):
            label16.config(text='', background="white")

def Prev():
    global pace
    if (pace > 0):    
        pace -= 1
        puzzle = steps[pace].puzzle
        label1.config(text=puzzle[0][0], background='#7ea098')
        label2.config(text=puzzle[0][1], background='#7ea098')
        label3.config(text=puzzle[0][2], background='#7ea098')
        label4.config(text=puzzle[0][3], background='#7ea098')
        label5.config(text=puzzle[1][0], background='#7ea098')
        label6.config(text=puzzle[1][1], background='#7ea098')
        label7.config(text=puzzle[1][2], background='#7ea098')
        label8.config(text=puzzle[1][3], background='#7ea098')
        label9.config(text=puzzle[2][0], background='#7ea098')
        label10.config(text=puzzle[2][1], background='#7ea098')
        label11.config(text=puzzle[2][2], background='#7ea098')
        label12.config(text=puzzle[2][3], background='#7ea098')
        label13.config(text=puzzle[3][0], background='#7ea098')
        label14.config(text=puzzle[3][1], background='#7ea098')
        label15.config(text=puzzle[3][2], background='#7ea098')
        label16.config(text=puzzle[3][3], background='#7ea098')
    
        i, j = steps[pace].blank
        if (i == 0 and j == 0):
            label1.config(text='', background="white")
        elif (i == 0 and j == 1):
            label2.config(text='', background="white")
        elif (i == 0 and j == 2):
            label3.config(text='', background="white")
        elif (i == 0 and j == 3):
            label4.config(text='', background="white")
        elif (i == 1 and j == 0):
            label5.config(text='', background="white")
        elif (i == 1 and j == 1):
            label6.config(text='', background="white")
        elif (i == 1 and j == 2):
            label7.config(text='', background="white")
        elif (i == 1 and j == 3):
            label8.config(text='', background="white")
        elif (i == 2 and j == 0):
            label9.config(text='', background="white")
        elif (i == 2 and j == 1):
            label10.config(text='', background="white")
        elif (i == 2 and j == 2):
            label11.config(text='', background="white")
        elif (i == 2 and j == 3):
            label12.config(text='', background="white")
        elif (i == 3 and j == 0):
            label13.config(text='', background="white")
        elif (i == 3 and j == 1):
            label14.config(text='', background="white")
        elif (i == 3 and j == 2):
            label15.config(text='', background="white")
        elif (i == 3 and j == 3):
            label16.config(text='', background="white")

def main():
    print("1. Input File")
    print("2. Random")
    while (True):
        try:
            select = int(input("Masukkan angka pilihan: "))
        except Exception:
            print("Masukkan salah")
        else:
            break

    if (select == 1):
        while (True):
            try:
                filename = input("Masukkan nama file: ")
                puzzle = readFile(filename)
            except Exception:
                print("File tidak ditemukan")
            else:
                break
    else:
        puzzle = randomPuzzle()
    
    print("\nMatriks posisi awal 15-puzzle")
    blank = searchBlank(puzzle)
    root = Node(None, puzzle, None, 0, 0, blank, None)
    root.show()
    print()

    start_time = time()

    solvable, sum, array = achievable(puzzle)

    print("Nilai dari fungsi Kurang (i)")
    for i in range(16):
        print("Kurang({}) = {}".format(i+1, array[i]))

    print()

    print("Nilai KURANG (i) + X =", sum)
    print()

    if (not solvable):
        print("Status tujuan tidak dapat dicapai")
    else:
        global main_windows, play, prev, next, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, label16, steps, pace

        n = 0 # Jumlah simpul yang dibangkitkan
        dNode = [] 
        lNode = LiveNodeArray([root], 1)
        while (lNode.length != 0):
            solution = lNode.pop()
            if (not checkNode(solution.puzzle, dNode)):
                dNode.append(solution.puzzle)
            else:
                continue

            if (solution.isGoal()):
                break

            row, col = solution.blank

            # geser blok kosong ke atas
            if (row != 0 and solution.previous_step != 'down'):
                m1 = swap(solution.puzzle, row - 1, col, row, col)
                cost = (solution.level + 1) + g(m1)
                s1 =  Node(solution, m1, None, solution.level + 1, cost, (row-1, col), 'up')
                lNode.append(s1)
                n += 1

            # geser blok kosong ke kanan
            if (col != 3 and solution.previous_step != 'left'):
                m2 = swap(solution.puzzle, row, col + 1, row, col)
                cost = (solution.level + 1) + g(m2)
                s2 =  Node(solution, m2, None, solution.level + 1, cost, (row, col+1), 'right')
                lNode.append(s2)
                n += 1

            # geser blok kosong ke bawah
            if (row != 3 and solution.previous_step != 'up'):
                m3 = swap(solution.puzzle, row + 1, col, row, col)
                cost = (solution.level + 1) + g(m3)
                s3 =  Node(solution, m3, None, solution.level + 1, cost, (row+1, col), 'down')
                lNode.append(s3)
                n += 1

            # geser blok kosong ke kiri
            if (col != 0 and solution.previous_step != 'right'):
                m4 = swap(solution.puzzle, row, col-1, row, col)
                cost = (solution.level + 1) + g(m4)
                s4 =  Node(solution, m4, None, solution.level + 1, cost, (row, col-1), 'left')
                lNode.append(s4)
                n += 1
    
            # Menampilkan jumlah simpul yang sudah dibangkitkan
            sys.stdout.write("\r{} {}".format("Jumlah simpul yang sudah dibangkitkan :",n))

        print("\n")

        steps = []
        p = solution
        while (p is not None):
            steps.insert(0, p)
            p = p.parent
        
        print("Langkah-langkah\n")
        for step in steps:
            step.show()
            print()

        execution_time = time() - start_time
        print("Waktu eksekusi : ", execution_time)
        print("Jumlah Langkah menuju goal state :", solution.level)

        main_windows = tkinter.Tk()
        main_windows.title("PUZZLE PROCESS")

        pace = 0

        label1 = tkinter.Label(main_windows, text=puzzle[0,0], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label2 = tkinter.Label(main_windows, text=puzzle[0,1], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label3 = tkinter.Label(main_windows, text=puzzle[0,2], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label4 = tkinter.Label(main_windows, text=puzzle[0,3], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label5 = tkinter.Label(main_windows, text=puzzle[1,0], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label6 = tkinter.Label(main_windows, text=puzzle[1,1], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label7 = tkinter.Label(main_windows, text=puzzle[1,2], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label8 = tkinter.Label(main_windows, text=puzzle[1,3], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label9 = tkinter.Label(main_windows, text=puzzle[2,0], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label10 = tkinter.Label(main_windows, text=puzzle[2,1], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label11 = tkinter.Label(main_windows, text=puzzle[2,2], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label12 = tkinter.Label(main_windows, text=puzzle[2,3], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label13 = tkinter.Label(main_windows, text=puzzle[3,0], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label14 = tkinter.Label(main_windows, text=puzzle[3,1], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label15 = tkinter.Label(main_windows, text=puzzle[3,2], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))
        label16 = tkinter.Label(main_windows, text=puzzle[3,3], background='#7ea098', foreground="white", width=3, height=1, font=("Arial", 25))

        i, j = steps[pace].blank
        if (i == 0 and j == 0):
            label1.config(text='', background="white")
        elif (i == 0 and j == 1):
            label2.config(text='', background="white")
        elif (i == 0 and j == 2):
            label3.config(text='', background="white")
        elif (i == 0 and j == 3):
            label4.config(text='', background="white")
        elif (i == 1 and j == 0):
            label5.config(text='', background="white")
        elif (i == 1 and j == 1):
            label6.config(text='', background="white")
        elif (i == 1 and j == 2):
            label7.config(text='', background="white")
        elif (i == 1 and j == 3):
            label8.config(text='', background="white")
        elif (i == 2 and j == 0):
            label9.config(text='', background="white")
        elif (i == 2 and j == 1):
            label10.config(text='', background="white")
        elif (i == 2 and j == 2):
            label11.config(text='', background="white")
        elif (i == 2 and j == 3):
            label12.config(text='', background="white")
        elif (i == 3 and j == 0):
            label13.config(text='', background="white")
        elif (i == 3 and j == 1):
            label14.config(text='', background="white")
        elif (i == 3 and j == 2):
            label15.config(text='', background="white")
        elif (i == 3 and j == 3):
            label16.config(text='', background="white")

        next = tkinter.Button(main_windows, text ="NEXT STEP", command = Next)
        prev = tkinter.Button(main_windows, text="PREV STEP", command = Prev)
        play = tkinter.Button(main_windows, text="PLAY", command = Play)

        label1.grid(row=0,column=0,padx=1,pady=1)
        label2.grid(row=0,column=1,padx=1,pady=1)
        label3.grid(row=0,column=2,padx=1,pady=1)
        label4.grid(row=0,column=3,padx=1,pady=1)
        label5.grid(row=1,column=0,padx=1,pady=1)
        label6.grid(row=1,column=1,padx=1,pady=1)
        label7.grid(row=1,column=2,padx=1,pady=1)
        label8.grid(row=1,column=3,padx=1,pady=1)
        label9.grid(row=2,column=0,padx=1,pady=1)
        label10.grid(row=2,column=1,padx=1,pady=1)
        label11.grid(row=2,column=2,padx=1,pady=1)
        label12.grid(row=2,column=3,padx=1,pady=1)
        label13.grid(row=3,column=0,padx=1,pady=1)
        label14.grid(row=3,column=1,padx=1,pady=1)
        label15.grid(row=3,column=2,padx=1,pady=1)
        label16.grid(row=3,column=3,padx=1,pady=1)
        next.grid(row=4, column=3,padx=1,pady=1)
        prev.grid(row=4, column=0,padx=1,pady=1)
        prev.grid(row=4, column=0,padx=1,pady=1)
        play.grid(row=4, column=1, columnspan=2 ,padx=1,pady=1)

        main_windows.mainloop()

if __name__ == '__main__':
    main()