import pygame.midi
import time
pygame.midi.init()
output=pygame.midi.Output(pygame.midi.get_default_output_id())
output.set_instrument(0)

'''
0 Acoustic Grand Piano                    大钢琴（声学钢琴）
1 Bright Acoustic Piano                    明亮的钢琴
2 Electric Grand Piano                      电钢琴
3 Honky-tonk Piano                        酒吧钢琴
4 Rhodes Piano                               柔和的电钢琴
5 Chorused Piano                           加合唱效果的电钢琴
6 Harpsichord                                 羽管键琴（拨弦古钢琴）
7 Clavichord                                   科拉维科特琴（击弦古钢琴）

色彩打击乐器
8 Celesta                                        钢片琴
9 Glockenspiel                               钟琴
10 Music box                                 八音盒
11 Vibraphone                              颤音琴
12 Marimba                                  马林巴
13 Xylophone                               木琴
14 Tubular Bells                           管钟
15 Dulcimer                                 大扬琴

风琴
16 Hammond Organ                  击杆风琴
17 Percussive Organ                  打击式风琴
18 Rock Organ                           摇滚风琴
19 Church Organ                       教堂风琴
20 Reed Organ                          簧管风琴
21 Accordian                             手风琴
22 Harmonica                            口琴
23 Tango Accordian                  探戈手风琴

吉他
24 Acoustic Guitar (nylon)        尼龙弦吉他
25 Acoustic Guitar (steel)         钢弦吉他
26 Electric Guitar (jazz)             爵士电吉他
27 Electric Guitar (clean)          清音电吉他
28 Electric Guitar (muted)       闷音电吉他
29 Overdriven Guitar              加驱动效果的电吉他
30 Distortion Guitar                加失真效果的电吉他
31 Guitar Harmonics               吉他和音

贝司
32 Acoustic Bass                     大贝司（声学贝司）
33 Electric Bass(finger)           电贝司（指弹）
34 Electric Bass (pick)             电贝司（拨片）
35 Fretless Bass                      无品贝司
36 Slap Bass 1                        掌击Bass 1
37 Slap Bass 2                        掌击Bass 2
38 Synth Bass 1                     电子合成Bass 1
39 Synth Bass 2                     电子合成Bass 2

弦乐
40 Violin                               小提琴
41 Viola                                中提琴
42 Cello                                大提琴
43 Contrabass                      低音大提琴
44 Tremolo Strings              弦乐群颤音音色
45 Pizzicato Strings             弦乐群拨弦音色
46 Orchestral Harp              竖琴
47 Timpani                          定音鼓

合奏/合唱
48 String Ensemble 1          弦乐合奏音色1
49 String Ensemble 2         弦乐合奏音色2
50 Synth Strings 1             合成弦乐合奏音色1
51 Synth Strings 2             合成弦乐合奏音色2
52 Choir Aahs                    人声合唱“啊”
53 Voice Oohs                  人声“嘟”
54 Synth Voice                  合成人声
55 Orchestra Hit                管弦乐敲击齐奏

铜管
56 Trumpet                        小号
57 Trombone                     长号
58 Tuba                              大号
59 Muted Trumpet            加弱音器小号
60 French Horn                 法国号（圆号）
61 Brass Section                铜管组（铜管乐器合奏音色）
62 Synth Brass 1               合成铜管音色1
63 Synth Brass 2               合成铜管音色2

簧管
64 Soprano Sax                高音萨克斯风
65 Alto Sax                       次中音萨克斯风
66 Tenor Sax                    中音萨克斯风
67 Baritone Sax               低音萨克斯风
68 Oboe                          双簧管
69 English Horn              英国管
70 Bassoon                     巴松（大管）
71 Clarinet                      单簧管（黑管）

笛
72 Piccolo                       短笛
73 Flute                          长笛
74 Recorder                    竖笛
75 Pan Flute                   排箫
76 Bottle Blow               吹瓶声
77 Shakuhachi               日本尺八
78 Whistle                     口哨声
79 Ocarina                     奥卡雷那

合成主音
80 Lead 1 (square)        合成主音1（方波）
81 Lead 2 (sawtooth)    合成主音2（锯齿波）
82 Lead 3 (caliope lead)合成主音3
83 Lead 4 (chiff lead)    合成主音4
84 Lead 5 (charang)      合成主音5
85 Lead 6 (voice)          合成主音6（人声）
86 Lead 7 (fifths)          合成主音7（平行五度）
87 Lead 8 (bass+lead)  合成主音8（贝司加主音）

合成音色
88 Pad 1 (new age)      合成音色1（新世纪）
89 Pad 2 (warm)          合成音色2 （温暖）
90 Pad 3 (polysynth)    合成音色3
91 Pad 4 (choir)           合成音色4 （合唱）
92 Pad 5 (bowed)        合成音色5
93 Pad 6 (metallic)      合成音色6 （金属声）
94 Pad 7 (halo)            合成音色7 （光环）
95 Pad 8 (sweep)         合成音色8

合成效果
96 FX 1 (rain)               合成效果 1 雨声
97 FX 2 (soundtrack)   合成效果 2 音轨
98 FX 3 (crystal)           合成效果 3 水晶
99 FX 4 (atmosphere)  合成效果 4 大气
100 FX 5 (brightness)  合成效果 5 明亮
101 FX 6 (goblins)       合成效果 6 鬼怪
102 FX 7 (echoes)       合成效果 7 回声
103 FX 8 (sci-fi)           合成效果 8 科幻

民间乐器
104 Sitar                     西塔尔（印度）
105 Banjo                   班卓琴（美洲）
106 Shamisen             三昧线（日本）
107 Koto                     十三弦筝（日本）
108 Kalimba               卡林巴
109 Bagpipe               风笛
110 Fiddle                  民族提琴
111 Shanai                 山奈

打击乐器
112 Tinkle Bell           叮当铃
113 Agogo                摇摆舞铃
114 Steel Drums        钢鼓
115 Woodblock         木鱼
116 Taiko Drum         太鼓
117 Melodic Tom      通通鼓
118 Synth Drum         合成鼓
119 Reverse Cymbal   铜钹

Sound Effects 声音效果
120 Guitar Fret Noise  吉他换把杂音
121 Breath Noise         呼吸声
122 Seashore               海浪声
123 Bird Tweet            鸟鸣
124 Telephone Ring    电话铃
125 Helicopter             直升机
126 Applause               鼓掌声
127 Gunshot                枪击声
'''

