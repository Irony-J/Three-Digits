import sys
import math
class digit:
    def __init__(self, previous, move, position, depth=0, heuristic=0, order=0):
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
            self.digits[0] = math.floor(move / 100)
            self.digits[1] = math.floor((move % 100) / 10)
            self.digits[2] = math.floor(move % 10)


        self.position = position
        self.depth = depth
        self.heuristic = heuristic
        self.order = order

    def __eq__(self, other):
        return (self.value() == other.value()) and ((self.position == other.position))

    def update_heuristic(self, end):
        self.heuristic = math.fabs(self.digits[0] - math.floor(end / 100)) + math.fabs(self.digits[1] - math.floor((end % 100) / 10)) + math.fabs(self.digits[2] - math.floor(end % 10))

    def value(self):
        v = self.digits[0]*100 + self.digits[1]*10 + self.digits[2]*1
        return v

    def print_value(self):
        str = '{}{}{}'.format(self.digits[0], self.digits[1], self.digits[2])
        return str


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
        path.insert(0, tmp.print_value())
        tmp = tmp.previous

    for i in range(len(path)):
        if i != len(path) - 1:
            print('{},'.format(path[i]), end='')
        else:
            print(path[i])

    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].print_value()), end='')
        else:
            print(expanded[i].print_value())

def expanded_detect(expanded):

    for i in range(1,len(expanded)):
        print('{}, previous:{} position:{}'.format(expanded[i].print_value(), expanded[i].previous.print_value(), expanded[i].position))

def bfs(file):
    start, end, forbidden = read_file(file)
    # print(start, end, forbidden)
    frindge = []
    expanded = []
    path = []

    init = digit(None, start, -1)
    frindge.insert(0, init)
    count = 0
    while frindge and count < 1000:
        count = count + 1
        curr = frindge.pop(0)

        # print('curr:', curr.print_value())
        if curr not in expanded:
            expanded.append(curr)

            # Find the end
            if curr.value() == end:
                print_result(curr, expanded)
                # expanded_detect(expanded)
                quit()
            
            i = 0
            while i < 3:
                if curr.position != i:
                    if curr.digits[i] != 0:
                        newnode = digit(curr, -1, i)
                        if newnode.value() not in forbidden:
                            frindge.append(newnode)
                    if curr.digits[i] != 9:
                        newnodea = digit(curr, +1, i)
                        if newnodea.value() not in forbidden:
                            frindge.append(newnodea)
            
                i = i + 1

    print('No solution found.')
    # Print expanded
    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].print_value()), end='')
        else:
            print(expanded[i].print_value())



def dfs(file):
    start, end, forbidden = read_file(file)
    # print(start, end, forbidden)
    frindge = []
    expanded = []
    path = []

    init = digit(None, start, -1)
    frindge.insert(0, init)
    count = 0
    while frindge and count < 1000:
        count = count + 1
        curr = frindge.pop(0)

        print('curr:', curr.digits)
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
                            # print('new:', newnodea.digits)
                            frindge.insert(0, newnodea)
                    if curr.digits[i] != 0:
                        newnode = digit(curr, -1, i)
                        if newnode.value() not in forbidden:
                            # print('new:', newnode.digits)
                            frindge.insert(0, newnode)
                i = i - 1

    print('No solution found.')
    # Print expanded
    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].print_value()), end='')
        else:
            print(expanded[i].print_value())





def ids(file):
    start, end, forbidden = read_file(file)
    # print(start, end, forbidden)
    frindge = []
    expanded = []
    total_expanded = []
    path = []
    depth_limit = 0

    count = 0
    while count < 1000:

        init = digit(None, start, -1, 1)
        frindge = []
        expanded = []
        frindge.insert(0, init)
        depth_limit = depth_limit + 1


        while frindge:

            count = count + 1
            curr = frindge.pop(0)
            depth = curr.depth

            if count > 1000:
                print('No solution found.')
                # Print expanded
                for i in range(len(total_expanded)):
                    if i != len(total_expanded) - 1:
                        print('{},'.format(total_expanded[i].print_value()), end='')
                    else:
                        print(total_expanded[i].print_value())
                quit()

            if depth > depth_limit:
                continue
            if curr not in expanded:
                expanded.append(curr)
            total_expanded.append(curr)

            # Find the end
            if curr.value() == end:
                print_result(curr, total_expanded)
                quit()

            i = 2
            while i > -1:
                if curr.position != i:
                    if curr.digits[i] != 9:
                        newnodea = digit(curr, +1, i, depth + 1)
                        if newnodea.value() not in forbidden:
                            frindge.insert(0, newnodea)
                    if curr.digits[i] != 0:
                        newnode = digit(curr, -1, i, depth + 1)
                        if newnode.value() not in forbidden:
                            frindge.insert(0, newnode)
                i = i - 1


