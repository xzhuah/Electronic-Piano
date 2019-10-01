# Electronic Piano
 An piano program that can mimic different instrument for you to play with.

You will need a python3 environment and pygame package to run this program:
To install pygame:

	pip install pygame


To start the program:
	
	python piano.py

List of instrument that this program can support:
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

The default instrument is Acoustic Grand Piano

弹奏时需要选中程序的白框，不要选中黑框控制台
 
asdf jkl, 分别对应 1234567 音阶， 这个设计方便你用双手弹奏
往上提一个度： qweruio
往下降一个度： zxcvm,.

你可以用[]来将整个按键设置的音阶向下或向上调整1个度（7个音阶）

你可以按住shift键来提高半个音阶以此来模拟钢琴的黑键

你可以使用-+来切换不同乐器，你也可以使用'`'这个按键(一般是数字1左边的那个)，然后在黑框控制台中输入乐器序号来直接切换到你想要的乐器

演奏模式：默认情况下，当你按下并抬起一个音后，你可以听到这个音慢慢减弱（有些乐器不会减弱），这是为了方便初级使用者轻松弹出好听的音乐而设定的，如果你是高级玩家，你可以改变这种设置，这样当你抬起按键后，余音立刻停止，你可以通过\键来切换这个模式，有些乐器必须在这个模式下才能正常使用，如果你发现音乐声无法正常停止，多半是你使用了低级模式来弹奏那些需要高级模式的乐器，这个时候重启程序，先切换高级模式，再选择你的乐器即可。

你可以利用{ 和 }来切换不同的大小调，这涉及到一定的音理知识。

