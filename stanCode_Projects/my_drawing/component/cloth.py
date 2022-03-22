from campy.graphics.gcolor import GColor
from campy.graphics.gobjects import GPolygon, GArc, GOval, GLine


def cloth_body(window):
    # 衣服
    lower_cloth = GPolygon()
    lower_cloth.add_vertex((301, 256))
    lower_cloth.add_vertex((296, 260))
    lower_cloth.add_vertex((293, 268))
    lower_cloth.add_vertex((289, 281))
    lower_cloth.add_vertex((286, 296))
    lower_cloth.add_vertex((282, 311))
    lower_cloth.add_vertex((277, 336))
    lower_cloth.add_vertex((268, 375))
    lower_cloth.add_vertex((264, 397))
    lower_cloth.add_vertex((258, 420))
    lower_cloth.add_vertex((246, 448))
    lower_cloth.add_vertex((535, 449))
    lower_cloth.add_vertex((525, 426))
    lower_cloth.add_vertex((524, 419))
    lower_cloth.add_vertex((520, 407))
    lower_cloth.add_vertex((517, 390))
    lower_cloth.add_vertex((513, 370))
    lower_cloth.add_vertex((506, 337))
    lower_cloth.add_vertex((500, 309))
    lower_cloth.add_vertex((496, 290))
    lower_cloth.add_vertex((490, 268))
    lower_cloth.add_vertex((486, 262))
    lower_cloth.add_vertex((484, 259))
    lower_cloth.filled = True
    lower_cloth.fill_color = GColor(42, 106, 155)
    lower_cloth.color = GColor(42, 106, 155)
    window.add(lower_cloth)

    # 左手線
    left_arm = GPolygon()
    left_arm.add_vertex((314, 301))
    left_arm.add_vertex((315, 331))
    left_arm.add_vertex((314, 349))
    left_arm.add_vertex((312, 367))
    left_arm.add_vertex((308, 381))
    left_arm.add_vertex((305, 394))
    left_arm.add_vertex((301, 408))
    left_arm.add_vertex((298, 422))
    left_arm.add_vertex((295, 437))
    left_arm.add_vertex((294, 447))
    left_arm.add_vertex((293, 448))
    left_arm.add_vertex((294, 439))
    left_arm.add_vertex((297, 427))
    left_arm.add_vertex((300, 416))
    left_arm.add_vertex((302, 401))
    left_arm.add_vertex((304, 396))
    left_arm.add_vertex((307, 386))
    left_arm.add_vertex((310, 378))
    left_arm.add_vertex((310, 373))
    left_arm.add_vertex((313, 362))
    left_arm.add_vertex((313, 352))
    left_arm.add_vertex((314, 341))
    left_arm.add_vertex((315, 317))
    left_arm.color = GColor(28, 79, 126)
    window.add(left_arm)
    # 右手線
    right_arm = GPolygon()
    right_arm.add_vertex((473, 303))
    right_arm.add_vertex((474, 321))
    right_arm.add_vertex((476, 336))
    right_arm.add_vertex((476, 347))
    right_arm.add_vertex((477, 367))
    right_arm.add_vertex((476, 356))
    right_arm.add_vertex((476, 341))
    # right_arm.add_vertex((476, 329))
    right_arm.add_vertex((475, 327))
    right_arm.add_vertex((474, 309))
    right_arm.filled = True
    right_arm.fill_color = GColor(28, 79, 126)
    right_arm.color = GColor(28, 79, 126)
    window.add(right_arm)

    # 衣服 鯊魚嘴
    cloth_shark_mouse = GPolygon()
    cloth_shark_mouse.add_vertex((477, 368))
    cloth_shark_mouse.add_vertex((461, 376))
    cloth_shark_mouse.add_vertex((440, 389))
    cloth_shark_mouse.add_vertex((414, 407))
    cloth_shark_mouse.add_vertex((382, 433))
    cloth_shark_mouse.add_vertex((363, 450))
    cloth_shark_mouse.add_vertex((485, 450))
    cloth_shark_mouse.add_vertex((484, 426))
    cloth_shark_mouse.add_vertex((482, 397))
    cloth_shark_mouse.filled = True
    cloth_shark_mouse.fill_color = GColor(191, 85, 76)#(206, 89, 79)#(205, 85, 76)  # 紅色
    cloth_shark_mouse.color = GColor(28, 79, 126)#(206, 89, 79)
    window.add(cloth_shark_mouse)

    # 牙齒下的影子
    teeth_shadow2 = GPolygon()
    teeth_shadow2.add_vertex((481, 393))
    teeth_shadow2.add_vertex((463, 382))
    teeth_shadow2.add_vertex((459, 410))
    teeth_shadow2.add_vertex((427, 403))
    teeth_shadow2.add_vertex((421, 434))
    teeth_shadow2.add_vertex((388, 433))
    teeth_shadow2.add_vertex((383, 449))
    teeth_shadow2.add_vertex((386, 450))
    teeth_shadow2.add_vertex((385, 449))
    teeth_shadow2.add_vertex((389, 435))
    teeth_shadow2.add_vertex((421, 438))
    teeth_shadow2.add_vertex((427, 405))
    teeth_shadow2.add_vertex((457, 415))
    teeth_shadow2.add_vertex((462, 383))
    teeth_shadow2.add_vertex((481, 400))
    teeth_shadow2.filled = True
    teeth_shadow2.fill_color = GColor(130, 44, 42)
    teeth_shadow2.color = GColor(130, 44, 42)
    window.add(teeth_shadow2)

    # 衣服 鯊魚牙齒
    cloth_shark_teeth = GPolygon()
    cloth_shark_teeth.add_vertex((477, 368))
    cloth_shark_teeth.add_vertex((461, 376))
    cloth_shark_teeth.add_vertex((440, 389))
    cloth_shark_teeth.add_vertex((414, 407))
    cloth_shark_teeth.add_vertex((382, 433))
    cloth_shark_teeth.add_vertex((363, 450))
    cloth_shark_teeth.add_vertex((386, 450))
    cloth_shark_teeth.add_vertex((390, 434))
    cloth_shark_teeth.add_vertex((424, 437))
    cloth_shark_teeth.add_vertex((429, 407))
    cloth_shark_teeth.add_vertex((461, 413))
    cloth_shark_teeth.add_vertex((463, 383))
    cloth_shark_teeth.add_vertex((482, 397))
    cloth_shark_teeth.filled = True
    cloth_shark_teeth.fill_color = GColor(255, 255, 255)  # 紅色
    cloth_shark_teeth.color = GColor(130, 44, 42)
    window.add(cloth_shark_teeth)

    # 牙齒上的影子
    teeth_shadow = GPolygon()
    teeth_shadow.add_vertex((477, 370))
    teeth_shadow.add_vertex((476, 367))
    teeth_shadow.add_vertex((464, 373))
    teeth_shadow.add_vertex((442, 385))
    teeth_shadow.add_vertex((421, 398))
    teeth_shadow.add_vertex((402, 413))
    teeth_shadow.add_vertex((387, 425))
    teeth_shadow.add_vertex((378, 435))
    teeth_shadow.add_vertex((363, 449))
    teeth_shadow.add_vertex((367, 449))
    teeth_shadow.add_vertex((380, 437))
    teeth_shadow.add_vertex((398, 422))
    teeth_shadow.add_vertex((418, 407))
    teeth_shadow.add_vertex((430, 399))
    teeth_shadow.add_vertex((440, 392))
    teeth_shadow.add_vertex((447, 389))
    teeth_shadow.add_vertex((459, 381))
    teeth_shadow.add_vertex((468, 377))
    teeth_shadow.add_vertex((478, 374))
    teeth_shadow.filled = True
    teeth_shadow.fill_color = GColor(40, 54, 70)
    teeth_shadow.color = GColor(53, 57, 60)
    window.add(teeth_shadow)


