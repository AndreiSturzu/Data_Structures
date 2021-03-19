class Stack:
    def __init__(self):
        self.s = []

    def push(self, element):
        if len(self.s) == 0:
            self.s.append(element)
        else:
            self.s = [element, *self.s]

    def pop(self):
        popped_element = self.s[0]
        self.s = self.s[1:]
        return popped_element

    def print_stack(self):
        print(self.s)

    def size(self):
        return len(self.s)


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push_back(self, element):
        self.s1.push(element)
        ops = [f'read({element}) push(1, {element})']
        return ops

    def pop_front(self):
        ops = []
        if self.s1.size() == 0:
            if self.s2.size() == 0:
                # print("Queue is empty")
                ops.append("Queue is empty")
            else:
                popped_element = self.s2.pop()
                ops.append(f'pop(2) write({popped_element})')
                # return popped_element
        elif self.s2.size() != 0:
            popped_element = self.s2.pop()
            ops.append(f'pop(2) write({popped_element})')
            # return popped_element
        else:
            while self.s1.size() != 1:
                popped_element = self.s1.pop()
                self.s2.push(popped_element)
                ops.append(f'pop(1) push(2, {popped_element})')

            popped_element = self.s1.pop()
            self.s2.push(popped_element)
            ops.append(f'pop(1)')

            popped_element = self.s2.pop()
            ops.append(f'write({popped_element})')
            # return popped_element
        return ops

    def print_queue(self):
        self.s1.print_stack()
        self.s2.print_stack()

q = Queue()

file = 'coada-2stive.txt'
with open(file, 'rt') as f:
    content = f.readlines()
    content = [line.strip('\n') for line in content]
    # print(content)
    num_operations = int(content[0])

with open('coada-2stive.out', 'wt') as f:
    for i in range(1, num_operations + 1):
        line = content[i].split('(')
        print(i , line)
        operation = line[0]
        try:
            element = int(line[1][0])
        except ValueError:
            element = None
        f.write(f'{i}: ')
        # print(operation, element)
        if operation == 'push_back':
            ops = q.push_back(element)
            line_to_write = " ".join(ops)
            f.write(line_to_write)
        else:
            ops = q.pop_front()
            line_to_write = " ".join(ops)
            f.write(line_to_write)
        f.write('\n')








