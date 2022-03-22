
from campy.graphics.gcolor import GColor
from campy.graphics.gobjects import GOval, GPolygon, GArc, GLine


# 腮紅
def blush(window):
    # 腮紅 左

    oval = GOval(30, 22, x=370, y=153)
    oval.color = GColor(255, 230, 220)
    oval.filled = True
    oval.fill_color = GColor(255, 230, 220)
    window.add(oval)

    oval = GOval(23, 15, x=373, y=156)
    oval.color = GColor(255, 223, 209)
    oval.filled = True
    oval.fill_color = GColor(255, 223, 209)
    window.add(oval)

    oval = GOval(18, 10, x=375, y=159)
    oval.color = GColor(251, 218, 206)
    oval.filled = True
    oval.fill_color = GColor(251, 218, 206)
    window.add(oval)

    # 腮紅 右
    oval = GOval(30, 20, x=443, y=160)
    oval.color = GColor(255, 230, 220)
    oval.filled = True
    oval.fill_color = GColor(255, 230, 220)
    window.add(oval)

    oval = GOval(21, 11, x=446, y=165)
    oval.color = GColor(255, 223, 209)
    oval.filled = True
    oval.fill_color = GColor(255, 223, 209)
    window.add(oval)

    oval = GOval(16, 6, x=448, y=167)
    oval.color = GColor(251, 218, 206)
    oval.filled = True
    oval.fill_color = GColor(251, 218, 206)
    window.add(oval)


# 眉毛
def eyebrow(window):
    # 左眉毛
    poly = GPolygon()
    poly.add_vertex((371, 122))
    poly.add_vertex((376, 119))
    poly.add_vertex((384, 118))
    poly.add_vertex((390, 118))
    poly.add_vertex((397, 120))

    poly.add_vertex((390, 118))
    poly.add_vertex((384, 119))
    poly.add_vertex((376, 119))
    poly.color = GColor(219, 204, 195)
    window.add(poly)

    # 右眉毛
    poly = GPolygon()
    poly.add_vertex((437, 129))
    poly.add_vertex((442, 128))
    poly.add_vertex((447, 127))
    poly.add_vertex((452, 127))
    poly.add_vertex((458, 130))

    poly.add_vertex((452, 127))
    poly.add_vertex((447, 128))
    poly.add_vertex((442, 128))
    poly.color = GColor(219, 204, 195)
    window.add(poly)


