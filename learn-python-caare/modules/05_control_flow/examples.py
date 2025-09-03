# Control Flow — Examples

def loop_else_demo(n):
    for i in range(n):
        if i == -1:  # never true; else will execute
            break
    else:
        print("Loop completed without break.")

def comprehensions():
    squares = [x*x for x in range(6) if x % 2 == 0]
    print("Even squares:", squares)

if __name__ == "__main__":
    loop_else_demo(5)
    comprehensions()
