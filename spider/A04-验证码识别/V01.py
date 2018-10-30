'''
验证码识别 pytesseract
'''
import pytesseract as pt
from PIL import Image
import time

image = Image.open("03.png")
#image = Image.open("YM_01.png")
# 调用pytessreact,把图片转换成文字
time.sleep(4)
text = pt.image_to_string(image)
print(text)

