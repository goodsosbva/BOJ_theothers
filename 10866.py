import sys
from collections import deque


def push_front(x):
    Queue.appendleft(x)


def push_back(x):
    Queue.append(x)


# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop_front():
    if not Queue:
        return -1
    else:
        return Queue.popleft()
    # else:
    #    return stack.pop()


def pop_back():
    if not Queue:
        return -1
    else:
        return Queue.pop()
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
Queue = deque()

for i in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    command = input_split[0]
    # if i == 0:
    #    print(' ')

    if command == "push_front":
        push_front(input_split[1])
    elif command == "push_back":
        push_back(input_split[1])
    elif command == "pop_front":
        print(pop_front())
    elif command == "pop_back":
        print(pop_back())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())