def cloth_bridging_line(window):
    # 帽T橋接線? (右)
    cloth_right_bridge_line = GArc(95, 85, 93, 77, x=400, y=277)
    cloth_right_bridge_line.color = (205, 179, 112)
    window.add(cloth_right_bridge_line)

    # 帽T橋接線? (左)
    cloth_left_bridge_line = GArc(95, 85, 15, 76, x=370, y=277)
    cloth_left_bridge_line.color = (205, 179, 112)
    window.add(cloth_left_bridge_line)


# 衣服 陰影
def cloth_shadow(window):
    # 左側身體陰影3
    left_cloth_shadow3 = GPolygon()
    left_cloth_shadow3.add_vertex((316, 300))
    left_cloth_shadow3.add_vertex((322, 301))
    left_cloth_shadow3.add_vertex((320, 307))
    left_cloth_shadow3.add_vertex((324, 317))
    left_cloth_shadow3.add_vertex((328, 323))
    left_cloth_shadow3.add_vertex((333, 333))
    left_cloth_shadow3.add_vertex((335, 341))
    left_cloth_shadow3.add_vertex((336, 352))
    left_cloth_shadow3.add_vertex((336, 361))
    left_cloth_shadow3.add_vertex((335, 369))
    left_cloth_shadow3.add_vertex((332, 381))
    left_cloth_shadow3.add_vertex((332, 391))
    left_cloth_shadow3.add_vertex((332, 409))
    left_cloth_shadow3.add_vertex((330, 429))
    left_cloth_shadow3.add_vertex((330, 436))
    left_cloth_shadow3.add_vertex((330, 445))
    left_cloth_shadow3.add_vertex((330, 447))
    left_cloth_shadow3.add_vertex((297, 448))
    left_cloth_shadow3.add_vertex((298, 434))
    left_cloth_shadow3.add_vertex((301, 419))
    left_cloth_shadow3.add_vertex((305, 406))
    left_cloth_shadow3.add_vertex((306, 395))
    left_cloth_shadow3.add_vertex((310, 383))
    left_cloth_shadow3.add_vertex((314, 371))
    left_cloth_shadow3.add_vertex((315, 354))
    left_cloth_shadow3.add_vertex((316, 342))
    left_cloth_shadow3.add_vertex((316, 326))
    left_cloth_shadow3.add_vertex((316, 319))
    left_cloth_shadow3.add_vertex((316, 312))
    left_cloth_shadow3.filled = True
    left_cloth_shadow3.fill_color = GColor(42, 102, 150)#(43, 105, 151)#(38, 98, 143)
    left_cloth_shadow3.color = GColor(42, 102, 150)#(43, 105, 153)#(38, 98, 143)
    window.add(left_cloth_shadow3)

    # 左側身體陰影 右瓣
    left_cloth_shadow = GPolygon()
    left_cloth_shadow.add_vertex((309, 382))
    left_cloth_shadow.add_vertex((314, 385))
    left_cloth_shadow.add_vertex((321, 390))
    left_cloth_shadow.add_vertex((324, 399))
    left_cloth_shadow.add_vertex((321, 409))
    left_cloth_shadow.add_vertex((314, 417))
    left_cloth_shadow.add_vertex((310, 421))
    left_cloth_shadow.add_vertex((306, 426))
    left_cloth_shadow.add_vertex((304, 431))
    left_cloth_shadow.add_vertex((306, 440))
    left_cloth_shadow.add_vertex((312, 445))
    left_cloth_shadow.add_vertex((314, 447))
    left_cloth_shadow.add_vertex((295, 446))
    left_cloth_shadow.add_vertex((296, 440))
    left_cloth_shadow.add_vertex((297, 434))
    left_cloth_shadow.add_vertex((299, 426))
    left_cloth_shadow.add_vertex((301, 418))
    left_cloth_shadow.add_vertex((302, 410))
    left_cloth_shadow.add_vertex((304, 401))
    left_cloth_shadow.add_vertex((306, 395))
    left_cloth_shadow.add_vertex((307, 389))
    left_cloth_shadow.filled = True
    left_cloth_shadow.fill_color = GColor(40, 98, 143)#(42, 106, 153)#(32, 85, 130)
    left_cloth_shadow.color = GColor(40, 98, 143)#(32, 85, 130)
    window.add(left_cloth_shadow)

    # 左側身體陰影2
    left_cloth_shadow2 = GPolygon()
    left_cloth_shadow2.add_vertex((292, 441))
    left_cloth_shadow2.add_vertex((292, 428))
    left_cloth_shadow2.add_vertex((289, 417))
    left_cloth_shadow2.add_vertex((288, 407))
    left_cloth_shadow2.add_vertex((284, 398))
    left_cloth_shadow2.add_vertex((284, 386))
    left_cloth_shadow2.add_vertex((287, 378))
    left_cloth_shadow2.add_vertex((295, 376))
    left_cloth_shadow2.add_vertex((301, 381))
    left_cloth_shadow2.add_vertex((305, 383))
    left_cloth_shadow2.add_vertex((302, 399))
    left_cloth_shadow2.add_vertex((297, 417))
    left_cloth_shadow2.add_vertex((296, 427))
    left_cloth_shadow2.filled = True
    left_cloth_shadow2.fill_color = GColor(42, 102, 150)#(37, 97, 142)#(42, 106, 153)
    left_cloth_shadow2.color = GColor(42, 102, 150)
    window.add(left_cloth_shadow2)

    # 左側身體陰影4 手肘
    left_cloth_shadow4 = GPolygon()
    left_cloth_shadow4.add_vertex((300, 257))
    left_cloth_shadow4.add_vertex((296, 261))
    left_cloth_shadow4.add_vertex((292, 273))
    left_cloth_shadow4.add_vertex((288, 289))
    left_cloth_shadow4.add_vertex((285, 303))
    left_cloth_shadow4.add_vertex((280, 319))
    left_cloth_shadow4.add_vertex((276, 337))
    left_cloth_shadow4.add_vertex((270, 355))
    left_cloth_shadow4.add_vertex((268, 367))
    left_cloth_shadow4.add_vertex((266, 377))
    left_cloth_shadow4.add_vertex((264, 389))
    left_cloth_shadow4.add_vertex((261, 400))
    left_cloth_shadow4.add_vertex((258, 411))
    left_cloth_shadow4.add_vertex((256, 422))
    left_cloth_shadow4.add_vertex((252, 430))
    left_cloth_shadow4.add_vertex((249, 437))
    left_cloth_shadow4.add_vertex((244, 448))
    left_cloth_shadow4.add_vertex((270, 447))
    left_cloth_shadow4.add_vertex((263, 423))
    left_cloth_shadow4.add_vertex((263, 411))
    left_cloth_shadow4.add_vertex((266, 397))
    left_cloth_shadow4.add_vertex((270, 385))
    left_cloth_shadow4.add_vertex((274, 375))
    left_cloth_shadow4.add_vertex((280, 359))
    left_cloth_shadow4.add_vertex((281, 348))
    left_cloth_shadow4.add_vertex((282, 338))
    left_cloth_shadow4.add_vertex((281, 327))
    left_cloth_shadow4.add_vertex((283, 319))
    left_cloth_shadow4.add_vertex((285, 307))
    left_cloth_shadow4.add_vertex((288, 295))
    left_cloth_shadow4.add_vertex((290, 281))
    left_cloth_shadow4.add_vertex((295, 266))
    left_cloth_shadow4.filled = True
    left_cloth_shadow4.fill_color = GColor(37, 97, 142)#(42, 106, 153)
    left_cloth_shadow4.color = GColor(37, 97, 142)
    window.add(left_cloth_shadow4)

    # 右側身體陰影1
    right_cloth_shadow1 = GPolygon()
    right_cloth_shadow1.add_vertex((481, 377))
    right_cloth_shadow1.add_vertex((482, 399))
    right_cloth_shadow1.add_vertex((485, 420))
    right_cloth_shadow1.add_vertex((486, 444))
    right_cloth_shadow1.add_vertex((486, 447))
    right_cloth_shadow1.add_vertex((492, 448))
    right_cloth_shadow1.add_vertex((496, 435))
    right_cloth_shadow1.add_vertex((496, 416))
    right_cloth_shadow1.add_vertex((498, 405))
    right_cloth_shadow1.add_vertex((502, 384))
    right_cloth_shadow1.add_vertex((506, 380))
    right_cloth_shadow1.add_vertex((511, 375))
    right_cloth_shadow1.add_vertex((506, 349))
    right_cloth_shadow1.add_vertex((498, 359))
    right_cloth_shadow1.add_vertex((492, 367))
    right_cloth_shadow1.filled = True
    right_cloth_shadow1.fill_color = GColor(42, 102, 150)
    right_cloth_shadow1.color = GColor(42, 102, 150)
    window.add(right_cloth_shadow1)

    # 右側手肘陰影
    right_cloth_shadow2 = GPolygon()
    right_cloth_shadow2.add_vertex((484, 259))
    right_cloth_shadow2.add_vertex((488, 265))
    right_cloth_shadow2.add_vertex((491, 275))
    right_cloth_shadow2.add_vertex((493, 286))
    right_cloth_shadow2.add_vertex((496, 300))
    right_cloth_shadow2.add_vertex((499, 312))
    right_cloth_shadow2.add_vertex((502, 327))
    right_cloth_shadow2.add_vertex((505, 337))
    right_cloth_shadow2.add_vertex((509, 353))
    right_cloth_shadow2.add_vertex((512, 369))
    right_cloth_shadow2.add_vertex((515, 386))
    right_cloth_shadow2.add_vertex((517, 396))
    right_cloth_shadow2.add_vertex((520, 410))
    right_cloth_shadow2.add_vertex((523, 421))
    right_cloth_shadow2.add_vertex((527, 431))
    right_cloth_shadow2.add_vertex((530, 439))
    right_cloth_shadow2.add_vertex((534, 448))
    right_cloth_shadow2.add_vertex((512, 448))
    right_cloth_shadow2.add_vertex((515, 437))
    right_cloth_shadow2.add_vertex((518, 431))
    right_cloth_shadow2.add_vertex((520, 423))
    right_cloth_shadow2.add_vertex((519, 416))
    right_cloth_shadow2.add_vertex((516, 406))
    right_cloth_shadow2.add_vertex((514, 397))
    right_cloth_shadow2.add_vertex((511, 387))
    right_cloth_shadow2.add_vertex((507, 384))
    right_cloth_shadow2.add_vertex((505, 372))
    right_cloth_shadow2.add_vertex((503, 362))
    right_cloth_shadow2.add_vertex((501, 352))
    right_cloth_shadow2.add_vertex((501, 339))
    right_cloth_shadow2.add_vertex((498, 317))
    right_cloth_shadow2.add_vertex((496, 308))
    right_cloth_shadow2.add_vertex((493, 292))
    right_cloth_shadow2.add_vertex((491, 279))
    right_cloth_shadow2.add_vertex((489, 270))
    right_cloth_shadow2.add_vertex((486, 262))
    right_cloth_shadow2.filled = True
    right_cloth_shadow2.fill_color = GColor(37, 97, 142)#(42, 102, 150)
    right_cloth_shadow2.color = GColor(37, 97, 142)#(42, 102, 150)
    window.add(right_cloth_shadow2)


