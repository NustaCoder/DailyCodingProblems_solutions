# enter value using push
# retrive right end value using pull
# retrive left end value using pop


def push_one(lst, val):
    lst.append(val)


def pull_one(lst):
    return lst.pop(0)


def pop_one(lst):
    return lst.pop(-1)


lst = [i for i in range(100)]
while True:
    print("enter the operation")
    print("1.push\t2.pop\t3.pull")
    op = int(input())

    if op == 1:
        print("\nenter the value")
        val = int(input())
        push_one(lst, val)
        print(lst)
    elif op == 2:
        val = pop_one(lst)
        print(val)
    elif op == 3:
        val = pull_one(lst)
        print(val)
    else:
        break