# 眼睛
def eyes(window):
    # 左眼
    poly = GPolygon()
    poly.add_vertex((369, 137))
    poly.add_vertex((376, 134))
    poly.add_vertex((385, 134))
    poly.add_vertex((386, 134))
    poly.add_vertex((392, 135))
    poly.add_vertex((401, 139))
    poly.add_vertex((405, 145))
    poly.add_vertex((405, 153))
    poly.add_vertex((401, 158))
    poly.add_vertex((394, 157))
    poly.add_vertex((386, 155))
    poly.add_vertex((379, 152))
    poly.add_vertex((373, 149))
    poly.add_vertex((372, 146))
    poly.add_vertex((370, 142))
    poly.color = 'white'
    poly.filled = True
    poly.fill_color = 'white'
    window.add(poly)

    # 左眼球
    poly = GPolygon()
    poly.add_vertex((382, 136))
    poly.add_vertex((380, 139))
    poly.add_vertex((379, 144))
    poly.add_vertex((379, 149))
    poly.add_vertex((381, 153))
    poly.add_vertex((386, 155))
    poly.add_vertex((392, 156))
    poly.add_vertex((397, 155))
    poly.add_vertex((398, 153))
    poly.add_vertex((398, 145))
    poly.add_vertex((397, 141))
    poly.add_vertex((396, 139))
    poly.add_vertex((391, 137))
    poly.color = GColor(138, 182, 211)
    poly.filled = True
    poly.fill_color = GColor(138, 182, 211)
    window.add(poly)

    # 左眼球 下淺色
    poly = GPolygon()
    poly.add_vertex((381, 148))
    poly.add_vertex((386, 148))
    poly.add_vertex((392, 149))
    poly.add_vertex((396, 151))
    poly.add_vertex((396, 155))
    poly.add_vertex((391, 155))
    poly.add_vertex((390, 155))
    poly.add_vertex((389, 155))
    poly.add_vertex((383, 153))
    poly.add_vertex((381, 150))
    poly.color = GColor(180, 214, 223)
    poly.filled = True
    poly.fill_color = GColor(180, 214, 223)
    window.add(poly)

    # 左眼球 上深色-中
    poly = GPolygon()
    poly.add_vertex((381, 135))
    poly.add_vertex((388, 137))
    poly.add_vertex((394, 138))
    poly.add_vertex((397, 143))
    poly.add_vertex((390, 142))
    poly.add_vertex((384, 145))
    poly.add_vertex((380, 145))
    poly.add_vertex((380, 141))
    poly.color = GColor(113, 133, 161)
    poly.filled = True
    poly.fill_color = GColor(113, 133, 161)
    window.add(poly)

    # 左眼球 上深色
    poly = GPolygon()
    poly.add_vertex((381, 135))
    poly.add_vertex((388, 136))
    poly.add_vertex((394, 138))
    poly.add_vertex((397, 140))
    poly.add_vertex((390, 139))
    poly.add_vertex((384, 140))
    poly.add_vertex((380, 141))
    poly.add_vertex((380, 141))
    poly.color = GColor(56, 72, 99)
    poly.filled = True
    poly.fill_color = GColor(56, 72, 99)
    window.add(poly)

    # 左 瞳孔-黑
    cc = GOval(3, 3, x=390, y=146)
    cc.filled = True
    cc.fill_color = GColor(72, 109, 149)
    cc.color = GColor(72, 109, 149)
    window.add(cc)

    # 左 瞳孔-白
    cc = GOval(2, 2, x=395, y=145)
    cc.filled = True
    cc.fill_color = 'white'
    cc.color = 'white'
    window.add(cc)

    # 左 黑色睫毛
    poly = GPolygon()
    poly.add_vertex((369, 138))
    poly.add_vertex((376, 134))
    poly.add_vertex((383, 134))
    poly.add_vertex((383, 134))
    poly.add_vertex((389, 135))
    poly.add_vertex((390, 135))
    poly.add_vertex((396, 137))
    poly.add_vertex((402, 139))
    poly.add_vertex((405, 143))
    poly.add_vertex((406, 145))
    poly.add_vertex((401, 143))
    poly.add_vertex((392, 138))
    poly.add_vertex((388, 136))
    poly.add_vertex((385, 136))
    poly.add_vertex((384, 136))
    poly.add_vertex((383, 136))
    poly.add_vertex((380, 137))
    poly.add_vertex((375, 138))
    poly.add_vertex((373, 140))
    poly.color = GColor(49, 48, 55)
    poly.filled = True
    poly.fill_color = GColor(49, 48, 55)
    window.add(poly)

    # 左 黑邊
    poly = GPolygon()
    poly.add_vertex((370, 139))
    poly.add_vertex((371, 143))
    poly.add_vertex((373, 146))
    poly.add_vertex((372, 142))
    poly.add_vertex((373, 138))
    poly.color = GColor(90, 79, 85)
    poly.filled = True
    poly.fill_color = GColor(90, 79, 85)
    window.add(poly)

    # 右眼
    poly = GPolygon()
    poly.add_vertex((442, 149))
    poly.add_vertex((445, 146))
    poly.add_vertex((453, 145))
    poly.add_vertex((461, 147))
    poly.add_vertex((465, 151))
    poly.add_vertex((465, 155))
    poly.add_vertex((464, 159))
    poly.add_vertex((462, 162))
    poly.add_vertex((460, 164))
    poly.add_vertex((454, 164))
    poly.add_vertex((448, 163))
    poly.add_vertex((444, 160))
    poly.add_vertex((442, 155))
    poly.color = 'white'
    poly.filled = True
    poly.fill_color = 'white'
    window.add(poly)

    # 右眼球
    poly = GPolygon()
    poly.add_vertex((443, 149))
    poly.add_vertex((441, 152))
    poly.add_vertex((442, 156))
    poly.add_vertex((447, 162))
    poly.add_vertex((453, 164))
    poly.add_vertex((456, 162))
    poly.add_vertex((457, 154))
    poly.add_vertex((457, 149))
    poly.add_vertex((455, 146))
    poly.add_vertex((449, 146))
    poly.color = GColor(138, 182, 211)
    poly.filled = True
    poly.fill_color = GColor(138, 182, 211)
    window.add(poly)

    # 右眼球 下淺色
    poly = GPolygon()
    poly.add_vertex((444, 156))
    poly.add_vertex((447, 156))
    poly.add_vertex((453, 156))
    poly.add_vertex((454, 159))
    poly.add_vertex((452, 162))
    poly.add_vertex((448, 161))
    poly.add_vertex((445, 160))
    poly.color = GColor(180, 214, 223)
    poly.filled = True
    poly.fill_color = GColor(180, 214, 223)
    window.add(poly)
    #
    # # 右眼球 上深色-中
    poly = GPolygon()
    poly.add_vertex((442, 149))
    poly.add_vertex((446, 146))
    poly.add_vertex((450, 146))
    poly.add_vertex((457, 148))
    poly.add_vertex((457, 150))
    poly.add_vertex((455, 150))
    poly.add_vertex((453, 149))
    poly.add_vertex((448, 150))
    poly.add_vertex((445, 151))
    poly.add_vertex((442, 153))
    poly.color = GColor(113, 133, 161)
    poly.filled = True
    poly.fill_color = GColor(113, 133, 161)
    window.add(poly)
    #
    # # 右眼球 上深色
    poly = GPolygon()
    poly.add_vertex((442, 149))
    poly.add_vertex((444, 148))
    poly.add_vertex((447, 147))
    poly.add_vertex((449, 147))
    poly.add_vertex((446, 149))
    poly.add_vertex((443, 151))
    poly.color = GColor(56, 72, 99)
    poly.filled = True
    poly.fill_color = GColor(56, 72, 99)
    window.add(poly)

    # 右 瞳孔-黑
    cc = GOval(3, 2, x=448, y=154)
    cc.filled = True
    cc.fill_color = GColor(72, 109, 149)
    cc.color = GColor(72, 109, 149)
    window.add(cc)

    # 右 瞳孔-白
    cc = GOval(2, 2, x=453, y=152)
    cc.filled = True
    cc.fill_color = GColor(204, 214, 225)
    cc.color = GColor(204, 214, 225)
    window.add(cc)

    # 右 黑色睫毛
    poly = GPolygon()
    poly.add_vertex((442, 151))
    poly.add_vertex((443, 148))
    poly.add_vertex((446, 145))
    poly.add_vertex((451, 143))
    poly.add_vertex((457, 143))
    poly.add_vertex((461, 146))
    poly.add_vertex((462, 147))
    poly.add_vertex((466, 151))
    poly.add_vertex((466, 154))
    poly.add_vertex((461, 149))
    poly.add_vertex((457, 147))
    poly.add_vertex((449, 146))
    poly.add_vertex((445, 149))
    poly.color = GColor(56, 72, 99)
    poly.filled = True
    poly.fill_color = GColor(56, 72, 99)
    window.add(poly)