# 衣服帶子
def cloth_strap(window):

    # 衣服 左邊帶子陰影
    left_tie_shadow = GPolygon()
    left_tie_shadow.add_vertex((373, 402))
    left_tie_shadow.add_vertex((374, 371))
    left_tie_shadow.add_vertex((375, 355))
    left_tie_shadow.add_vertex((376, 337))
    left_tie_shadow.add_vertex((377, 319))
    left_tie_shadow.add_vertex((379, 294))
    left_tie_shadow.add_vertex((378, 293))
    left_tie_shadow.add_vertex((376, 299))
    left_tie_shadow.add_vertex((374, 322))
    left_tie_shadow.add_vertex((373, 345))
    left_tie_shadow.add_vertex((372, 389))
    left_tie_shadow.filled = True
    left_tie_shadow.fill_color = GColor(40, 70, 96)
    left_tie_shadow.color = GColor(40, 70, 96)
    window.add(left_tie_shadow)

    # 衣服 左邊帶子
    cloth_tie = GPolygon()
    cloth_tie.add_vertex((367, 286))
    cloth_tie.add_vertex((366, 313))
    cloth_tie.add_vertex((362, 365))
    cloth_tie.add_vertex((362, 384))
    cloth_tie.add_vertex((362, 405))
    cloth_tie.add_vertex((363, 427))
    cloth_tie.add_vertex((363, 426))
    cloth_tie.add_vertex((366, 446))
    cloth_tie.add_vertex((377, 446))
    cloth_tie.add_vertex((375, 433))
    cloth_tie.add_vertex((374, 411))
    cloth_tie.add_vertex((373, 387))
    cloth_tie.add_vertex((373, 367))
    cloth_tie.add_vertex((374, 338))
    cloth_tie.add_vertex((377, 309))
    cloth_tie.add_vertex((378, 290))
    cloth_tie.filled = True
    cloth_tie.fill_color = GColor(156, 154, 155)  # 黑色
    cloth_tie.color = GColor(156, 154, 155)
    window.add(cloth_tie)

    # 帽子 左側帶子上緣
    left_upper_tie_shadow = GPolygon()
    left_upper_tie_shadow.add_vertex((367, 286))
    # left_upper_tie_shadow.add_vertex((369, 286))
    left_upper_tie_shadow.add_vertex((367, 289))
    left_upper_tie_shadow.add_vertex((378, 293))
    left_upper_tie_shadow.add_vertex((378, 288))
    left_upper_tie_shadow.filled = True
    left_upper_tie_shadow.fill_color = GColor(80, 86, 95)
    left_upper_tie_shadow.color = GColor(80, 86, 95)
    window.add(left_upper_tie_shadow)

    # 衣服 左邊帶子上扣子
    cloth_tie_upper_button = GOval(5, 5, x=366, y=429)
    cloth_tie_upper_button.filled = True
    cloth_tie_upper_button.fill_color = GColor(34, 31, 33)  # 黑色
    cloth_tie_upper_button.color = GColor(37, 36, 37)
    window.add(cloth_tie_upper_button)

    # 衣服 左邊帶子上扣子
    cloth_tie_lower_button = GOval(8, 8, x=366, y=437)
    cloth_tie_lower_button.filled = True
    cloth_tie_lower_button.fill_color = GColor(34, 31, 33)  # 黑色
    cloth_tie_lower_button.color = GColor(37, 36, 37)
    window.add(cloth_tie_lower_button)

    # 右側帽T帶子陰影
    right_tie_shadow = GPolygon()
    right_tie_shadow.add_vertex((434, 294))
    right_tie_shadow.add_vertex((435, 315))
    right_tie_shadow.add_vertex((439, 362))
    right_tie_shadow.add_vertex((440, 329))
    right_tie_shadow.add_vertex((436, 293))
    right_tie_shadow.filled = True
    right_tie_shadow.fill_color = GColor(40, 70, 96)
    right_tie_shadow.color = GColor(40, 70, 96)
    window.add(right_tie_shadow)

    # 衣服 右邊帶子
    cloth_right_tie = GPolygon()
    cloth_right_tie.add_vertex((436, 293))
    cloth_right_tie.add_vertex((436, 294))
    cloth_right_tie.add_vertex((438, 314))
    cloth_right_tie.add_vertex((438, 326))
    cloth_right_tie.add_vertex((440, 336))
    cloth_right_tie.add_vertex((440, 344))
    cloth_right_tie.add_vertex((440, 356))
    cloth_right_tie.add_vertex((440, 367))
    cloth_right_tie.add_vertex((439, 377))
    cloth_right_tie.add_vertex((449, 379))
    cloth_right_tie.add_vertex((449, 369))
    cloth_right_tie.add_vertex((450, 356))
    cloth_right_tie.add_vertex((450, 342))
    cloth_right_tie.add_vertex((449, 332))
    cloth_right_tie.add_vertex((448, 319))
    cloth_right_tie.add_vertex((446, 304))
    cloth_right_tie.add_vertex((445, 289))
    cloth_right_tie.filled = True
    cloth_right_tie.fill_color = GColor(156, 154, 155)  # 灰色
    cloth_right_tie.color = GColor(156, 154, 155)
    window.add(cloth_right_tie)

    # 衣服 右邊帶子上緣陰影
    right_upper_tie_shadow = GPolygon()
    right_upper_tie_shadow.add_vertex((435, 295))
    right_upper_tie_shadow.add_vertex((436, 293))
    right_upper_tie_shadow.add_vertex((445, 289))
    right_upper_tie_shadow.add_vertex((443, 287))
    right_upper_tie_shadow.filled = True
    right_upper_tie_shadow.fill_color = GColor(90, 97, 105)
    right_upper_tie_shadow.color = GColor(90, 97, 105)
    window.add(right_upper_tie_shadow)

    # 衣服 右邊帶子上扣子
    cloth_tie_right_upper_button = GOval(5, 5, x=442, y=361)
    cloth_tie_right_upper_button.filled = True
    cloth_tie_right_upper_button.fill_color = GColor(34, 31, 33)  # 黑色
    cloth_tie_right_upper_button.color = GColor(37, 36, 37)
    window.add(cloth_tie_right_upper_button)

    # 衣服 右邊帶子下扣子
    cloth_tie_right_lower_button = GOval(6, 7, x=442, y=369)
    cloth_tie_right_lower_button.filled = True
    cloth_tie_right_lower_button.fill_color = GColor(34, 31, 33)  # 黑色
    cloth_tie_right_lower_button.color = GColor(37, 36, 37)
    window.add(cloth_tie_right_lower_button)


