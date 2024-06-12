def say_hello():
    print("Hello!")

def repeat(say_hello, n):
    for _ in range(n):
        say_hello()