# 嘴巴
def mouth(window):
    # 嘴巴
    poly = GPolygon()
    poly.add_vertex((412, 183))
    poly.add_vertex((422, 181))
    poly.add_vertex((432, 183))
    poly.add_vertex((437, 187))
    poly.add_vertex((434, 193))
    poly.add_vertex((429, 197))
    poly.add_vertex((421, 198))
    poly.add_vertex((414, 195))
    poly.add_vertex((412, 190))
    poly.color = GColor(206, 109, 102)
    poly.filled = True
    poly.fill_color = GColor(211, 133, 127)
    window.add(poly)

    # 嘴巴 上牙齒
    poly = GPolygon()
    poly.add_vertex((412, 183))  # 上排
    poly.add_vertex((422, 181))  # 上排
    poly.add_vertex((432, 183))  # 上排
    poly.add_vertex((438, 187))  # 上排
    poly.add_vertex((437, 186))  # 牙齒
    poly.add_vertex((436, 186))  # 牙齒
    poly.add_vertex((435, 185))
    poly.add_vertex((433, 185))  # 牙齒
    poly.add_vertex((432, 185))  # 牙齒
    poly.add_vertex((431, 183))
    poly.add_vertex((429, 184))  # 牙齒
    poly.add_vertex((428, 184))  # 牙齒
    poly.add_vertex((427, 182))
    poly.add_vertex((425, 183))  # 牙齒
    poly.add_vertex((423, 183))  # 牙齒
    poly.add_vertex((421, 182))
    poly.add_vertex((420, 183))  # 牙齒
    poly.add_vertex((418, 183))  # 牙齒
    poly.add_vertex((416, 182))
    poly.add_vertex((414, 184))  # 牙齒
    poly.add_vertex((413, 184))  # 牙齒
    poly.add_vertex((412, 183))
    poly.color = GColor(237, 201, 188)
    poly.filled = True
    poly.fill_color = GColor(241, 237, 237)
    window.add(poly)

    # 嘴巴 下淺色
    poly = GPolygon()
    poly.add_vertex((412, 192))
    poly.add_vertex((417, 192))
    poly.add_vertex((422, 195))
    poly.add_vertex((425, 198))
    poly.add_vertex((419, 198))
    poly.add_vertex((415, 196))
    poly.color = GColor(245, 161, 152)
    poly.filled = True
    poly.fill_color = GColor(245, 161, 152)
    window.add(poly)

    # 嘴巴 外輪廓
    poly = GPolygon()
    poly.add_vertex((412, 183))
    poly.add_vertex((422, 182))
    poly.add_vertex((432, 183))
    poly.add_vertex((438, 187))
    poly.add_vertex((434, 193))
    poly.add_vertex((429, 197))
    poly.add_vertex((421, 198))
    poly.add_vertex((414, 195))
    poly.add_vertex((412, 190))
    poly.color = GColor(208, 174, 161)
    window.add(poly)