def collar(window):
    # 衣服 衣領
    cloth_collar = GPolygon()
    cloth_collar.add_vertex((319, 236))
    cloth_collar.add_vertex((314, 239))
    cloth_collar.add_vertex((310, 241))
    cloth_collar.add_vertex((308, 243))
    cloth_collar.add_vertex((306, 247))
    cloth_collar.add_vertex((305, 251))
    cloth_collar.add_vertex((304, 256))
    cloth_collar.add_vertex((308, 262))
    cloth_collar.add_vertex((316, 265))
    cloth_collar.add_vertex((325, 269))
    cloth_collar.add_vertex((334, 273))
    cloth_collar.add_vertex((343, 277))
    cloth_collar.add_vertex((353, 281))
    cloth_collar.add_vertex((368, 285))
    cloth_collar.add_vertex((382, 290))
    cloth_collar.add_vertex((394, 296))
    cloth_collar.add_vertex((401, 300))
    cloth_collar.add_vertex((408, 303))
    cloth_collar.add_vertex((414, 303))
    cloth_collar.add_vertex((422, 299))
    cloth_collar.add_vertex((430, 295))
    cloth_collar.add_vertex((440, 289))
    cloth_collar.add_vertex((452, 283))
    cloth_collar.add_vertex((464, 276))
    cloth_collar.add_vertex((475, 269))
    cloth_collar.add_vertex((482, 263))
    cloth_collar.add_vertex((482, 256))
    cloth_collar.add_vertex((476, 246))
    cloth_collar.filled = True
    cloth_collar.fill_color = GColor(234, 234, 238)#(249, 247, 252)#(233, 235, 239)  # 白色
    cloth_collar.color = GColor(234, 234, 238)#(130, 146, 164)
    window.add(cloth_collar)

    # 衣領左側內部
    inner_left_collar = GPolygon()
    inner_left_collar.add_vertex((407, 298))
    inner_left_collar.add_vertex((386, 290))
    inner_left_collar.add_vertex((363, 280))
    inner_left_collar.add_vertex((343, 271))
    inner_left_collar.add_vertex((329, 264))
    inner_left_collar.add_vertex((320, 256))
    inner_left_collar.add_vertex((317, 250))
    inner_left_collar.add_vertex((318, 245))
    inner_left_collar.add_vertex((322, 243))
    inner_left_collar.add_vertex((331, 248))
    inner_left_collar.add_vertex((341, 252))
    inner_left_collar.add_vertex((349, 257))
    inner_left_collar.add_vertex((362, 262))
    inner_left_collar.add_vertex((371, 267))
    inner_left_collar.add_vertex((381, 272))
    inner_left_collar.add_vertex((389, 276))
    # inner_left_collar.add_vertex((395, 282))
    inner_left_collar.add_vertex((395, 280))
    inner_left_collar.add_vertex((399, 284))
    inner_left_collar.add_vertex((404, 290))
    inner_left_collar.filled = True
    inner_left_collar.fill_color = GColor(255, 255, 255)
    inner_left_collar.color = GColor(233, 235, 239)
    window.add(inner_left_collar)

    # 衣領右側內部
    inner_right_collar = GPolygon()
    inner_right_collar.add_vertex((413, 299))
    inner_right_collar.add_vertex((415, 291))
    inner_right_collar.add_vertex((418, 283))
    # inner_right_collar.add_vertex((422, 280))
    inner_right_collar.add_vertex((424, 277))
    inner_right_collar.add_vertex((430, 272))
    inner_right_collar.add_vertex((436, 266))
    inner_right_collar.add_vertex((443, 260))
    inner_right_collar.add_vertex((447, 256))
    inner_right_collar.add_vertex((449, 253))
    inner_right_collar.add_vertex((474, 244))
    inner_right_collar.add_vertex((470, 257))
    inner_right_collar.add_vertex((467, 263))
    inner_right_collar.add_vertex((463, 270))
    inner_right_collar.add_vertex((456, 275))
    inner_right_collar.add_vertex((446, 281))
    inner_right_collar.add_vertex((430, 291))
    inner_right_collar.add_vertex((420, 295))
    inner_right_collar.filled = True
    inner_right_collar.fill_color = GColor(255, 255, 255)
    inner_right_collar.color = GColor(233, 235, 239)
    window.add(inner_right_collar)

    # 左側衣領最內部陰影
    inner2_left_collar = GPolygon()
    inner2_left_collar.add_vertex((393, 276))
    inner2_left_collar.add_vertex((382, 270))
    inner2_left_collar.add_vertex((370, 264))
    inner2_left_collar.add_vertex((362, 259))
    inner2_left_collar.add_vertex((360, 258))
    inner2_left_collar.add_vertex((354, 252))
    inner2_left_collar.add_vertex((349, 247))
    inner2_left_collar.add_vertex((373, 250))
    inner2_left_collar.add_vertex((374, 252))
    inner2_left_collar.add_vertex((383, 262))
    inner2_left_collar.add_vertex((392, 273))
    inner2_left_collar.filled = True
    inner2_left_collar.fill_color = GColor(241, 236, 230)
    inner2_left_collar.color = GColor(228, 224, 224)
    window.add(inner2_left_collar)

    # 右側衣領最內部陰影
    inner2_right_collar = GPolygon()
    inner2_right_collar.add_vertex((419, 279))
    inner2_right_collar.add_vertex((426, 272))
    inner2_right_collar.add_vertex((432, 268))
    inner2_right_collar.add_vertex((438, 261))
    inner2_right_collar.add_vertex((443, 255))
    inner2_right_collar.add_vertex((441, 253))
    inner2_right_collar.add_vertex((426, 253))
    inner2_right_collar.add_vertex((424, 262))
    inner2_right_collar.filled = True
    inner2_right_collar.fill_color = GColor(241, 236, 230)
    inner2_right_collar.color = GColor(228, 224, 224)
    window.add(inner2_right_collar)

    # 衣領左下陰影
    left_collar_shadow = GPolygon()
    left_collar_shadow.add_vertex((405, 302))
    left_collar_shadow.add_vertex((400, 302))
    left_collar_shadow.add_vertex((395, 301))
    left_collar_shadow.add_vertex((390, 299))
    left_collar_shadow.add_vertex((382, 295))
    left_collar_shadow.add_vertex((371, 291))
    left_collar_shadow.add_vertex((359, 287))
    left_collar_shadow.add_vertex((351, 283))
    left_collar_shadow.add_vertex((340, 278))
    left_collar_shadow.add_vertex((332, 275))
    left_collar_shadow.add_vertex((324, 272))
    left_collar_shadow.add_vertex((317, 268))
    left_collar_shadow.add_vertex((313, 267))
    left_collar_shadow.add_vertex((310, 264))
    left_collar_shadow.add_vertex((305, 261))
    left_collar_shadow.add_vertex((302, 256))
    left_collar_shadow.add_vertex((306, 259))
    left_collar_shadow.add_vertex((313, 264))
    left_collar_shadow.add_vertex((327, 270))
    left_collar_shadow.add_vertex((338, 275))
    left_collar_shadow.add_vertex((356, 282))
    left_collar_shadow.add_vertex((376, 289))
    left_collar_shadow.add_vertex((390, 294))
    left_collar_shadow.add_vertex((394, 295))
    left_collar_shadow.add_vertex((400, 299))
    left_collar_shadow.filled = True
    left_collar_shadow.fill_color = GColor(33, 61, 91)
    left_collar_shadow.color = GColor(27, 72, 116)  # (43, 101, 148)
    window.add(left_collar_shadow)
    
    # 衣領右下陰影
    right_collar_shadow = GPolygon()
    right_collar_shadow.add_vertex((420, 299))
    right_collar_shadow.add_vertex((427, 298))
    right_collar_shadow.add_vertex((434, 295))
    right_collar_shadow.add_vertex((442, 291))
    right_collar_shadow.add_vertex((450, 287))
    right_collar_shadow.add_vertex((457, 282))
    right_collar_shadow.add_vertex((462, 279))
    right_collar_shadow.add_vertex((472, 271))
    right_collar_shadow.add_vertex((464, 276))
    right_collar_shadow.add_vertex((455, 280))
    right_collar_shadow.add_vertex((445, 287))
    right_collar_shadow.add_vertex((433, 293))
    right_collar_shadow.add_vertex((425, 297))
    right_collar_shadow.filled = True
    right_collar_shadow.fill_color = GColor(33, 61, 91)
    right_collar_shadow.color = GColor(27, 72, 116)  # (43, 101, 148)
    window.add(right_collar_shadow)


