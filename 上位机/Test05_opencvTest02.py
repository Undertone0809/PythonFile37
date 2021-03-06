# DelelopmentTime: 2020/11/23  20:34
#这是一个调用笔记本内置相机的模块

'''
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import cv2
# 引入库
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    # 读取内容
    if cv2.waitKey(10) == ord("q"):
        break

# 随时准备按q退出
cap.release()
cv2.destroyAllWindows()
# 停止调用，关闭窗口

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————
'''

# import numpy as np
# import cv2

# camera_number = 0
# cap = cv2.VideoCapture( camera_number + cv2.CAP_DSHOW)

# # define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     # write the flipped frame
#     out.write(frame)
#     cv2.imshow('image',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     else:
#         break

# # release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()


import numpy as np
import cv2

camera_number = 0
cap = cv2.VideoCapture(camera_number + cv2.CAP_DSHOW)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

import cv2
import os

# 引入库

print("=============================================")
print("=  热键(请在摄像头的窗口使用)：             =")
print("=  z: 更改存储目录                          =")
print("=  x: 拍摄图片                              =")
print("=  q: 退出                                  =")
print("=============================================")
# 提醒用户操作字典

class_name = input("请输入存储目录：")
while os.path.exists(class_name):
    class_name = input("目录已存在！请输入存储目录：")
os.mkdir(class_name)
# 存储

index = 1
cap = cv2.VideoCapture(0)
width = 640
height = 480
w = 360
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
crop_w_start = (width - w) // 2
crop_h_start = (height - w) // 2
print(width, height)
# 设置特定值

while True:
    ret, frame = cap.read()

    frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]
    # 没理解？

    frame = cv2.flip(frame, 1, dst=None)
    # 镜像显示
    cv2.imshow("capture", frame)
    # 显示

    input = cv2.waitKey(1) & 0xFF
    if input == ord('z'):
        class_name = input("请输入存储目录：")
        while os.path.exists(class_name):
            class_name = input("目录已存在！请输入存储目录：")
        os.mkdir(class_name)
    # 存储

    elif input == ord('x'):
        cv2.imwrite("%s/%d.jpeg" % (class_name, index),
                    cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA))
        print("%s: %d 张图片" % (class_name, index))
        index += 1
    # ？
    if input == ord('q'):
        break
    # 退出

cap.release()
cv2.destroyAllWindows()