# 臉
def face(window):
    poly = GPolygon()
    poly.add_vertex((420, 214))
    poly.add_vertex((394, 205))
    poly.add_vertex((377, 196))
    poly.add_vertex((355, 183))
    poly.add_vertex((355, 182))
    poly.add_vertex((345, 153))
    poly.add_vertex((346, 125))
    poly.add_vertex((359, 95))
    poly.add_vertex((386, 75))
    poly.add_vertex((405, 75))
    poly.add_vertex((430, 75))
    poly.add_vertex((455, 83))
    poly.add_vertex((468, 102))
    poly.add_vertex((475, 118))
    poly.add_vertex((478, 134))
    poly.add_vertex((478, 135))
    poly.add_vertex((478, 136))
    poly.add_vertex((478, 137))
    poly.add_vertex((473, 162))
    poly.add_vertex((473, 164))
    poly.add_vertex((472, 164))
    poly.add_vertex((472, 165))
    poly.add_vertex((472, 167))
    poly.add_vertex((465, 187))
    poly.add_vertex((455, 193))
    poly.add_vertex((441, 205))
    poly.color = GColor(175, 164, 166)
    poly.filled = True
    poly.fill_color = GColor(255, 240, 223)
    window.add(poly)


# 脖子
def neck(window):
    poly = GPolygon()
    poly.add_vertex((379, 189))
    poly.add_vertex((372, 217))
    poly.add_vertex((409, 230))
    poly.add_vertex((417, 204))
    poly.color = GColor(159, 125, 126)
    poly.filled = True
    poly.fill_color = GColor(217, 180, 173)
    window.add(poly)


# 鎖骨
def clavicle(window):
    # 鎖骨
    poly = GPolygon()
    poly.add_vertex((388, 267))
    poly.add_vertex((392, 268))
    poly.add_vertex((396, 270))
    poly.add_vertex((402, 271))
    poly.add_vertex((408, 271))
    poly.add_vertex((413, 271))
    poly.add_vertex((418, 269))
    poly.add_vertex((423, 266))
    poly.add_vertex((423, 267))
    poly.add_vertex((425, 259))
    poly.add_vertex((426, 253))
    poly.add_vertex((377, 253))

    poly.filled = True
    poly.fill_color = GColor(255, 238, 219)
    poly.color = GColor(228, 211, 195)
    window.add(poly)

    # 鎖骨線條 (右)
    right_clavicle_line = GArc(50, 50, 84, 65, x=410, y=260)
    right_clavicle_line.color = (221, 195, 176)
    window.add(right_clavicle_line)

    # 鎖骨線條 (左)
    left_clavicle_line = GArc(50, 50, 33, 65, x=373, y=260)
    left_clavicle_line.color = (221, 195, 176)
    window.add(left_clavicle_line)


# 後側頭髮 (脖子右邊)
def behind_hair(window):
    # 頭髮 脖子右邊
    poly = GPolygon()
    poly.add_vertex((414, 190))
    poly.add_vertex((464, 180))
    poly.add_vertex((458, 220))
    poly.add_vertex((407, 232))
    poly.color = GColor(190, 196, 208)
    poly.filled = True
    poly.fill_color = GColor(190, 196, 208)
    window.add(poly)

    # 頭髮 脖子右邊 中深
    poly = GPolygon()
    poly.add_vertex((446, 197))
    poly.add_vertex((441, 230))
    poly.add_vertex((408, 230))
    poly.add_vertex((410, 203))
    poly.color = GColor(170, 181, 202)
    poly.filled = True
    poly.fill_color = GColor(170, 181, 202)
    window.add(poly)