def greedy(file):
    start, end, forbidden = read_file(file)
    # print(start, end, forbidden)
    frindge = []
    expanded = []
    path = []
    order = 0

    init = digit(None, start, -1, order=order)
    init.update_heuristic(end)

    frindge.insert(0, init)
    count = 0
    while frindge and count < 1000:
        count = count + 1
        frindge.sort(key=lambda x: (x.heuristic, x.order), reverse=False)
        curr = frindge.pop(0)
        # print('curr:{}, h():{}'.format(curr.value(), curr.heuristic))

        if curr not in expanded:
            expanded.append(curr)

        # Find the end
        if curr.value() == end:
            print_result(curr, expanded)
            quit()

        i = 0
        while i < 3:
            if curr.position != i:
                if curr.digits[i] != 0:
                    newnode = digit(curr, -1, i, order=order-1)
                    newnode.update_heuristic(end)
                    if newnode.value() not in forbidden:
                        order = order - 1
                        frindge.append(newnode)
                if curr.digits[i] != 9:
                    newnodea = digit(curr, +1, i, order=order-1)
                    newnodea.update_heuristic(end)
                    if newnodea.value() not in forbidden:
                        order = order - 1
                        frindge.append(newnodea)

            i = i + 1

    print('No solution found.')
    # Print expanded
    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].print_value()), end='')
        else:
            print(expanded[i].print_value())

def a_star(file):
    start, end, forbidden = read_file(file)
    # print(start, end, forbidden)
    frindge = []
    expanded = []
    path = []
    order = 0
    depth = 0

    init = digit(None, start, -1, depth=depth, order=order)
    init.update_heuristic(end)

    frindge.insert(0, init)
    count = 0
    while frindge and count < 1000:
        count = count + 1
        frindge.sort(key=lambda x: (x.heuristic + x.depth, x.order), reverse=False)
        curr = frindge.pop(0)
        # print('curr:{}, h():{}, depth:{}'.format(curr.value(), curr.heuristic, curr.depth))

        if curr not in expanded:
            expanded.append(curr)

        # Find the end
        if curr.value() == end:
            print_result(curr, expanded)
            quit()

        i = 0
        while i < 3:
            if curr.position != i:
                if curr.digits[i] != 0:
                    newnode = digit(curr, -1, i, depth=depth+1, order=order-1)
                    newnode.update_heuristic(end)
                    if newnode.value() not in forbidden:
                        order = order - 1
                        frindge.append(newnode)
                if curr.digits[i] != 9:
                    newnodea = digit(curr, +1, i, depth=depth+1, order=order-1)
                    newnodea.update_heuristic(end)
                    if newnodea.value() not in forbidden:
                        order = order - 1
                        frindge.append(newnodea)

            i = i + 1
        depth = depth + 1

    print('No solution found.')
    # Print expanded
    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].print_value()), end='')
        else:
            print(expanded[i].print_value())

def hill_climbling(file):
    start, end, forbidden = read_file(file)
    # print(start, end, forbidden)
    frindge = []
    expanded = []
    path = []
    order = 0
    depth = 0

    init = digit(None, start, -1, depth=depth, order=order)
    init.update_heuristic(end)
    best = init.heuristic
    curr_best = best

    frindge.insert(0, init)
    count = 0
    while frindge and count < 1000:
        count = count + 1
        frindge.sort(key=lambda x: (x.heuristic, x.order), reverse=False)
        curr = frindge.pop(0)
        # print('curr:{}, h():{}, depth:{}'.format(curr.value(), curr.heuristic, curr.depth))
        frindge.clear()

        if curr not in expanded:
            expanded.append(curr)

        # Find the end
        if curr.value() == end:
            print_result(curr, expanded)
            quit()

        i = 0
        while i < 3:
            if curr.position != i:
                if curr.digits[i] != 0:
                    newnode = digit(curr, -1, i, order=order-1)
                    newnode.update_heuristic(end)
                    if newnode.value() not in forbidden and newnode.heuristic <= best:
                        best = newnode.heuristic
                        order = order - 1
                        frindge.append(newnode)
                if curr.digits[i] != 9:
                    newnodea = digit(curr, +1, i, order=order-1)
                    newnodea.update_heuristic(end)
                    if newnodea.value() not in forbidden and newnodea.heuristic <= best:
                        best = newnodea.heuristic
                        order = order - 1
                        frindge.append(newnodea)

            i = i + 1

    print('No solution found.')
    # Print expanded
    for i in range(len(expanded)):
        if i != len(expanded) - 1:
            print('{},'.format(expanded[i].print_value()), end='')
        else:
            print(expanded[i].print_value())

def main():
    mode = sys.argv[1]
    text_file = sys.argv[2]

    if mode == 'B':
        bfs(text_file)
    elif mode == 'D':
        dfs(text_file)
    elif mode == 'I':
        ids(text_file)
    elif mode == 'G':
        greedy(text_file)
    elif mode == 'A':
        a_star(text_file)
    elif mode == 'H':
        hill_climbling(text_file)
    else:
        print('Undefined mode!')

if __name__ == "__main__":
    main()