import turtle
turtle.reset()
mode = 0
offset = 0
current_instrunment = 0
def changemode():
    global mode,offset
    mode = 1 - mode
    turtle.onkeypress(scale_122, 'z')
    turtle.onkeypress(scale_120, 'x')
    turtle.onkeypress(scale_99, 'c')
    turtle.onkeypress(scale_118, 'v')
    turtle.onkeypress(scale_109, 'm')
    turtle.onkeypress(scale_44, ',')
    turtle.onkeypress(scale_46, '.')
    turtle.onkeypress(scale_97, 'a')
    turtle.onkeypress(scale_115, 's')
    turtle.onkeypress(scale_100, 'd')
    turtle.onkeypress(scale_102, 'f')
    turtle.onkeypress(scale_106, 'j')
    turtle.onkeypress(scale_107, 'k')
    turtle.onkeypress(scale_108, 'l')
    turtle.onkeypress(scale_113, 'q')
    turtle.onkeypress(scale_119, 'w')
    turtle.onkeypress(scale_101, 'e')
    turtle.onkeypress(scale_114, 'r')
    turtle.onkeypress(scale_117, 'u')
    turtle.onkeypress(scale_105, 'i')
    turtle.onkeypress(scale_111, 'o')
    turtle.onkeypress(scale_49, '1')
    turtle.onkeypress(scale_50, '2')
    turtle.onkeypress(scale_51, '3')
    turtle.onkeypress(scale_52, '4')
    turtle.onkeypress(scale_55, '7')
    turtle.onkeypress(scale_56, '8')
    turtle.onkeypress(scale_57, '9')



    turtle.onkeypress(scale_90, 'Z')
    turtle.onkeypress(scale_88, 'X')
    turtle.onkeypress(scale_67, 'C')
    turtle.onkeypress(scale_86, 'V')
    turtle.onkeypress(scale_77, 'M')
    turtle.onkeypress(scale_60, '<')
    turtle.onkeypress(scale_62, '>')
    turtle.onkeypress(scale_65, 'A')
    turtle.onkeypress(scale_83, 'S')
    turtle.onkeypress(scale_68, 'D')
    turtle.onkeypress(scale_70, 'F')
    turtle.onkeypress(scale_74, 'J')
    turtle.onkeypress(scale_75, 'K')
    turtle.onkeypress(scale_76, 'L')
    turtle.onkeypress(scale_81, 'Q')
    turtle.onkeypress(scale_87, 'W')
    turtle.onkeypress(scale_69, 'E')
    turtle.onkeypress(scale_82, 'R')
    turtle.onkeypress(scale_85, 'U')
    turtle.onkeypress(scale_73, 'I')
    turtle.onkeypress(scale_79, 'O')
    turtle.onkeypress(scale_33, '!')
    turtle.onkeypress(scale_64, '@')
    turtle.onkeypress(scale_35, '#')
    turtle.onkeypress(scale_36, '$')
    turtle.onkeypress(scale_38, '&')
    turtle.onkeypress(scale_42, '*')
    turtle.onkeypress(scale_40, '(')



    turtle.onkeyrelease(r_scale_122, 'z')
    turtle.onkeyrelease(r_scale_120, 'x')
    turtle.onkeyrelease(r_scale_99, 'c')
    turtle.onkeyrelease(r_scale_118, 'v')
    turtle.onkeyrelease(r_scale_109, 'm')
    turtle.onkeyrelease(r_scale_44, ',')
    turtle.onkeyrelease(r_scale_46, '.')
    turtle.onkeyrelease(r_scale_97, 'a')
    turtle.onkeyrelease(r_scale_115, 's')
    turtle.onkeyrelease(r_scale_100, 'd')
    turtle.onkeyrelease(r_scale_102, 'f')
    turtle.onkeyrelease(r_scale_106, 'j')
    turtle.onkeyrelease(r_scale_107, 'k')
    turtle.onkeyrelease(r_scale_108, 'l')
    turtle.onkeyrelease(r_scale_113, 'q')
    turtle.onkeyrelease(r_scale_119, 'w')
    turtle.onkeyrelease(r_scale_101, 'e')
    turtle.onkeyrelease(r_scale_114, 'r')
    turtle.onkeyrelease(r_scale_117, 'u')
    turtle.onkeyrelease(r_scale_105, 'i')
    turtle.onkeyrelease(r_scale_111, 'o')
    turtle.onkeyrelease(r_scale_49, '1')
    turtle.onkeyrelease(r_scale_50, '2')
    turtle.onkeyrelease(r_scale_51, '3')
    turtle.onkeyrelease(r_scale_52, '4')
    turtle.onkeyrelease(r_scale_55, '7')
    turtle.onkeyrelease(r_scale_56, '8')
    turtle.onkeyrelease(r_scale_57, '9')




    turtle.onkeyrelease(r_scale_90, 'Z')
    turtle.onkeyrelease(r_scale_88, 'X')
    turtle.onkeyrelease(r_scale_67, 'C')
    turtle.onkeyrelease(r_scale_86, 'V')
    turtle.onkeyrelease(r_scale_77, 'M')
    turtle.onkeyrelease(r_scale_60, '<')
    turtle.onkeyrelease(r_scale_62, '>')
    turtle.onkeyrelease(r_scale_65, 'A')
    turtle.onkeyrelease(r_scale_83, 'S')
    turtle.onkeyrelease(r_scale_68, 'D')
    turtle.onkeyrelease(r_scale_70, 'F')
    turtle.onkeyrelease(r_scale_74, 'J')
    turtle.onkeyrelease(r_scale_75, 'K')
    turtle.onkeyrelease(r_scale_76, 'L')
    turtle.onkeyrelease(r_scale_81, 'Q')
    turtle.onkeyrelease(r_scale_87, 'W')
    turtle.onkeyrelease(r_scale_69, 'E')
    turtle.onkeyrelease(r_scale_82, 'R')
    turtle.onkeyrelease(r_scale_85, 'U')
    turtle.onkeyrelease(r_scale_73, 'I')
    turtle.onkeyrelease(r_scale_79, 'O')
    turtle.onkeyrelease(r_scale_33, '!')
    turtle.onkeyrelease(r_scale_64, '@')
    turtle.onkeyrelease(r_scale_35, '#')
    turtle.onkeyrelease(r_scale_36, '$')
    turtle.onkeyrelease(r_scale_38, '&')
    turtle.onkeyrelease(r_scale_42, '*')
    turtle.onkeyrelease(r_scale_40, '(')