# 頭髮
def hair(window):
    # 頭髮區塊-左
    poly = GPolygon()
    poly.add_vertex((339, 124))
    poly.add_vertex((365, 124))
    poly.add_vertex((367, 137))
    poly.add_vertex((374, 154))
    poly.add_vertex((366, 148))

    poly.add_vertex((364, 140))  # 岔出去
    poly.add_vertex((363, 135))

    poly.add_vertex((364, 140))  # 岔回去
    poly.add_vertex((366, 148))

    poly.add_vertex((371, 164))
    poly.add_vertex((378, 173))
    poly.add_vertex((385, 179))
    poly.add_vertex((373, 173))

    poly.add_vertex((367, 169))  # 岔出去
    poly.add_vertex((364, 164))
    poly.add_vertex((360, 157))

    poly.add_vertex((365, 164))  # 岔回來
    poly.add_vertex((368, 169))
    poly.add_vertex((373, 173))

    poly.add_vertex((375, 187))
    poly.add_vertex((380, 200))
    poly.add_vertex((387, 212))
    poly.add_vertex((398, 219))
    poly.add_vertex((386, 215))
    poly.add_vertex((378, 206))
    poly.add_vertex((372, 194))
    poly.add_vertex((369, 185))
    poly.add_vertex((367, 179))
    poly.add_vertex((367, 179))

    poly.add_vertex((374, 212))
    poly.add_vertex((382, 231))
    poly.add_vertex((389, 237))
    poly.add_vertex((382, 235))

    poly.add_vertex((378, 229))  # 岔出去
    poly.add_vertex((375, 222))
    poly.add_vertex((372, 215))
    poly.add_vertex((369, 208))

    poly.add_vertex((372, 215))  # 岔回來
    poly.add_vertex((375, 222))
    poly.add_vertex((378, 229))
    poly.add_vertex((382, 235))

    poly.add_vertex((385, 240))
    poly.add_vertex((398, 254))

    poly.add_vertex((392, 253))
    poly.add_vertex((387, 251))
    poly.add_vertex((381, 246))
    poly.add_vertex((385, 251))
    poly.add_vertex((388, 253))

    poly.add_vertex((384, 252))
    poly.add_vertex((373, 245))
    poly.add_vertex((360, 233))
    poly.add_vertex((354, 224))

    poly.add_vertex((352, 220))  # 岔出去
    poly.add_vertex((352, 215))
    poly.add_vertex((352, 208))

    poly.add_vertex((352, 215))  # 岔回來
    poly.add_vertex((352, 220))

    poly.add_vertex((357, 240))
    poly.add_vertex((362, 250))
    poly.add_vertex((370, 257))
    poly.add_vertex((361, 253))
    poly.add_vertex((355, 244))
    poly.add_vertex((350, 230))
    poly.add_vertex((347, 215))

    poly.add_vertex((347, 209))  # 岔出去
    poly.add_vertex((347, 203))
    poly.add_vertex((347, 197))

    poly.add_vertex((347, 203))  # 岔回來
    poly.add_vertex((347, 209))

    poly.add_vertex((346, 205))
    poly.add_vertex((344, 199))
    poly.add_vertex((341, 187))
    poly.add_vertex((340, 177))
    poly.add_vertex((335, 185))
    poly.add_vertex((328, 193))
    poly.add_vertex((319, 198))
    poly.add_vertex((308, 201))
    poly.add_vertex((301, 200))

    poly.add_vertex((311, 199))
    poly.add_vertex((321, 193))
    poly.add_vertex((329, 186))
    poly.add_vertex((334, 177))
    poly.add_vertex((339, 164))
    poly.add_vertex((335, 150))
    poly.color = GColor(185, 185, 185)
    poly.filled = True
    poly.fill_color = GColor(243, 243, 243)
    window.add(poly)

    # 頭髮區塊-右
    poly = GPolygon()
    poly.add_vertex((464, 126))
    poly.add_vertex((481, 124))
    poly.add_vertex((485, 144))
    poly.add_vertex((484, 161))
    poly.add_vertex((484, 182))
    poly.add_vertex((485, 194))
    poly.add_vertex((489, 206))
    poly.add_vertex((493, 217))
    poly.add_vertex((498, 222))
    poly.add_vertex((490, 217))
    poly.add_vertex((486, 209))
    poly.add_vertex((483, 201))
    poly.add_vertex((480, 217))
    poly.add_vertex((477, 232))
    poly.add_vertex((475, 245))
    poly.add_vertex((471, 257))
    poly.add_vertex((465, 268))
    poly.add_vertex((459, 271))
    poly.add_vertex((466, 262))
    poly.add_vertex((470, 252))
    poly.add_vertex((473, 241))
    poly.add_vertex((469, 245))
    poly.add_vertex((463, 253))
    poly.add_vertex((455, 262))
    poly.add_vertex((448, 265))
    poly.add_vertex((439, 266))
    poly.add_vertex((448, 257))
    poly.add_vertex((452, 250))
    poly.add_vertex((445, 252))
    poly.add_vertex((451, 243))
    poly.add_vertex((458, 230))
    poly.add_vertex((462, 215))
    poly.add_vertex((465, 201))
    poly.add_vertex((458, 216))
    poly.add_vertex((451, 225))
    poly.add_vertex((444, 230))
    poly.add_vertex((454, 218))
    poly.add_vertex((459, 206))
    poly.add_vertex((461, 194))
    poly.add_vertex((461, 190))
    poly.add_vertex((454, 191))
    poly.add_vertex((460, 185))
    poly.add_vertex((462, 176))
    poly.add_vertex((465, 166))
    poly.add_vertex((467, 155))
    poly.add_vertex((467, 139))
    poly.color = GColor(185, 185, 185)
    poly.filled = True
    poly.fill_color = GColor(243, 243, 243)
    window.add(poly)

    # 頭髮區塊-中
    poly = GPolygon()
    poly.add_vertex((336, 139))
    poly.add_vertex((337, 135))
    poly.add_vertex((338, 128))
    poly.add_vertex((344, 115))
    poly.add_vertex((353, 106))
    poly.add_vertex((362, 95))
    poly.add_vertex((373, 89))
    poly.add_vertex((383, 78))
    poly.add_vertex((392, 72))
    poly.add_vertex((397, 64))
    poly.add_vertex((405, 60))
    poly.add_vertex((417, 57))
    poly.add_vertex((430, 57))
    poly.add_vertex((441, 65))
    poly.add_vertex((449, 70))
    poly.add_vertex((457, 82))
    poly.add_vertex((464, 91))
    poly.add_vertex((469, 98))
    poly.add_vertex((475, 105))
    poly.add_vertex((478, 115))
    poly.add_vertex((479, 122))
    poly.add_vertex((466, 125))
    poly.add_vertex((463, 122))
    poly.add_vertex((464, 127))
    poly.add_vertex((464, 131))
    poly.add_vertex((464, 134))
    poly.add_vertex((463, 137))
    poly.add_vertex((461, 136))
    poly.add_vertex((459, 132))
    poly.add_vertex((457, 128))
    poly.add_vertex((455, 123))
    poly.add_vertex((453, 118))
    poly.add_vertex((455, 121))
    poly.add_vertex((455, 121))
    poly.add_vertex((454, 122))
    poly.add_vertex((454, 125))
    poly.add_vertex((454, 128))
    poly.add_vertex((454, 127))
    poly.add_vertex((452, 124))
    poly.add_vertex((452, 122))
    poly.add_vertex((451, 118))
    poly.add_vertex((450, 115))
    poly.add_vertex((450, 114))
    poly.add_vertex((449, 111))
    poly.add_vertex((448, 107))
    poly.add_vertex((447, 103))
    poly.add_vertex((446, 101))
    poly.add_vertex((444, 96))
    poly.add_vertex((443, 94))
    poly.add_vertex((445, 99))
    poly.add_vertex((446, 101))
    poly.add_vertex((446, 106))
    poly.add_vertex((446, 111))
    poly.add_vertex((447, 116))
    poly.add_vertex((447, 121))
    poly.add_vertex((447, 120))
    poly.add_vertex((448, 125))
    poly.add_vertex((447, 124))
    poly.add_vertex((446, 121))
    poly.add_vertex((445, 119))
    poly.add_vertex((444, 116))
    poly.add_vertex((443, 113))
    poly.add_vertex((443, 110))
    poly.add_vertex((444, 115))
    poly.add_vertex((443, 119))
    poly.add_vertex((443, 122))
    poly.add_vertex((442, 124))
    poly.add_vertex((441, 126))
    poly.add_vertex((440, 128))
    poly.add_vertex((438, 129))
    poly.add_vertex((437, 127))
    poly.add_vertex((436, 121))
    poly.add_vertex((436, 116))
    poly.add_vertex((435, 111))
    poly.add_vertex((435, 107))
    poly.add_vertex((435, 103))
    poly.add_vertex((434, 99))
    poly.add_vertex((434, 105))
    poly.add_vertex((434, 109))
    poly.add_vertex((433, 113))
    poly.add_vertex((433, 117))
    poly.add_vertex((433, 120))
    poly.add_vertex((432, 123))
    poly.add_vertex((431, 125))
    poly.add_vertex((429, 126))
    poly.add_vertex((428, 124))
    poly.add_vertex((428, 122))
    poly.add_vertex((428, 123))
    poly.add_vertex((428, 124))
    poly.add_vertex((428, 126))
    poly.add_vertex((428, 127))
    poly.add_vertex((428, 128))
    poly.add_vertex((428, 129))
    poly.add_vertex((428, 118))
    poly.add_vertex((428, 114))
    poly.add_vertex((428, 109))
    poly.add_vertex((427, 105))
    poly.add_vertex((427, 101))
    poly.add_vertex((427, 97))
    poly.add_vertex((427, 105))
    poly.add_vertex((426, 110))
    poly.add_vertex((426, 114))
    poly.add_vertex((425, 118))
    poly.add_vertex((424, 121))
    poly.add_vertex((424, 122))
    poly.add_vertex((423, 125))
    poly.add_vertex((419, 124))
    poly.add_vertex((416, 123))
    poly.add_vertex((415, 123))
    poly.add_vertex((411, 123))
    poly.add_vertex((408, 124))
    poly.add_vertex((407, 120))
    poly.add_vertex((407, 115))
    poly.add_vertex((406, 110))
    poly.add_vertex((406, 105))
    poly.add_vertex((406, 101))
    poly.add_vertex((406, 95))
    poly.add_vertex((406, 91))
    poly.add_vertex((406, 98))
    poly.add_vertex((405, 108))
    poly.add_vertex((405, 113))
    poly.add_vertex((405, 119))
    poly.add_vertex((405, 120))
    poly.add_vertex((404, 125))
    poly.add_vertex((402, 125))
    poly.add_vertex((401, 121))
    poly.add_vertex((401, 120))
    poly.add_vertex((400, 119))
    poly.add_vertex((400, 118))
    poly.add_vertex((400, 113))
    poly.add_vertex((401, 109))
    poly.add_vertex((400, 103))
    poly.add_vertex((401, 100))
    poly.add_vertex((401, 94))
    poly.add_vertex((401, 100))
    poly.add_vertex((398, 104))
    poly.add_vertex((396, 107))
    poly.add_vertex((394, 112))
    poly.add_vertex((392, 116))
    poly.add_vertex((390, 119))
    poly.add_vertex((389, 123))
    poly.add_vertex((387, 125))
    poly.add_vertex((387, 123))
    poly.add_vertex((388, 117))
    poly.add_vertex((389, 113))
    poly.add_vertex((390, 111))
    poly.add_vertex((391, 107))
    poly.add_vertex((392, 101))
    poly.add_vertex((393, 98))
    poly.add_vertex((394, 93))
    poly.add_vertex((392, 102))
    poly.add_vertex((390, 105))
    poly.add_vertex((386, 108))
    poly.add_vertex((384, 112))
    poly.add_vertex((381, 115))
    poly.add_vertex((379, 120))
    poly.add_vertex((376, 125))
    poly.add_vertex((375, 126))
    poly.add_vertex((373, 128))
    poly.add_vertex((370, 130))
    poly.add_vertex((371, 126))
    poly.add_vertex((371, 123))
    poly.add_vertex((371, 119))
    poly.add_vertex((371, 116))
    poly.add_vertex((369, 123))
    poly.add_vertex((368, 128))
    poly.add_vertex((366, 130))
    poly.add_vertex((367, 135))
    poly.add_vertex((361, 136))
    poly.add_vertex((350, 138))
    poly.add_vertex((344, 139))
    poly.color = GColor(185, 185, 185)
    poly.filled = True
    poly.fill_color = GColor(243, 243, 243)
    window.add(poly)

    # 頭髮 遮線 左
    poly = GPolygon()
    poly.add_vertex((365, 138))
    poly.add_vertex((366, 121))
    poly.add_vertex((339, 130))
    poly.add_vertex((337, 145))
    poly.color = GColor(243, 243, 243)
    poly.filled = True
    poly.fill_color = GColor(243, 243, 243)
    window.add(poly)

    # 頭髮 遮線 右
    poly = GPolygon()
    poly.add_vertex((464, 125))
    poly.add_vertex((470, 143))
    poly.add_vertex((483, 135))
    poly.add_vertex((481, 121))
    poly.color = GColor(243, 243, 243)
    poly.filled = True
    poly.fill_color = GColor(243, 243, 243)
    window.add(poly)


