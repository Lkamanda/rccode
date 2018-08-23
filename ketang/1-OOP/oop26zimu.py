
class getTuxing():
    # 打印字母A
    def getA(self):
        for i in range(1,6):
            for k in range(6-i):
                print(' ',end='')
            for j in range(1,i+1):
                if i==1 or i==3 or j==1 or j==i:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
    # 打印字母B
    def getB(self):
        for i in range(1,8):
            for j in range(1,4):
                if i == 1 or i==4 or i ==7 or j==1:
                    if j<3:
                        print('*',end=' ')
                elif j==3:
                    if i ==3 or i==2 or i==6 or i ==5:
                        print('*',end=' ')
                else:
                    print(' ', end=' ')
            print()

    #打印字母C
    def getC(self):
        for i in range(1,5):
            for j in range(1,4):
                if (i ==1 or i==4) and (j==2 or j==3 ):
                    print('*', end=' ')
                elif (i==2 or i==3) and j==1:
                    print('*',end=' ')
                else:
                    print(' ', end='')
            print()



    # 打印字母D
    def getD(self):
        for i in range(1,5):
            for j in range(1,4):
                if  i ==1 or i==4 or j==1 :
                    if j<3:
                        print('*',end=' ')
                elif j ==3:
                    if i ==2 or i==3:
                        print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

    # def getSr(self):

if __name__ == '__main__':
    a = getTuxing()
    a.getD()
    print('#'*10)
    a.getC()
