"""
File: my_drawing.py
Name: Ryan
----------------------
TODO: My drawing
"""


from campy.graphics.gcolor import GColor
from campy.graphics.gobjects import GRect, GLabel
from campy.graphics.gwindow import GWindow

from component.cloth import cloth_body, collar, fish_bone, cloth_strap, inner_cloth, cloth_bridging_line, cloth_shadow
from component.body import clavicle, behind_hair, neck, face, blush, eyes, mouth, eyebrow, hair, hair_decorate
from component.hat import hat, upper_teeth, lower_teeth

window = GWindow(600, 450, title='Gawr Gura')


def main():
    """
    Title:可愛就是正義 ("A")

    Gawr Gura is so cute.
    source:https://www.mirrormedia.com.tw/assets/images/20210705182358-a6daaee4513d72858cc6ae3d09e7dc0c-mobile.png
    """
    # ===========背景============
    bg = GRect(600, 450)
    bg.filled = True
    bg.fill_color = GColor(45, 45, 45)
    window.add(bg)
    # ===========背景============

    # ===========文字============
    label = GLabel("A", -30, 580)
    label.font = 'Helvetica-420-bold'
    label.color = GColor(255, 255, 255)
    window.add(label)
    # ===========文字============

    # ===========下半身============
    # 衣服本體
    cloth_body(window)

    # 衣服 衣領
    collar(window)

    # 魚骨
    fish_bone(window)

    # 衣服帶子
    cloth_strap(window)

    # 內層衣服
    inner_cloth(window)

    # 帽T橋接線
    cloth_bridging_line(window)

    # 鎖骨
    clavicle(window)

    # 衣服 陰影
    cloth_shadow(window)
    # ===========下半身============

    # ===========上半身============
    # 帽子本體
    hat(window)

    # 脖子旁邊的 深色頭髮
    behind_hair(window)

    # 脖子
    neck(window)

    # 帽子 下牙齒
    lower_teeth(window)

    # 臉
    face(window)

    # 腮紅
    blush(window)

    # 眼睛
    eyes(window)

    # 嘴巴
    mouth(window)

    # 眉毛
    eyebrow(window)

    # 頭髮
    hair(window)

    # 帽子 上牙齒
    upper_teeth(window)

    # 頭髮 裝飾
    hair_decorate(window)
    # ===========上半身============


if __name__ == '__main__':
    main()