def increaseoffSet():
    global offset
    if offset<2:
        offset+=1
def decreaseoffSet():
    global offset
    if offset>-4:
        offset-=1

def resetInstrument():
    global output,current_instrunment
    pygame.midi.init()
    new = input("Instrument number")
    try:
        output.set_instrument(int(new))
        current_instrunment = int(new)
    except:
        pass
def inc_instrunment():
    global output,current_instrunment
    pygame.midi.init()
  
    try:
        output.set_instrument(current_instrunment+1)
        current_instrunment+=1
    except:
        pass


def init_music():
    pygame.midi.init()


def dec_instrunment():
    global output,current_instrunment
    pygame.midi.init()
  
    try:
        output.set_instrument(current_instrunment-1)
        current_instrunment-=1
    except:
        pass

def scale_122():
    global mode,offset
    output.note_on(48+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'z')
def r_scale_122():
    global mode,offset
    if mode==1:
        output.note_off(48+12*offset,127)
        turtle.onkeypress(scale_122, 'z')
def scale_120():
    global mode,offset
    output.note_on(50+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'x')
def r_scale_120():
    global mode,offset
    if mode==1:
        output.note_off(50+12*offset,127)
        turtle.onkeypress(scale_120, 'x')
def scale_99():
    global mode,offset
    output.note_on(52+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'c')
