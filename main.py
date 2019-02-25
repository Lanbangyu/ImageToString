from PIL import Image

coedLib =  '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''#生成字符画所需的字符集
count = len(coedLib)

def transform1(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数“L”表示黑白模式
    codePic = ''
    for h in range(0,image_file.size[1]): #size属性表示图片分辨率,'0'为横向大小，‘1’为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果打开的图像是多层次的图片，那就
                                            #返回一个元组
            codePic = codePic + coedLib[int(((count-1)*gray)/256)]      #建立灰度与字符集的映射
        codePic = codePic +'\r\n'
    return codePic

fp = open('表情包.jpg','rb')
image_file = Image.open(fp)
print(u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)
image_file = image_file.resize((int(image_file.size[0]),int(image_file.size[1]*0.3)))
print(u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)

tmp = open('tmp.txt','w')
tmp.write(transform1(image_file))
tmp.close()
