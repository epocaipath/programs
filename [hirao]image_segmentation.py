#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 課題6,7 (opencvでの切り取りを実施)

# 保存していたpng画像を読み込む
im = cv2.imread('Tumor.png')

# 切り取りの処理速度を計測
import time
start_time=time.time()

# 切り取るサイズ
x = 1000 
y = 1000

# 画像サイズ
img_x = im.shape[1]
img_y = im.shape[0]

# 画像切り取り用の関数(切る幅は引数で設定)
def img_cut(x_csize,y_csize):
    # 画像サイズのyをy軸の切り取り幅で割ったものに+1した回数繰り返す。(例: 画像のy=30を8ずつ切りたい場合=> 30/8 +1 = 4回)
    for i in range(int(img_y / y_csize)+1):
        # 画像サイズのxをx軸の切り取り幅で割ったものに+1した回数繰り返す。(例: 画像のx=20を8ずつ切りたい場合=> 20/8 +1 = 3回)
        for j in range(int(img_x / x_csize)+1):
            # x,y両方向において切り取り幅x(i+1)及び(i+1)がそれぞれ画像のx方向及びy方向サイズよりも大きくなった場合は、それぞれ末尾のx,yを画像のx,yサイズとする。
            if x_csize*(j+1) >= img_x and y_csize*(i+1) >= img_y:
                img1 = im[y_csize*i:img_y, x_csize*j:img_x]
            # x方向の切り取り幅×(j+1)が画像のx方向のサイズ以上の場合は、切り取りの末尾のxを画像のx方向サイズにする。            
            elif x_csize*(j+1) >= img_x:
                img1 = im[y_csize*i:y_csize*(i+1), x_csize*j:img_x]
            # y方向の切り取り幅×(i+1)が画像のy方向のサイズ以上の場合は、切り取りの末尾のyを画像のy方向サイズにする。            
            elif y_csize*(i+1) >= img_y:
                img1 = im[y_csize*i:img_y,x_csize*j:x_csize*(j+1)]
            # 上記のどちらにも該当しなければ、x_csize,y_csizeに従って画像を左上端から右方向へ、下の段に降りて再度左端から右方向へと切り取っていく。           
            else:
                img1=im[y_csize*i:y_csize*(i+1),x_csize*j:x_csize*(j+1)]

            cv2.imwrite(f"tumor[{j}x{i}].jpg",img1)

# x×yサイズで切り取り
img_cut(x,y) 

process_time = time.time()-start_time
print(process_time)

