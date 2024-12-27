import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import json
import argparse


# 定义一个函数，返回n的所有唯一因子对，其中第二个因子是偶数
def unique_factor_pairs(n):
    """返回n的所有唯一因子对，其中第二个因子是偶数。"""
    pairs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            pair = (i, n // i)
            if (n // i) % 2 == 0:
                pairs.append(pair)
    pairs.sort()
    return pairs


# 在给定的图像形状上绘制黑色圆圈，并保存图像和对应的因子对数据
def draw_black_circle_(shape, interval=60, w_index=0, h_index=0, fname="img"):
    """在给定的图像形状上绘制黑色圆圈。"""
    img_circle = np.uint8(np.ones([shape[1], shape[0], 3]) * 255)  # 创建白色背景图像
    w_data = unique_factor_pairs(shape[0])
    h_data = unique_factor_pairs(shape[1])

    # 确保索引在有效范围内
    w_index = min(w_index, len(w_data) - 1)
    h_index = min(h_index, len(h_data) - 1)

    w_num, w_pixel = w_data[w_index]
    h_num, h_pixel = h_data[h_index]
    radius = max(min(w_pixel, h_pixel) - interval, 0) // 2

    # 根据因子对绘制圆圈
    for row in range(w_num):
        for col in range(h_num):
            left = row * w_pixel
            top = col * h_pixel
            center_x = left + w_pixel // 2
            center_y = top + h_pixel // 2
            cv.circle(img_circle, (center_x, center_y), radius, (0, 0, 0), -1)

    # 保存图像和因子对数据
    cv.imwrite(f"{fname}.jpg", img_circle)
    circle_data = {"w": w_data[w_index], "h": h_data[h_index]}
    with open(f"{fname}.json", 'w') as f:
        json.dump(circle_data, f)

    return img_circle, circle_data


# 设置命令行参数解析器
def get_parser():
    parser = argparse.ArgumentParser(description='生成circle图像。')
    parser.add_argument("--s", type=int, nargs='+', default=None, help="图像分辨率")
    parser.add_argument("--n", type=str, default="circle", help="文件名")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # 解析命令行参数
    args = get_parser()
    shape = args.s  # 图像形状
    fname = args.n  # 文件名

    # 创建主窗口
    root = tk.Tk()
    root.title("Slider Example with Two Scales and Image Update")

    # 获取因子对列表
    w_data = unique_factor_pairs(shape[0])
    h_data = unique_factor_pairs(shape[1])
    w_num_max = len(w_data) - 1
    h_num_max = len(h_data) - 1

    # 创建滑块控件，用于选择宽度和高度因子对的索引，以及间隔
    slider_a = tk.Scale(root, from_=0, to=w_num_max, orient=tk.HORIZONTAL, label="Slider A (Width Index)")
    slider_a.pack()

    slider_b = tk.Scale(root, from_=0, to=h_num_max, orient=tk.HORIZONTAL, label="Slider B (Height Index)")
    slider_b.pack()

    slider_c = tk.Scale(root, from_=10, to=50, orient=tk.HORIZONTAL, label="Slider C (Interval Index)")
    slider_c.pack()

    text = tk.Text(root)
    text.pack()

    # 初始显示空白图像
    zero_img = np.zeros([shape[1], shape[0], 3], dtype=np.uint8)
    pil_img = Image.fromarray(zero_img, mode='RGB')
    blank_photo = ImageTk.PhotoImage(pil_img)

    image_label = tk.Label(root, image=blank_photo)
    image_label.pack()


    # 定义更新图片的函数，根据滑块值重新绘制图像
    def update_result(*args):
        a_value = int(slider_a.get())
        b_value = int(slider_b.get())
        c_value = int(slider_c.get())

        # 绘制图像并获取结果
        image, data = draw_black_circle_(shape=shape, w_index=a_value, h_index=b_value, interval=c_value, fname=fname)

        # 将NumPy数组转换为PIL图像，再转换为PhotoImage
        image_pil = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(image_pil)

        # 更新文本框内容
        text.insert(tk.END, f"w:{w_data[a_value][0]}, h:{h_data[b_value][0]} ")

        # 更新Label控件的图片
        image_label.config(image=photo)
        image_label.image = photo  # 保持对PhotoImage对象的引用


    # 绑定滑块事件
    slider_a.config(command=update_result)
    slider_b.config(command=update_result)
    slider_c.config(command=update_result)

    # 进入主事件循环
    root.mainloop()