def r_scale_99():
    global mode,offset
    if mode==1:
        output.note_off(52+12*offset,127)
        turtle.onkeypress(scale_99, 'c')
def scale_118():
    global mode,offset
    output.note_on(53+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'v')
def r_scale_118():
    global mode,offset
    if mode==1:
        output.note_off(53+12*offset,127)
        turtle.onkeypress(scale_118, 'v')
def scale_109():
    global mode,offset
    output.note_on(55+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'm')
def r_scale_109():
    global mode,offset
    if mode==1:
        output.note_off(55+12*offset,127)
        turtle.onkeypress(scale_109, 'm')
def scale_44():
    global mode,offset
    output.note_on(57+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, ',')
def r_scale_44():
    global mode,offset
    if mode==1:
        output.note_off(57+12*offset,127)
        turtle.onkeypress(scale_44, ',')
def scale_46():
    global mode,offset
    output.note_on(59+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '.')
def r_scale_46():
    global mode,offset
    if mode==1:
        output.note_off(59+12*offset,127)
        turtle.onkeypress(scale_46, '.')
def scale_97():
    global mode,offset
    output.note_on(60+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'a')
def r_scale_97():
    global mode,offset
    if mode==1:
        output.note_off(60+12*offset,127)
        turtle.onkeypress(scale_97, 'a')
def scale_115():
    global mode,offset
    output.note_on(62+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 's')
def r_scale_115():
    global mode,offset
    if mode==1:
        output.note_off(62+12*offset,127)
        turtle.onkeypress(scale_115, 's')
def scale_100():
    global mode,offset
    output.note_on(64+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'd')
def r_scale_100():
    global mode,offset
    if mode==1:
        output.note_off(64+12*offset,127)
        turtle.onkeypress(scale_100, 'd')
def scale_102():
    global mode,offset
    output.note_on(65+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'f')
def r_scale_102():
    global mode,offset
    if mode==1:
        output.note_off(65+12*offset,127)
        turtle.onkeypress(scale_102, 'f')
def scale_106():
    global mode,offset
    output.note_on(67+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'j')
def r_scale_106():
    global mode,offset
    if mode==1:
        output.note_off(67+12*offset,127)
        turtle.onkeypress(scale_106, 'j')
def scale_107():
    global mode,offset
    output.note_on(69+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'k')
