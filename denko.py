from PIL import Image,ImageDraw,ImageFont
import time
import threading

def make_lightmap(image):
    pixels = image.getdata()
    lightmap = ""
    for pixel in pixels:
        if pixel < 200:
            lightmap += "◆ "
        else:
            lightmap += "　 "
    return lightmap

def make_denko(str_list):
    denko = []
    font = ImageFont.truetype('msgothic.ttc', 40) #"C:\Windows\Fonts"内の（もしくはパスから書いて）お好きなフォントで #エラーが出なければこのままでOK
    for i in str_list:
        im = Image.new("L",(40,40),"white") #空の白地画像の作成
        mozi = ImageDraw.Draw(im)
        mozi.text((0,0),i,font=font) #文字入れ

        # im.show()

        lightmap = make_lightmap(im)
        j = 0
        gyou = ""
        for light in lightmap:
            j += 1
            gyou += light
            if j == 80:
                j = 0
                denko.append(gyou)
                gyou = ""

        denko.append("\n" + "\n" + "\n" + "\n")

    return denko

def check_key():
    check = input()

str = input("文字を入力：")
denko = make_denko(str)
# print(type(denko))
t = threading.Thread(target=check_key)
t.start()
while True:
    for i in denko:
        print(i)
        if not t.is_alive():
            break
        time.sleep(0.04)
    if not t.is_alive():
        break
    for i in range(0,30):
        print("\n")
        time.sleep(0.04)