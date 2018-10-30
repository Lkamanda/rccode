#一次清除黑点
from PIL import Image
def fall ():
    white = (255,255,255,255)
    black = (0,0,0,255)
    img = Image.open('YM_01.png') # 读入图片
    pixdata = img.load()
    X = img.size[0]-1#因为我校的验证码二值化后正好剩下一圈宽度为一像素的白边，所以这么处理了
    Y = img.size[1]-1

    def icolor(RGBA):
        if RGBA == white:
            return(1)
        else:
            return(0)

    for y in range(Y):
        for x in range(X):
            if (x<1 or y<1):
                pass
            else:
                if icolor(pixdata[x,y]) == 1:
                    pass
                else:
                    if (
                         icolor(pixdata[x+1,y])+
                         icolor(pixdata[x,y+1])+
                         icolor(pixdata[x-1,y])+
                         icolor(pixdata[x,y-1])+
                         icolor(pixdata[x-1,y-1])+
                         icolor(pixdata[x+1,y-1])+
                         icolor(pixdata[x-1,y+1])+
                         icolor(pixdata[x+1,y+1])
                         )>5:
                         #如果一个黑色像素周围的8个像素中白色像素数量大于5个，则判断其为噪点，填充为白色
                        pix[x,y] = white

#填充白点
    for y in range(Y):
        for x in range(X):
            if (x<1 or y<1):
                pass
            else:
                if icolor(pixdata[x,y]) == 0:
                    pass
                else:
                    if (
                         (icolor(pixdata[x+1,y]))+
                         (icolor(pixdata[x,y+1]))+
                         (icolor(pixdata[x-1,y]))+
                         (icolor(pixdata[x,y-1]))
                         )<2:
                         #如果一个白色像素上下左右4个像素中黑色像素的个数大于2个，则判定其为有效像素，填充为黑色。
                        pix[x,y] = black
#二次去除黑点
    for y in range(Y):
        for x in range(X):
            if (x<1 or y<1):
                pass
            else:
                if icolor(pixdata[x,y]) == 1:
                    pass
                else:
                    if (
                         icolor(pixdata[x+1,y])+
                         icolor(pixdata[x,y+1])+
                         icolor(pixdata[x-1,y])+
                         icolor(pixdata[x,y-1])
                         )>2:
                        pix[x,y] = white
    img.save('jz.png', "png")
if __name__ == '__main__':
    fall()