def r_scale_107():
    global mode,offset
    if mode==1:
        output.note_off(69+12*offset,127)
        turtle.onkeypress(scale_107, 'k')
def scale_108():
    global mode,offset
    output.note_on(71+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'l')
def r_scale_108():
    global mode,offset
    if mode==1:
        output.note_off(71+12*offset,127)
        turtle.onkeypress(scale_108, 'l')
def scale_113():
    global mode,offset
    output.note_on(72+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'q')
def r_scale_113():
    global mode,offset
    if mode==1:
        output.note_off(72+12*offset,127)
        turtle.onkeypress(scale_113, 'q')
def scale_119():
    global mode,offset
    output.note_on(74+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'w')
def r_scale_119():
    global mode,offset
    if mode==1:
        output.note_off(74+12*offset,127)
        turtle.onkeypress(scale_119, 'w')
def scale_101():
    global mode,offset
    output.note_on(76+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'e')
def r_scale_101():
    global mode,offset
    if mode==1:
        output.note_off(76+12*offset,127)
        turtle.onkeypress(scale_101, 'e')
def scale_114():
    global mode,offset
    output.note_on(77+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'r')
def r_scale_114():
    global mode,offset
    if mode==1:
        output.note_off(77+12*offset,127)
        turtle.onkeypress(scale_114, 'r')
def scale_117():
    global mode,offset
    output.note_on(79+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'u')
def r_scale_117():
    global mode,offset
    if mode==1:
        output.note_off(79+12*offset,127)
        turtle.onkeypress(scale_117, 'u')
def scale_105():
    global mode,offset
    output.note_on(81+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'i')
def r_scale_105():
    global mode,offset
    if mode==1:
        output.note_off(81+12*offset,127)
        turtle.onkeypress(scale_105, 'i')
def scale_111():
    global mode,offset
    output.note_on(83+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'o')
def r_scale_111():
    global mode,offset
    if mode==1:
        output.note_off(83+12*offset,127)
        turtle.onkeypress(scale_111, 'o')
def scale_49():
    global mode,offset
    output.note_on(84+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '1')
def r_scale_49():
    global mode,offset
    if mode==1:
        output.note_off(84+12*offset,127)
        turtle.onkeypress(scale_49, '1')
def scale_50():
    global mode,offset
    output.note_on(86+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '2')
def r_scale_50():
    global mode,offset
    if mode==1:
        output.note_off(86+12*offset,127)
        turtle.onkeypress(scale_50, '2')
def scale_51():
    global mode,offset
    output.note_on(88+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '3')
def r_scale_51():
    global mode,offset
    if mode==1:
        output.note_off(88+12*offset,127)
        turtle.onkeypress(scale_51, '3')
def scale_52():
    global mode,offset
    output.note_on(89+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '4')
def r_scale_52():
    global mode,offset
    if mode==1:
        output.note_off(89+12*offset,127)
        turtle.onkeypress(scale_52, '4')
def scale_55():
    global mode,offset
    output.note_on(91+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '7')
def r_scale_55():
    global mode,offset
    if mode==1:
        output.note_off(91+12*offset,127)
        turtle.onkeypress(scale_55, '7')
def scale_56():
    global mode,offset
    output.note_on(93+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '8')
def r_scale_56():
    global mode,offset
    if mode==1:
        output.note_off(93+12*offset,127)
        turtle.onkeypress(scale_56, '8')
def scale_57():
    global mode,offset
    output.note_on(95+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '9')
def r_scale_57():
    global mode,offset
    if mode==1:
        output.note_off(95+12*offset,127)
        turtle.onkeypress(scale_57, '9')
def scale_90():
    global mode,offset
    output.note_on(49+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'Z')
def r_scale_90():
    global mode,offset
    if mode==1:
        output.note_off(49+12*offset,127)
        turtle.onkeypress(scale_90, 'Z')
def scale_88():
    global mode,offset
    output.note_on(51+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'X')
def r_scale_88():
    global mode,offset
    if mode==1:
        output.note_off(51+12*offset,127)
        turtle.onkeypress(scale_88, 'X')
def scale_67():
    global mode,offset
    output.note_on(53+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'C')
