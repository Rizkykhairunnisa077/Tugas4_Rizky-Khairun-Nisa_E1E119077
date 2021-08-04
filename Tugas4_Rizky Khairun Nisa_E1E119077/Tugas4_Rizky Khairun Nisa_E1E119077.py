class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output = open(filename, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()

    ofile = open(filename, "r")
    k = ofile.readlines()
    for i in k:
        print(i.rstrip())

def is_matched(expr):
    lefty = "({[" 
    righty = ")}]" 
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c) 
        elif c in righty:
            if S.is_empty():
                return False 
            if righty.index(c) != lefty.index(S.pop()):
                return False 
    return S.is_empty()

mulai_looping = True

while mulai_looping :
    print("\nPilihan : \n 1. Reverse File \n 2. Matching Delimiters \n 3. Keluar")
    print()
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1 :
        nama_file = input("Masukkan Nama File Anda : ")
        reverse_file(nama_file + ".txt"))
    elif pilih == 2 :
        pernyataan = input("Masukkan Pernyataan : ")
        match = is_matched(pernyataan)
        if match :
            print("\nSemua delimiters telah sesuai")
        else :
            print("\nTerdapat delimiters yang tidak sesuai")
    else :
        break
