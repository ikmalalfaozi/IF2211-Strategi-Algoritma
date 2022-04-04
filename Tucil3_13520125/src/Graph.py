class Node:
    def __init__(self, parent, puzzle, child, level, cost, blank, previous_step):
        self.parent = parent
        self.puzzle = puzzle
        self.child = child
        self.level = level
        self.cost = cost
        self.blank = blank # (x, y) blank puzzle
        self.previous_step = previous_step
    
    def show(self):
    # Menampilkan puzzle
        for row in self.puzzle:
            for col in row:
                if (col != 16):
                    if (col < 10):
                        print(col,end='   ')
                    else:
                        print(col, end='  ')
                else:
                    print('  ', end='  ')
            print()
    
    def isGoal(self):
    # Memeriksa apakah node merupakan goal state
        goal = True
        i = 0
        while (i < 4 and goal):
            j = 0
            while (j < 4 and goal):
                if (self.puzzle[i,j] != i*4 + j + 1):
                    goal = False
                j += 1
            i += 1
        return goal

class LiveNodeArray:
    def __init__(self, array, length):
        self.array = array
        self.length = length   

    def append(self, s):
    # Menambahkan simpul s ke dalam array berdasarkan prioritasnya (cost)
        found = False
        i = 0
        while (not found and i < self.length):
            if (self.array[i].cost >= s.cost):
                found = True
            else:
                i += 1
        self.array.insert(i, s)
        self.length += 1
    
    def pop(self):
    # Menghapus dan mengembalikan elemen pertama array
        first = self.array[0]
        self.array = self.array[1:]
        self.length -= 1
        return first
    
    def display(self):
    # Menampilkan seluruh isi array
        for i in range(self.length):
            self.array[i].show()
            print(self.array[i].cost)
            print()