def r_scale_67():
    global mode,offset
    if mode==1:
        output.note_off(53+12*offset,127)
        turtle.onkeypress(scale_67, 'C')
def scale_86():
    global mode,offset
    output.note_on(54+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'V')
def r_scale_86():
    global mode,offset
    if mode==1:
        output.note_off(54+12*offset,127)
        turtle.onkeypress(scale_86, 'V')
def scale_77():
    global mode,offset
    output.note_on(56+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'M')
def r_scale_77():
    global mode,offset
    if mode==1:
        output.note_off(56+12*offset,127)
        turtle.onkeypress(scale_77, 'M')
def scale_60():
    global mode,offset
    output.note_on(58+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '<')
def r_scale_60():
    global mode,offset
    if mode==1:
        output.note_off(58+12*offset,127)
        turtle.onkeypress(scale_60, '<')
def scale_62():
    global mode,offset
    output.note_on(60+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '>')
def r_scale_62():
    global mode,offset
    if mode==1:
        output.note_off(60+12*offset,127)
        turtle.onkeypress(scale_62, '>')
def scale_65():
    global mode,offset
    output.note_on(61+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'A')
def r_scale_65():
    global mode,offset
    if mode==1:
        output.note_off(61+12*offset,127)
        turtle.onkeypress(scale_65, 'A')
def scale_83():
    global mode,offset
    output.note_on(63+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'S')
def r_scale_83():
    global mode,offset
    if mode==1:
        output.note_off(63+12*offset,127)
        turtle.onkeypress(scale_83, 'S')
def scale_68():
    global mode,offset
    output.note_on(65+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'D')
def r_scale_68():
    global mode,offset
    if mode==1:
        output.note_off(65+12*offset,127)
        turtle.onkeypress(scale_68, 'D')
def scale_70():
    global mode,offset
    output.note_on(66+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'F')
def r_scale_70():
    global mode,offset
    if mode==1:
        output.note_off(66+12*offset,127)
        turtle.onkeypress(scale_70, 'F')
def scale_74():
    global mode,offset
    output.note_on(68+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'J')
def r_scale_74():
    global mode,offset
    if mode==1:
        output.note_off(68+12*offset,127)
        turtle.onkeypress(scale_74, 'J')
def scale_75():
    global mode,offset
    output.note_on(70+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'K')
def r_scale_75():
    global mode,offset
    if mode==1:
        output.note_off(70+12*offset,127)
        turtle.onkeypress(scale_75, 'K')
def scale_76():
    global mode,offset
    output.note_on(72+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'L')
def r_scale_76():
    global mode,offset
    if mode==1:
        output.note_off(72+12*offset,127)
        turtle.onkeypress(scale_76, 'L')
def scale_81():
    global mode,offset
    output.note_on(73+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'Q')
def r_scale_81():
    global mode,offset
    if mode==1:
        output.note_off(73+12*offset,127)
        turtle.onkeypress(scale_81, 'Q')
def scale_87():
    global mode,offset
    output.note_on(75+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'W')
def r_scale_87():
    global mode,offset
    if mode==1:
        output.note_off(75+12*offset,127)
        turtle.onkeypress(scale_87, 'W')
def scale_69():
    global mode,offset
    output.note_on(77+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'E')
def r_scale_69():
    global mode,offset
    if mode==1:
        output.note_off(77+12*offset,127)
        turtle.onkeypress(scale_69, 'E')
def scale_82():
    global mode,offset
    output.note_on(78+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'R')
def r_scale_82():
    global mode,offset
    if mode==1:
        output.note_off(78+12*offset,127)
        turtle.onkeypress(scale_82, 'R')
def scale_85():
    global mode,offset
    output.note_on(80+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'U')
def r_scale_85():
    global mode,offset
    if mode==1:
        output.note_off(80+12*offset,127)
        turtle.onkeypress(scale_85, 'U')
def scale_73():
    global mode,offset
    output.note_on(82+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'I')
def r_scale_73():
    global mode,offset
    if mode==1:
        output.note_off(82+12*offset,127)
        turtle.onkeypress(scale_73, 'I')
def scale_79():
    global mode,offset
    output.note_on(84+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, 'O')