# 魚骨
def fish_bone(window):

    # 衣服 項鍊魚頭骨
    cloth_necklace_head = GPolygon()
    cloth_necklace_head.add_vertex((424, 303))
    cloth_necklace_head.add_vertex((416, 301))
    # cloth_necklace_head.add_vertex((418, 304))
    cloth_necklace_head.add_vertex((421, 307))
    cloth_necklace_head.filled = True
    cloth_necklace_head.fill_color = GColor(0, 0, 0)  # 黑色
    cloth_necklace_head.color = GColor(0, 0, 0)
    window.add(cloth_necklace_head)

    # 衣服 項鍊魚骨脊椎
    cloth_necklace_spine = GLine(420, 303, 403, 314)
    cloth_necklace_spine.color = GColor(0, 0, 0)
    window.add(cloth_necklace_spine)

    # 衣服 第一魚骨
    cloth_necklace_first_bone = GLine(412, 305, 415, 309)
    cloth_necklace_first_bone.color = GColor(0, 0, 0)
    window.add(cloth_necklace_first_bone)

    # 衣服 第二魚骨
    cloth_necklace_second_bone = GLine(409, 306, 412, 311)
    cloth_necklace_second_bone.color = GColor(0, 0, 0)
    window.add(cloth_necklace_second_bone)

    # 衣服 第一魚骨
    cloth_necklace_third_bone = GLine(406, 308, 409, 313)
    cloth_necklace_third_bone.color = GColor(0, 0, 0)
    window.add(cloth_necklace_third_bone)

    # 衣服 項鍊魚尾骨
    cloth_necklace_tail = GPolygon()
    cloth_necklace_tail.add_vertex((405, 311))
    cloth_necklace_tail.add_vertex((397, 312))
    cloth_necklace_tail.add_vertex((401, 316))
    cloth_necklace_tail.add_vertex((403, 320))
    cloth_necklace_tail.filled = True
    cloth_necklace_tail.fill_color = GColor(0, 0, 0)  # 黑色
    cloth_necklace_tail.color = GColor(0, 0, 0)
    window.add(cloth_necklace_tail)


