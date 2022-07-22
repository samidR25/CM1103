import time
def f(p):
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(1)
    return p

def g(p):
    return p

print(f(True) and g(True))
