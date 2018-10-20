'''
验证码识别 pytesseract
'''
import pytesseract as pt
from PIL import Image

image = Image.open("03.png")
# 调用pytessreact,把图片转换成文字
text = pt.image_to_string(image)
print(text)