def r_scale_79():
    global mode,offset
    if mode==1:
        output.note_off(84+12*offset,127)
        turtle.onkeypress(scale_79, 'O')
def scale_33():
    global mode,offset
    output.note_on(85+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '!')
def r_scale_33():
    global mode,offset
    if mode==1:
        output.note_off(85+12*offset,127)
        turtle.onkeypress(scale_33, '!')
def scale_64():
    global mode,offset
    output.note_on(87+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '@')
def r_scale_64():
    global mode,offset
    if mode==1:
        output.note_off(87+12*offset,127)
        turtle.onkeypress(scale_64, '@')
def scale_35():
    global mode,offset
    output.note_on(89+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '#')
def r_scale_35():
    global mode,offset
    if mode==1:
        output.note_off(89+12*offset,127)
        turtle.onkeypress(scale_35, '#')
def scale_36():
    global mode,offset
    output.note_on(90+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '$')
def r_scale_36():
    global mode,offset
    if mode==1:
        output.note_off(90+12*offset,127)
        turtle.onkeypress(scale_36, '$')
def scale_38():
    global mode,offset
    output.note_on(92+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '&')
def r_scale_38():
    global mode,offset
    if mode==1:
        output.note_off(92+12*offset,127)
        turtle.onkeypress(scale_38, '&')
def scale_42():
    global mode,offset
    output.note_on(94+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '*')
def r_scale_42():
    global mode,offset
    if mode==1:
        output.note_off(94+12*offset,127)
        turtle.onkeypress(scale_42, '*')
def scale_40():
    global mode,offset
    output.note_on(96+12*offset,127)
    if mode==1:
        turtle.onkeypress(None, '(')
def r_scale_40():
    global mode,offset
    if mode==1:
        output.note_off(96+12*offset,127)
        turtle.onkeypress(scale_40, '(')

turtle.onkeypress(scale_122, 'z')
turtle.onkeypress(scale_120, 'x')
turtle.onkeypress(scale_99, 'c')
turtle.onkeypress(scale_118, 'v')
turtle.onkeypress(scale_109, 'm')
turtle.onkeypress(scale_44, ',')
turtle.onkeypress(scale_46, '.')
turtle.onkeypress(scale_97, 'a')
turtle.onkeypress(scale_115, 's')
turtle.onkeypress(scale_100, 'd')
turtle.onkeypress(scale_102, 'f')
turtle.onkeypress(scale_106, 'j')
turtle.onkeypress(scale_107, 'k')
turtle.onkeypress(scale_108, 'l')
turtle.onkeypress(scale_113, 'q')
turtle.onkeypress(scale_119, 'w')
turtle.onkeypress(scale_101, 'e')
turtle.onkeypress(scale_114, 'r')
turtle.onkeypress(scale_117, 'u')
turtle.onkeypress(scale_105, 'i')
turtle.onkeypress(scale_111, 'o')
turtle.onkeypress(scale_49, '1')
turtle.onkeypress(scale_50, '2')
turtle.onkeypress(scale_51, '3')
turtle.onkeypress(scale_52, '4')
turtle.onkeypress(scale_55, '7')
turtle.onkeypress(scale_56, '8')
turtle.onkeypress(scale_57, '9')



turtle.onkeypress(scale_90, 'Z')
turtle.onkeypress(scale_88, 'X')
turtle.onkeypress(scale_67, 'C')
turtle.onkeypress(scale_86, 'V')
turtle.onkeypress(scale_77, 'M')
turtle.onkeypress(scale_60, '<')
turtle.onkeypress(scale_62, '>')
turtle.onkeypress(scale_65, 'A')
turtle.onkeypress(scale_83, 'S')
turtle.onkeypress(scale_68, 'D')
turtle.onkeypress(scale_70, 'F')
turtle.onkeypress(scale_74, 'J')
turtle.onkeypress(scale_75, 'K')
turtle.onkeypress(scale_76, 'L')
turtle.onkeypress(scale_81, 'Q')
turtle.onkeypress(scale_87, 'W')
turtle.onkeypress(scale_69, 'E')
turtle.onkeypress(scale_82, 'R')
turtle.onkeypress(scale_85, 'U')
turtle.onkeypress(scale_73, 'I')
turtle.onkeypress(scale_79, 'O')
turtle.onkeypress(scale_33, '!')
turtle.onkeypress(scale_64, '@')
turtle.onkeypress(scale_35, '#')
turtle.onkeypress(scale_36, '$')
turtle.onkeypress(scale_38, '&')
turtle.onkeypress(scale_42, '*')
turtle.onkeypress(scale_40, '(')