def inner_cloth(window):
    # 內層衣服
    inside_cloth = GPolygon()
    inside_cloth.add_vertex((423, 267))
    inside_cloth.add_vertex((420, 279))
    inside_cloth.add_vertex((418, 284))
    inside_cloth.add_vertex((416, 289))
    inside_cloth.add_vertex((413, 292))
    inside_cloth.add_vertex((413, 295))
    inside_cloth.add_vertex((411, 297))
    inside_cloth.add_vertex((409, 297))
    inside_cloth.add_vertex((408, 294))
    inside_cloth.add_vertex((406, 292))
    inside_cloth.add_vertex((404, 288))
    inside_cloth.add_vertex((400, 282))
    inside_cloth.add_vertex((396, 278))
    inside_cloth.add_vertex((388, 267))
    inside_cloth.add_vertex((392, 268))
    inside_cloth.add_vertex((396, 270))
    inside_cloth.add_vertex((402, 271))
    inside_cloth.add_vertex((408, 271))
    inside_cloth.add_vertex((413, 271))
    inside_cloth.add_vertex((418, 269))
    inside_cloth.filled = True
    inside_cloth.fill_color = GColor(186, 184, 183)
    inside_cloth.color = GColor(164, 152, 147)# (164, 167, 177)  # (108, 112, 129)
    window.add(inside_cloth)

    # 內層衣服邊邊
    inside_cloth_edge = GPolygon()
    inside_cloth_edge.add_vertex((415, 290))
    inside_cloth_edge.add_vertex((413, 295))
    inside_cloth_edge.add_vertex((410, 296))
    inside_cloth_edge.add_vertex((408, 295))
    inside_cloth_edge.add_vertex((407, 292))
    inside_cloth_edge.add_vertex((406, 291))
    inside_cloth_edge.add_vertex((404, 289))
    inside_cloth_edge.add_vertex((410, 291))
    inside_cloth_edge.filled = True
    inside_cloth_edge.fill_color = GColor(112, 115, 131)
    inside_cloth_edge.color = GColor(112, 115, 131)
    window.add(inside_cloth_edge)