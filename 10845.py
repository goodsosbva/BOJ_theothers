import sys



def push(x):
    Queue.append(x)


# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if not Queue:
        return -1
    else:
        return Queue.pop(0)
    # else:
    #    return stack.pop()


# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    return len(Queue)


# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    return 0 if Queue else 1


# 스택의 가장 위에 있는 정수를 출력한다.
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def front():
    return Queue[0] if Queue else -1


def back():
    return Queue[-1] if Queue else -1


N = int(sys.stdin.readline().rstrip())
Queue = []

for i in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    command = input_split[0]
    # if i == 0:
    #    print(' ')

    if command == "push":
        push(input_split[1])
    elif command == "pop":
        print(pop())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())
