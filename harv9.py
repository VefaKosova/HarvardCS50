while True:
    n=int(input("What's n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")


def main():
    number = get_number()
    print(number)
    meow(3)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n>0:
            break
    return n
    

def meow(n):
    for _ in range(n):
        print("meow")


main()
  