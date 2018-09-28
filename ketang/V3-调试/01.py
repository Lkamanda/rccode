def SayHello(name):
    print("i want to say hello with your,{0}".format(name))
    print("Hello,{0}".format(name))
    print("Done...")

if __name__ == '__main__':
    print('****'*10)

    name = input("please input your name:")

    print(SayHello(name = name))
    print('@@@'*10)