# 頭髮 裝飾
def hair_decorate(window):
    # 頭髮 藍左
    poly = GPolygon()
    poly.add_vertex((361, 174))
    poly.add_vertex((371, 215))
    poly.add_vertex((378, 233))
    poly.add_vertex((368, 215))
    poly.add_vertex((361, 197))
    poly.color = GColor(112, 177, 226)
    poly.filled = True
    poly.fill_color = GColor(112, 177, 226)
    window.add(poly)

    # 頭髮 藍右
    poly = GPolygon()
    poly.add_vertex((471, 193))
    poly.add_vertex((450, 248))
    poly.add_vertex((463, 232))
    poly.add_vertex((468, 216))
    poly.color = GColor(112, 177, 226)
    poly.filled = True
    poly.fill_color = GColor(112, 177, 226)
    window.add(poly)

    # 頭髮 深藍色
    poly = GPolygon()
    poly.add_vertex((410, 79))
    poly.add_vertex((413, 105))
    poly.add_vertex((417, 121))
    poly.add_vertex((409, 124))
    poly.add_vertex((405, 104))
    poly.color = GColor(103, 160, 229)
    poly.filled = True
    poly.fill_color = GColor(103, 160, 229)
    window.add(poly)

    # 頭髮 淺藍色
    poly = GPolygon()
    # poly.add_vertex((400, 103))
    # poly.add_vertex((401, 123))
    # poly.add_vertex((405, 124))
    # poly.add_vertex((408, 102))
    # poly.add_vertex((402, 87))
    # poly.add_vertex((402, 91))
    # poly.add_vertex((401, 98))
    poly.add_vertex((401, 104))
    poly.add_vertex((400, 110))
    poly.add_vertex((401, 116))
    poly.add_vertex((402, 121))
    poly.add_vertex((401, 121))
    poly.add_vertex((403, 125))
    poly.add_vertex((404, 119))
    poly.add_vertex((405, 110))
    poly.add_vertex((405, 99))
    poly.add_vertex((405, 93))
    poly.add_vertex((406, 88))

    poly.color = GColor(186, 227, 249)
    poly.filled = True
    poly.fill_color = GColor(186, 227, 249)
    window.add(poly)


    # 頭髮 淺藍色 左
    poly = GPolygon()
    poly.add_vertex((368, 98))
    poly.add_vertex((366, 123))
    poly.add_vertex((376, 116))
    poly.add_vertex((376, 100))
    poly.color = GColor(186, 227, 249)
    poly.filled = True
    poly.fill_color = GColor(186, 227, 249)
    window.add(poly)

    # 頭髮 淺藍色 左 陰影
    poly = GPolygon()
    poly.add_vertex((368, 98))
    poly.add_vertex((376, 100))
    poly.add_vertex((377, 89))
    poly.add_vertex((369, 86))
    poly.color = GColor(79, 113, 151)
    poly.filled = True
    poly.fill_color = GColor(79, 113, 151)
    window.add(poly)

    # 頭髮 淺藍色 右
    poly = GPolygon()
    poly.add_vertex((461, 107))
    poly.add_vertex((466, 137))
    poly.add_vertex((468, 128))
    poly.color = GColor(186, 227, 249)
    poly.filled = True
    poly.fill_color = GColor(186, 227, 249)
    window.add(poly)

    # 頭髮 中中 灰
    poly = GPolygon()
    poly.add_vertex((360, 146))
    poly.add_vertex((361, 158))
    poly.add_vertex((369, 169))
    poly.add_vertex((378, 175))
    poly.add_vertex((372, 168))
    poly.add_vertex((368, 159))
    poly.add_vertex((365, 155))
    poly.color = GColor(214, 215, 219)
    poly.filled = True
    poly.fill_color = GColor(214, 215, 219)
    window.add(poly)

    # 頭髮 左中 灰 (左)
    poly = GPolygon()
    poly.add_vertex((343, 171))
    poly.add_vertex((339, 180))
    poly.add_vertex((335, 187))
    poly.add_vertex((328, 193))
    poly.add_vertex((322, 197))
    poly.add_vertex((328, 190))
    poly.add_vertex((333, 185))
    poly.add_vertex((336, 182))
    poly.color = GColor(214, 215, 219)
    poly.filled = True
    poly.fill_color = GColor(214, 215, 219)
    window.add(poly)

    # 頭髮 左下 灰
    poly = GPolygon()
    poly.add_vertex((353, 193))
    poly.add_vertex((354, 220))
    poly.add_vertex((359, 231))
    poly.add_vertex((371, 244))
    poly.add_vertex((376, 245))
    poly.add_vertex((370, 237))
    poly.add_vertex((364, 230))
    poly.add_vertex((358, 215))
    poly.add_vertex((355, 203))
    poly.color = GColor(214, 215, 219)
    poly.filled = True
    poly.fill_color = GColor(214, 215, 219)
    window.add(poly)

    # 頭髮 右中 灰
    poly = GPolygon()
    poly.add_vertex((469, 157))
    poly.add_vertex((464, 175))
    poly.add_vertex((459, 188))
    poly.add_vertex((467, 181))
    poly.add_vertex((469, 169))
    poly.color = GColor(197, 199, 204)
    poly.filled = True
    poly.fill_color = GColor(197, 199, 204)
    window.add(poly)

    # 頭髮 右下 灰
    poly = GPolygon()
    poly.add_vertex((476, 195))
    poly.add_vertex((472, 222))
    poly.add_vertex((464, 247))
    poly.add_vertex((454, 259))
    poly.add_vertex((463, 251))
    poly.add_vertex((472, 241))
    poly.add_vertex((475, 228))
    poly.color = GColor(197, 199, 204)
    poly.filled = True
    poly.fill_color = GColor(197, 199, 204)
    window.add(poly)

    line = GLine(370, 120, 374, 98)
    line.color = GColor(185, 185, 185)
    window.add(line)

    # 帽子外頭髮
    poly = GPolygon()
    poly.add_vertex((297, 222))
    poly.add_vertex((293, 230))
    poly.add_vertex((287, 238))
    poly.add_vertex((280, 244))
    poly.add_vertex((271, 251))
    poly.add_vertex((277, 250))
    poly.add_vertex((285, 246))
    poly.add_vertex((291, 240))
    poly.add_vertex((295, 234))
    poly.add_vertex((301, 226))
    poly.add_vertex((295, 236))
    poly.add_vertex((291, 248))
    poly.add_vertex((286, 257))
    poly.add_vertex((280, 268))
    poly.add_vertex((274, 274))
    poly.add_vertex((265, 282))
    poly.add_vertex((275, 277))
    poly.add_vertex((280, 273))
    poly.add_vertex((286, 267))
    poly.add_vertex((292, 260))
    poly.add_vertex((298, 250))
    poly.add_vertex((303, 241))
    poly.add_vertex((307, 230))
    poly.add_vertex((305, 236))
    poly.add_vertex((303, 244))
    poly.add_vertex((303, 256))
    poly.add_vertex((303, 254))  # 標記
    poly.add_vertex((305, 247))  # 標記
    poly.add_vertex((306, 244))  # 標記
    poly.add_vertex((308, 243))  # 標記
    poly.add_vertex((312, 239))  # 標記
    poly.add_vertex((315, 238))  # 標記
    poly.add_vertex((318, 235))  # 標記
    poly.add_vertex((320, 235))
    poly.color = GColor(149, 155, 165)
    poly.filled = True
    poly.fill_color = GColor(209, 214, 226)
    window.add(poly)
