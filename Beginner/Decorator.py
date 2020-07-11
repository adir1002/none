def logger(func):
    def inner (a):
        print("11111111111111111111")
        func()
        print(a)
        print("2222222222222222")
    return inner

@logger
def sample():
    print("inside")

sample(12)