turtle.onkeyrelease(r_scale_122, 'z')
turtle.onkeyrelease(r_scale_120, 'x')
turtle.onkeyrelease(r_scale_99, 'c')
turtle.onkeyrelease(r_scale_118, 'v')
turtle.onkeyrelease(r_scale_109, 'm')
turtle.onkeyrelease(r_scale_44, ',')
turtle.onkeyrelease(r_scale_46, '.')
turtle.onkeyrelease(r_scale_97, 'a')
turtle.onkeyrelease(r_scale_115, 's')
turtle.onkeyrelease(r_scale_100, 'd')
turtle.onkeyrelease(r_scale_102, 'f')
turtle.onkeyrelease(r_scale_106, 'j')
turtle.onkeyrelease(r_scale_107, 'k')
turtle.onkeyrelease(r_scale_108, 'l')
turtle.onkeyrelease(r_scale_113, 'q')
turtle.onkeyrelease(r_scale_119, 'w')
turtle.onkeyrelease(r_scale_101, 'e')
turtle.onkeyrelease(r_scale_114, 'r')
turtle.onkeyrelease(r_scale_117, 'u')
turtle.onkeyrelease(r_scale_105, 'i')
turtle.onkeyrelease(r_scale_111, 'o')
turtle.onkeyrelease(r_scale_49, '1')
turtle.onkeyrelease(r_scale_50, '2')
turtle.onkeyrelease(r_scale_51, '3')
turtle.onkeyrelease(r_scale_52, '4')
turtle.onkeyrelease(r_scale_55, '7')
turtle.onkeyrelease(r_scale_56, '8')
turtle.onkeyrelease(r_scale_57, '9')




turtle.onkeyrelease(r_scale_90, 'Z')
turtle.onkeyrelease(r_scale_88, 'X')
turtle.onkeyrelease(r_scale_67, 'C')
turtle.onkeyrelease(r_scale_86, 'V')
turtle.onkeyrelease(r_scale_77, 'M')
turtle.onkeyrelease(r_scale_60, '<')
turtle.onkeyrelease(r_scale_62, '>')
turtle.onkeyrelease(r_scale_65, 'A')
turtle.onkeyrelease(r_scale_83, 'S')
turtle.onkeyrelease(r_scale_68, 'D')
turtle.onkeyrelease(r_scale_70, 'F')
turtle.onkeyrelease(r_scale_74, 'J')
turtle.onkeyrelease(r_scale_75, 'K')
turtle.onkeyrelease(r_scale_76, 'L')
turtle.onkeyrelease(r_scale_81, 'Q')
turtle.onkeyrelease(r_scale_87, 'W')
turtle.onkeyrelease(r_scale_69, 'E')
turtle.onkeyrelease(r_scale_82, 'R')
turtle.onkeyrelease(r_scale_85, 'U')
turtle.onkeyrelease(r_scale_73, 'I')
turtle.onkeyrelease(r_scale_79, 'O')
turtle.onkeyrelease(r_scale_33, '!')
turtle.onkeyrelease(r_scale_64, '@')
turtle.onkeyrelease(r_scale_35, '#')
turtle.onkeyrelease(r_scale_36, '$')
turtle.onkeyrelease(r_scale_38, '&')
turtle.onkeyrelease(r_scale_42, '*')
turtle.onkeyrelease(r_scale_40, '(')


turtle.onkeyrelease(resetInstrument,'`')

turtle.onkeyrelease(changemode,'\\')

turtle.onkeyrelease(decreaseoffSet,'[')

turtle.onkeyrelease(increaseoffSet,']')
turtle.onkeyrelease(inc_instrunment,"=")
turtle.onkeyrelease(dec_instrunment,"-")


turtle.listen()
#output.close()
#pygame.midi.quit()
turtle.done()
