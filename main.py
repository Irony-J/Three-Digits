import sys
import math
class digit:
    def __init__(self, previous, move, position):
        self.previous = previous
        self.digits = [0,0,0]
        if previous is not None:
            for i in range(3):
                self.digits[i] = previous.digits[i]
            self.digits[position] = self.digits[position] + move
            # if move == 100:
            #     self.digits[0] = self.digits[0] + 1
            #
            # elif move == -100:
            #     self.digits[0] = self.digits[0] - 1
            #
            # elif move == 10:
            #     self.digits[1] = self.digits[0] + 1
            #
            # elif move == -10:
            #     self.digits[1] = self.digits[1] - 1
            #
            # elif move == 1:
            #     self.digits[2] = self.digits[2] + 1
            #
            # elif move == -1:
            #     self.digits[2] = self.digits[2] - 1


        else:
            self.digits = [int(x) for x in str(move)]
        self.position = position

    def value(self):
        v = self.digits[0]*100 + self.digits[1]*10 + self.digits[2]*1
        return v


def read_file(file):
    f = open(file, 'r')
    # First line
    start = int(f.readline())
    # second line
    end = int(f.readline())
    # forbidden
    forbidden = [int(s) for s in f.readline().split(',') if s.isdigit()]

    f.close()
    return start, end, forbidden

def print_result(node,expanded):
    tmp = node
    path = []
    while tmp is not None:
        path.insert(0, tmp.value())
        tmp = tmp.previous

    for i in range(len(path)):
        if i != len(path) - 1:
            print('{},'.format(path[i]), end='')
        else:
            print(path[i])

    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].value()), end='')
        else:
            print(expanded[i].value())

def bfs():
    # TODO
    pass

def dfs(file):
    start, end, forbidden = read_file(file)
    print(start, end, forbidden)
    frindge = []
    expanded = []
    path = []

    init = digit(None, start, -1)
    frindge.insert(0, init)
    count = 0
    while frindge and count < 1000:
        count = count + 1
        curr = frindge.pop(0)
        print('curr',curr.digits)

        if curr not in expanded:
            expanded.append(curr)

        # Find the end
        if curr.value() == end:
            print_result(curr, expanded)
            quit()

        i = 2
        while i > -1:
            if curr.position != i:
                if curr.digits[i] != 9:
                    newnodea = digit(curr, +1, i)
                    if newnodea.value() not in forbidden:
                        frindge.insert(0, newnodea)
                if curr.digits[i] != 0:
                    newnode = digit(curr, -1, i)
                    if newnode.value() not in forbidden:
                        frindge.insert(0, newnode)
            i = i - 1




def ids():
    # TODO implement this method
    pass

def greedy():
    # TODO
    pass

def a_star():
    # TODO
    pass

def hill_climbling():
    # TODO
    pass

def main():
    mode = sys.argv[1]
    text_file = sys.argv[2]

    if mode == 'B':
        bfs()
    elif mode == 'D':
        dfs(text_file)
    elif mode == 'I':
        ids()
    elif mode == 'G':
        greedy()
    elif mode == 'A':
        a_star()
    elif mode == 'H':
        hill_climbling()
    else:
        print('Undefined mode!')




if __name__ == "__main__":
    main()
