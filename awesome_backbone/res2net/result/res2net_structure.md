====================================================================================================
                                             Kernel Shape       Output Shape  \
Layer                                                                          
0_conv1                                     [3, 64, 7, 7]  [1, 64, 112, 112]   
1_bn1                                                [64]  [1, 64, 112, 112]   
2_relu                                                  -  [1, 64, 112, 112]   
3_maxpool                                               -    [1, 64, 56, 56]   
4_layer1.0.Conv2d_conv1                   [64, 104, 1, 1]   [1, 104, 56, 56]   
5_layer1.0.BatchNorm2d_bn1                          [104]   [1, 104, 56, 56]   
6_layer1.0.ReLU_relu                                    -   [1, 104, 56, 56]   
7_layer1.0.convs.Conv2d_0                  [26, 26, 3, 3]    [1, 26, 56, 56]   
8_layer1.0.bns.BatchNorm2d_0                         [26]    [1, 26, 56, 56]   
9_layer1.0.ReLU_relu                                    -    [1, 26, 56, 56]   
10_layer1.0.convs.Conv2d_1                 [26, 26, 3, 3]    [1, 26, 56, 56]   
11_layer1.0.bns.BatchNorm2d_1                        [26]    [1, 26, 56, 56]   
12_layer1.0.ReLU_relu                                   -    [1, 26, 56, 56]   
13_layer1.0.convs.Conv2d_2                 [26, 26, 3, 3]    [1, 26, 56, 56]   
14_layer1.0.bns.BatchNorm2d_2                        [26]    [1, 26, 56, 56]   
15_layer1.0.ReLU_relu                                   -    [1, 26, 56, 56]   
16_layer1.0.AvgPool2d_pool                              -    [1, 26, 56, 56]   
17_layer1.0.Conv2d_conv3                 [104, 256, 1, 1]   [1, 256, 56, 56]   
18_layer1.0.BatchNorm2d_bn3                         [256]   [1, 256, 56, 56]   
19_layer1.0.downsample.Conv2d_0           [64, 256, 1, 1]   [1, 256, 56, 56]   
20_layer1.0.downsample.BatchNorm2d_1                [256]   [1, 256, 56, 56]   
21_layer1.0.ReLU_relu                                   -   [1, 256, 56, 56]   
22_layer1.1.Conv2d_conv1                 [256, 104, 1, 1]   [1, 104, 56, 56]   
23_layer1.1.BatchNorm2d_bn1                         [104]   [1, 104, 56, 56]   
24_layer1.1.ReLU_relu                                   -   [1, 104, 56, 56]   
25_layer1.1.convs.Conv2d_0                 [26, 26, 3, 3]    [1, 26, 56, 56]   
26_layer1.1.bns.BatchNorm2d_0                        [26]    [1, 26, 56, 56]   
27_layer1.1.ReLU_relu                                   -    [1, 26, 56, 56]   
28_layer1.1.convs.Conv2d_1                 [26, 26, 3, 3]    [1, 26, 56, 56]   
29_layer1.1.bns.BatchNorm2d_1                        [26]    [1, 26, 56, 56]   
30_layer1.1.ReLU_relu                                   -    [1, 26, 56, 56]   
31_layer1.1.convs.Conv2d_2                 [26, 26, 3, 3]    [1, 26, 56, 56]   
32_layer1.1.bns.BatchNorm2d_2                        [26]    [1, 26, 56, 56]   
33_layer1.1.ReLU_relu                                   -    [1, 26, 56, 56]   
34_layer1.1.Conv2d_conv3                 [104, 256, 1, 1]   [1, 256, 56, 56]   
35_layer1.1.BatchNorm2d_bn3                         [256]   [1, 256, 56, 56]   
36_layer1.1.ReLU_relu                                   -   [1, 256, 56, 56]   
37_layer1.2.Conv2d_conv1                 [256, 104, 1, 1]   [1, 104, 56, 56]   
38_layer1.2.BatchNorm2d_bn1                         [104]   [1, 104, 56, 56]   
39_layer1.2.ReLU_relu                                   -   [1, 104, 56, 56]   
40_layer1.2.convs.Conv2d_0                 [26, 26, 3, 3]    [1, 26, 56, 56]   
41_layer1.2.bns.BatchNorm2d_0                        [26]    [1, 26, 56, 56]   
42_layer1.2.ReLU_relu                                   -    [1, 26, 56, 56]   
43_layer1.2.convs.Conv2d_1                 [26, 26, 3, 3]    [1, 26, 56, 56]   
44_layer1.2.bns.BatchNorm2d_1                        [26]    [1, 26, 56, 56]   
45_layer1.2.ReLU_relu                                   -    [1, 26, 56, 56]   
46_layer1.2.convs.Conv2d_2                 [26, 26, 3, 3]    [1, 26, 56, 56]   
47_layer1.2.bns.BatchNorm2d_2                        [26]    [1, 26, 56, 56]   
48_layer1.2.ReLU_relu                                   -    [1, 26, 56, 56]   
49_layer1.2.Conv2d_conv3                 [104, 256, 1, 1]   [1, 256, 56, 56]   
50_layer1.2.BatchNorm2d_bn3                         [256]   [1, 256, 56, 56]   
51_layer1.2.ReLU_relu                                   -   [1, 256, 56, 56]   
52_layer2.0.Conv2d_conv1                 [256, 208, 1, 1]   [1, 208, 56, 56]   
53_layer2.0.BatchNorm2d_bn1                         [208]   [1, 208, 56, 56]   
54_layer2.0.ReLU_relu                                   -   [1, 208, 56, 56]   
55_layer2.0.convs.Conv2d_0                 [52, 52, 3, 3]    [1, 52, 28, 28]   
56_layer2.0.bns.BatchNorm2d_0                        [52]    [1, 52, 28, 28]   
57_layer2.0.ReLU_relu                                   -    [1, 52, 28, 28]   
58_layer2.0.convs.Conv2d_1                 [52, 52, 3, 3]    [1, 52, 28, 28]   
59_layer2.0.bns.BatchNorm2d_1                        [52]    [1, 52, 28, 28]   
60_layer2.0.ReLU_relu                                   -    [1, 52, 28, 28]   
61_layer2.0.convs.Conv2d_2                 [52, 52, 3, 3]    [1, 52, 28, 28]   
62_layer2.0.bns.BatchNorm2d_2                        [52]    [1, 52, 28, 28]   
63_layer2.0.ReLU_relu                                   -    [1, 52, 28, 28]   
64_layer2.0.AvgPool2d_pool                              -    [1, 52, 28, 28]   
65_layer2.0.Conv2d_conv3                 [208, 512, 1, 1]   [1, 512, 28, 28]   
66_layer2.0.BatchNorm2d_bn3                         [512]   [1, 512, 28, 28]   
67_layer2.0.downsample.Conv2d_0          [256, 512, 1, 1]   [1, 512, 28, 28]   
68_layer2.0.downsample.BatchNorm2d_1                [512]   [1, 512, 28, 28]   
69_layer2.0.ReLU_relu                                   -   [1, 512, 28, 28]   
70_layer2.1.Conv2d_conv1                 [512, 208, 1, 1]   [1, 208, 28, 28]   
71_layer2.1.BatchNorm2d_bn1                         [208]   [1, 208, 28, 28]   
72_layer2.1.ReLU_relu                                   -   [1, 208, 28, 28]   
73_layer2.1.convs.Conv2d_0                 [52, 52, 3, 3]    [1, 52, 28, 28]   
74_layer2.1.bns.BatchNorm2d_0                        [52]    [1, 52, 28, 28]   
75_layer2.1.ReLU_relu                                   -    [1, 52, 28, 28]   
76_layer2.1.convs.Conv2d_1                 [52, 52, 3, 3]    [1, 52, 28, 28]   
77_layer2.1.bns.BatchNorm2d_1                        [52]    [1, 52, 28, 28]   
78_layer2.1.ReLU_relu                                   -    [1, 52, 28, 28]   
79_layer2.1.convs.Conv2d_2                 [52, 52, 3, 3]    [1, 52, 28, 28]   
80_layer2.1.bns.BatchNorm2d_2                        [52]    [1, 52, 28, 28]   
81_layer2.1.ReLU_relu                                   -    [1, 52, 28, 28]   
82_layer2.1.Conv2d_conv3                 [208, 512, 1, 1]   [1, 512, 28, 28]   
83_layer2.1.BatchNorm2d_bn3                         [512]   [1, 512, 28, 28]   
84_layer2.1.ReLU_relu                                   -   [1, 512, 28, 28]   
85_layer2.2.Conv2d_conv1                 [512, 208, 1, 1]   [1, 208, 28, 28]   
86_layer2.2.BatchNorm2d_bn1                         [208]   [1, 208, 28, 28]   
87_layer2.2.ReLU_relu                                   -   [1, 208, 28, 28]   
88_layer2.2.convs.Conv2d_0                 [52, 52, 3, 3]    [1, 52, 28, 28]   
89_layer2.2.bns.BatchNorm2d_0                        [52]    [1, 52, 28, 28]   
90_layer2.2.ReLU_relu                                   -    [1, 52, 28, 28]   
91_layer2.2.convs.Conv2d_1                 [52, 52, 3, 3]    [1, 52, 28, 28]   
92_layer2.2.bns.BatchNorm2d_1                        [52]    [1, 52, 28, 28]   
93_layer2.2.ReLU_relu                                   -    [1, 52, 28, 28]   
94_layer2.2.convs.Conv2d_2                 [52, 52, 3, 3]    [1, 52, 28, 28]   
95_layer2.2.bns.BatchNorm2d_2                        [52]    [1, 52, 28, 28]   
96_layer2.2.ReLU_relu                                   -    [1, 52, 28, 28]   
97_layer2.2.Conv2d_conv3                 [208, 512, 1, 1]   [1, 512, 28, 28]   
98_layer2.2.BatchNorm2d_bn3                         [512]   [1, 512, 28, 28]   
99_layer2.2.ReLU_relu                                   -   [1, 512, 28, 28]   
100_layer2.3.Conv2d_conv1                [512, 208, 1, 1]   [1, 208, 28, 28]   
101_layer2.3.BatchNorm2d_bn1                        [208]   [1, 208, 28, 28]   
102_layer2.3.ReLU_relu                                  -   [1, 208, 28, 28]   
103_layer2.3.convs.Conv2d_0                [52, 52, 3, 3]    [1, 52, 28, 28]   
104_layer2.3.bns.BatchNorm2d_0                       [52]    [1, 52, 28, 28]   
105_layer2.3.ReLU_relu                                  -    [1, 52, 28, 28]   
106_layer2.3.convs.Conv2d_1                [52, 52, 3, 3]    [1, 52, 28, 28]   
107_layer2.3.bns.BatchNorm2d_1                       [52]    [1, 52, 28, 28]   
108_layer2.3.ReLU_relu                                  -    [1, 52, 28, 28]   
109_layer2.3.convs.Conv2d_2                [52, 52, 3, 3]    [1, 52, 28, 28]   
110_layer2.3.bns.BatchNorm2d_2                       [52]    [1, 52, 28, 28]   
111_layer2.3.ReLU_relu                                  -    [1, 52, 28, 28]   
112_layer2.3.Conv2d_conv3                [208, 512, 1, 1]   [1, 512, 28, 28]   
113_layer2.3.BatchNorm2d_bn3                        [512]   [1, 512, 28, 28]   
114_layer2.3.ReLU_relu                                  -   [1, 512, 28, 28]   
115_layer3.0.Conv2d_conv1                [512, 416, 1, 1]   [1, 416, 28, 28]   
116_layer3.0.BatchNorm2d_bn1                        [416]   [1, 416, 28, 28]   
117_layer3.0.ReLU_relu                                  -   [1, 416, 28, 28]   
118_layer3.0.convs.Conv2d_0              [104, 104, 3, 3]   [1, 104, 14, 14]   
119_layer3.0.bns.BatchNorm2d_0                      [104]   [1, 104, 14, 14]   
120_layer3.0.ReLU_relu                                  -   [1, 104, 14, 14]   
121_layer3.0.convs.Conv2d_1              [104, 104, 3, 3]   [1, 104, 14, 14]   
122_layer3.0.bns.BatchNorm2d_1                      [104]   [1, 104, 14, 14]   
123_layer3.0.ReLU_relu                                  -   [1, 104, 14, 14]   
124_layer3.0.convs.Conv2d_2              [104, 104, 3, 3]   [1, 104, 14, 14]   
125_layer3.0.bns.BatchNorm2d_2                      [104]   [1, 104, 14, 14]   
126_layer3.0.ReLU_relu                                  -   [1, 104, 14, 14]   
127_layer3.0.AvgPool2d_pool                             -   [1, 104, 14, 14]   
128_layer3.0.Conv2d_conv3               [416, 1024, 1, 1]  [1, 1024, 14, 14]   
129_layer3.0.BatchNorm2d_bn3                       [1024]  [1, 1024, 14, 14]   
130_layer3.0.downsample.Conv2d_0        [512, 1024, 1, 1]  [1, 1024, 14, 14]   
131_layer3.0.downsample.BatchNorm2d_1              [1024]  [1, 1024, 14, 14]   
132_layer3.0.ReLU_relu                                  -  [1, 1024, 14, 14]   
133_layer3.1.Conv2d_conv1               [1024, 416, 1, 1]   [1, 416, 14, 14]   
134_layer3.1.BatchNorm2d_bn1                        [416]   [1, 416, 14, 14]   
135_layer3.1.ReLU_relu                                  -   [1, 416, 14, 14]   
136_layer3.1.convs.Conv2d_0              [104, 104, 3, 3]   [1, 104, 14, 14]   
137_layer3.1.bns.BatchNorm2d_0                      [104]   [1, 104, 14, 14]   
138_layer3.1.ReLU_relu                                  -   [1, 104, 14, 14]   
139_layer3.1.convs.Conv2d_1              [104, 104, 3, 3]   [1, 104, 14, 14]   
140_layer3.1.bns.BatchNorm2d_1                      [104]   [1, 104, 14, 14]   
141_layer3.1.ReLU_relu                                  -   [1, 104, 14, 14]   
142_layer3.1.convs.Conv2d_2              [104, 104, 3, 3]   [1, 104, 14, 14]   
143_layer3.1.bns.BatchNorm2d_2                      [104]   [1, 104, 14, 14]   
144_layer3.1.ReLU_relu                                  -   [1, 104, 14, 14]   
145_layer3.1.Conv2d_conv3               [416, 1024, 1, 1]  [1, 1024, 14, 14]   
146_layer3.1.BatchNorm2d_bn3                       [1024]  [1, 1024, 14, 14]   
147_layer3.1.ReLU_relu                                  -  [1, 1024, 14, 14]   
148_layer3.2.Conv2d_conv1               [1024, 416, 1, 1]   [1, 416, 14, 14]   
149_layer3.2.BatchNorm2d_bn1                        [416]   [1, 416, 14, 14]   
150_layer3.2.ReLU_relu                                  -   [1, 416, 14, 14]   
151_layer3.2.convs.Conv2d_0              [104, 104, 3, 3]   [1, 104, 14, 14]   
152_layer3.2.bns.BatchNorm2d_0                      [104]   [1, 104, 14, 14]   
153_layer3.2.ReLU_relu                                  -   [1, 104, 14, 14]   
154_layer3.2.convs.Conv2d_1              [104, 104, 3, 3]   [1, 104, 14, 14]   
155_layer3.2.bns.BatchNorm2d_1                      [104]   [1, 104, 14, 14]   
156_layer3.2.ReLU_relu                                  -   [1, 104, 14, 14]   
157_layer3.2.convs.Conv2d_2              [104, 104, 3, 3]   [1, 104, 14, 14]   
158_layer3.2.bns.BatchNorm2d_2                      [104]   [1, 104, 14, 14]   
159_layer3.2.ReLU_relu                                  -   [1, 104, 14, 14]   
160_layer3.2.Conv2d_conv3               [416, 1024, 1, 1]  [1, 1024, 14, 14]   
161_layer3.2.BatchNorm2d_bn3                       [1024]  [1, 1024, 14, 14]   
162_layer3.2.ReLU_relu                                  -  [1, 1024, 14, 14]   
163_layer3.3.Conv2d_conv1               [1024, 416, 1, 1]   [1, 416, 14, 14]   
164_layer3.3.BatchNorm2d_bn1                        [416]   [1, 416, 14, 14]   
165_layer3.3.ReLU_relu                                  -   [1, 416, 14, 14]   
166_layer3.3.convs.Conv2d_0              [104, 104, 3, 3]   [1, 104, 14, 14]   
167_layer3.3.bns.BatchNorm2d_0                      [104]   [1, 104, 14, 14]   
168_layer3.3.ReLU_relu                                  -   [1, 104, 14, 14]   
169_layer3.3.convs.Conv2d_1              [104, 104, 3, 3]   [1, 104, 14, 14]   
170_layer3.3.bns.BatchNorm2d_1                      [104]   [1, 104, 14, 14]   
171_layer3.3.ReLU_relu                                  -   [1, 104, 14, 14]   
172_layer3.3.convs.Conv2d_2              [104, 104, 3, 3]   [1, 104, 14, 14]   
173_layer3.3.bns.BatchNorm2d_2                      [104]   [1, 104, 14, 14]   
174_layer3.3.ReLU_relu                                  -   [1, 104, 14, 14]   
175_layer3.3.Conv2d_conv3               [416, 1024, 1, 1]  [1, 1024, 14, 14]   
176_layer3.3.BatchNorm2d_bn3                       [1024]  [1, 1024, 14, 14]   
177_layer3.3.ReLU_relu                                  -  [1, 1024, 14, 14]   
178_layer3.4.Conv2d_conv1               [1024, 416, 1, 1]   [1, 416, 14, 14]   
179_layer3.4.BatchNorm2d_bn1                        [416]   [1, 416, 14, 14]   
180_layer3.4.ReLU_relu                                  -   [1, 416, 14, 14]   
181_layer3.4.convs.Conv2d_0              [104, 104, 3, 3]   [1, 104, 14, 14]   
182_layer3.4.bns.BatchNorm2d_0                      [104]   [1, 104, 14, 14]   
183_layer3.4.ReLU_relu                                  -   [1, 104, 14, 14]   
184_layer3.4.convs.Conv2d_1              [104, 104, 3, 3]   [1, 104, 14, 14]   
185_layer3.4.bns.BatchNorm2d_1                      [104]   [1, 104, 14, 14]   
186_layer3.4.ReLU_relu                                  -   [1, 104, 14, 14]   
187_layer3.4.convs.Conv2d_2              [104, 104, 3, 3]   [1, 104, 14, 14]   
188_layer3.4.bns.BatchNorm2d_2                      [104]   [1, 104, 14, 14]   
189_layer3.4.ReLU_relu                                  -   [1, 104, 14, 14]   
190_layer3.4.Conv2d_conv3               [416, 1024, 1, 1]  [1, 1024, 14, 14]   
191_layer3.4.BatchNorm2d_bn3                       [1024]  [1, 1024, 14, 14]   
192_layer3.4.ReLU_relu                                  -  [1, 1024, 14, 14]   
193_layer3.5.Conv2d_conv1               [1024, 416, 1, 1]   [1, 416, 14, 14]   
194_layer3.5.BatchNorm2d_bn1                        [416]   [1, 416, 14, 14]   
195_layer3.5.ReLU_relu                                  -   [1, 416, 14, 14]   
196_layer3.5.convs.Conv2d_0              [104, 104, 3, 3]   [1, 104, 14, 14]   
197_layer3.5.bns.BatchNorm2d_0                      [104]   [1, 104, 14, 14]   
198_layer3.5.ReLU_relu                                  -   [1, 104, 14, 14]   
199_layer3.5.convs.Conv2d_1              [104, 104, 3, 3]   [1, 104, 14, 14]   
200_layer3.5.bns.BatchNorm2d_1                      [104]   [1, 104, 14, 14]   
201_layer3.5.ReLU_relu                                  -   [1, 104, 14, 14]   
202_layer3.5.convs.Conv2d_2              [104, 104, 3, 3]   [1, 104, 14, 14]   
203_layer3.5.bns.BatchNorm2d_2                      [104]   [1, 104, 14, 14]   
204_layer3.5.ReLU_relu                                  -   [1, 104, 14, 14]   
205_layer3.5.Conv2d_conv3               [416, 1024, 1, 1]  [1, 1024, 14, 14]   
206_layer3.5.BatchNorm2d_bn3                       [1024]  [1, 1024, 14, 14]   
207_layer3.5.ReLU_relu                                  -  [1, 1024, 14, 14]   
208_layer4.0.Conv2d_conv1               [1024, 832, 1, 1]   [1, 832, 14, 14]   
209_layer4.0.BatchNorm2d_bn1                        [832]   [1, 832, 14, 14]   
210_layer4.0.ReLU_relu                                  -   [1, 832, 14, 14]   
211_layer4.0.convs.Conv2d_0              [208, 208, 3, 3]     [1, 208, 7, 7]   
212_layer4.0.bns.BatchNorm2d_0                      [208]     [1, 208, 7, 7]   
213_layer4.0.ReLU_relu                                  -     [1, 208, 7, 7]   
214_layer4.0.convs.Conv2d_1              [208, 208, 3, 3]     [1, 208, 7, 7]   
215_layer4.0.bns.BatchNorm2d_1                      [208]     [1, 208, 7, 7]   
216_layer4.0.ReLU_relu                                  -     [1, 208, 7, 7]   
217_layer4.0.convs.Conv2d_2              [208, 208, 3, 3]     [1, 208, 7, 7]   
218_layer4.0.bns.BatchNorm2d_2                      [208]     [1, 208, 7, 7]   
219_layer4.0.ReLU_relu                                  -     [1, 208, 7, 7]   
220_layer4.0.AvgPool2d_pool                             -     [1, 208, 7, 7]   
221_layer4.0.Conv2d_conv3               [832, 2048, 1, 1]    [1, 2048, 7, 7]   
222_layer4.0.BatchNorm2d_bn3                       [2048]    [1, 2048, 7, 7]   
223_layer4.0.downsample.Conv2d_0       [1024, 2048, 1, 1]    [1, 2048, 7, 7]   
224_layer4.0.downsample.BatchNorm2d_1              [2048]    [1, 2048, 7, 7]   
225_layer4.0.ReLU_relu                                  -    [1, 2048, 7, 7]   
226_layer4.1.Conv2d_conv1               [2048, 832, 1, 1]     [1, 832, 7, 7]   
227_layer4.1.BatchNorm2d_bn1                        [832]     [1, 832, 7, 7]   
228_layer4.1.ReLU_relu                                  -     [1, 832, 7, 7]   
229_layer4.1.convs.Conv2d_0              [208, 208, 3, 3]     [1, 208, 7, 7]   
230_layer4.1.bns.BatchNorm2d_0                      [208]     [1, 208, 7, 7]   
231_layer4.1.ReLU_relu                                  -     [1, 208, 7, 7]   
232_layer4.1.convs.Conv2d_1              [208, 208, 3, 3]     [1, 208, 7, 7]   
233_layer4.1.bns.BatchNorm2d_1                      [208]     [1, 208, 7, 7]   
234_layer4.1.ReLU_relu                                  -     [1, 208, 7, 7]   
235_layer4.1.convs.Conv2d_2              [208, 208, 3, 3]     [1, 208, 7, 7]   
236_layer4.1.bns.BatchNorm2d_2                      [208]     [1, 208, 7, 7]   
237_layer4.1.ReLU_relu                                  -     [1, 208, 7, 7]   
238_layer4.1.Conv2d_conv3               [832, 2048, 1, 1]    [1, 2048, 7, 7]   
239_layer4.1.BatchNorm2d_bn3                       [2048]    [1, 2048, 7, 7]   
240_layer4.1.ReLU_relu                                  -    [1, 2048, 7, 7]   
241_layer4.2.Conv2d_conv1               [2048, 832, 1, 1]     [1, 832, 7, 7]   
242_layer4.2.BatchNorm2d_bn1                        [832]     [1, 832, 7, 7]   
243_layer4.2.ReLU_relu                                  -     [1, 832, 7, 7]   
244_layer4.2.convs.Conv2d_0              [208, 208, 3, 3]     [1, 208, 7, 7]   
245_layer4.2.bns.BatchNorm2d_0                      [208]     [1, 208, 7, 7]   
246_layer4.2.ReLU_relu                                  -     [1, 208, 7, 7]   
247_layer4.2.convs.Conv2d_1              [208, 208, 3, 3]     [1, 208, 7, 7]   
248_layer4.2.bns.BatchNorm2d_1                      [208]     [1, 208, 7, 7]   
249_layer4.2.ReLU_relu                                  -     [1, 208, 7, 7]   
250_layer4.2.convs.Conv2d_2              [208, 208, 3, 3]     [1, 208, 7, 7]   
251_layer4.2.bns.BatchNorm2d_2                      [208]     [1, 208, 7, 7]   
252_layer4.2.ReLU_relu                                  -     [1, 208, 7, 7]   
253_layer4.2.Conv2d_conv3               [832, 2048, 1, 1]    [1, 2048, 7, 7]   
254_layer4.2.BatchNorm2d_bn3                       [2048]    [1, 2048, 7, 7]   
255_layer4.2.ReLU_relu                                  -    [1, 2048, 7, 7]   
256_avgpool                                             -    [1, 2048, 1, 1]   
257_fc                                       [2048, 1000]          [1, 1000]   

                                          Params    Mult-Adds  
Layer                                                          
0_conv1                                   9.408k  118.013952M  
1_bn1                                      128.0         64.0  
2_relu                                         -            -  
3_maxpool                                      -            -  
4_layer1.0.Conv2d_conv1                   6.656k   20.873216M  
5_layer1.0.BatchNorm2d_bn1                 208.0        104.0  
6_layer1.0.ReLU_relu                           -            -  
7_layer1.0.convs.Conv2d_0                 6.084k   19.079424M  
8_layer1.0.bns.BatchNorm2d_0                52.0         26.0  
9_layer1.0.ReLU_relu                           -            -  
10_layer1.0.convs.Conv2d_1                6.084k   19.079424M  
11_layer1.0.bns.BatchNorm2d_1               52.0         26.0  
12_layer1.0.ReLU_relu                          -            -  
13_layer1.0.convs.Conv2d_2                6.084k   19.079424M  
14_layer1.0.bns.BatchNorm2d_2               52.0         26.0  
15_layer1.0.ReLU_relu                          -            -  
16_layer1.0.AvgPool2d_pool                     -            -  
17_layer1.0.Conv2d_conv3                 26.624k   83.492864M  
18_layer1.0.BatchNorm2d_bn3                512.0        256.0  
19_layer1.0.downsample.Conv2d_0          16.384k   51.380224M  
20_layer1.0.downsample.BatchNorm2d_1       512.0        256.0  
21_layer1.0.ReLU_relu                          -            -  
22_layer1.1.Conv2d_conv1                 26.624k   83.492864M  
23_layer1.1.BatchNorm2d_bn1                208.0        104.0  
24_layer1.1.ReLU_relu                          -            -  
25_layer1.1.convs.Conv2d_0                6.084k   19.079424M  
26_layer1.1.bns.BatchNorm2d_0               52.0         26.0  
27_layer1.1.ReLU_relu                          -            -  
28_layer1.1.convs.Conv2d_1                6.084k   19.079424M  
29_layer1.1.bns.BatchNorm2d_1               52.0         26.0  
30_layer1.1.ReLU_relu                          -            -  
31_layer1.1.convs.Conv2d_2                6.084k   19.079424M  
32_layer1.1.bns.BatchNorm2d_2               52.0         26.0  
33_layer1.1.ReLU_relu                          -            -  
34_layer1.1.Conv2d_conv3                 26.624k   83.492864M  
35_layer1.1.BatchNorm2d_bn3                512.0        256.0  
36_layer1.1.ReLU_relu                          -            -  
37_layer1.2.Conv2d_conv1                 26.624k   83.492864M  
38_layer1.2.BatchNorm2d_bn1                208.0        104.0  
39_layer1.2.ReLU_relu                          -            -  
40_layer1.2.convs.Conv2d_0                6.084k   19.079424M  
41_layer1.2.bns.BatchNorm2d_0               52.0         26.0  
42_layer1.2.ReLU_relu                          -            -  
43_layer1.2.convs.Conv2d_1                6.084k   19.079424M  
44_layer1.2.bns.BatchNorm2d_1               52.0         26.0  
45_layer1.2.ReLU_relu                          -            -  
46_layer1.2.convs.Conv2d_2                6.084k   19.079424M  
47_layer1.2.bns.BatchNorm2d_2               52.0         26.0  
48_layer1.2.ReLU_relu                          -            -  
49_layer1.2.Conv2d_conv3                 26.624k   83.492864M  
50_layer1.2.BatchNorm2d_bn3                512.0        256.0  
51_layer1.2.ReLU_relu                          -            -  
52_layer2.0.Conv2d_conv1                 53.248k  166.985728M  
53_layer2.0.BatchNorm2d_bn1                416.0        208.0  
54_layer2.0.ReLU_relu                          -            -  
55_layer2.0.convs.Conv2d_0               24.336k   19.079424M  
56_layer2.0.bns.BatchNorm2d_0              104.0         52.0  
57_layer2.0.ReLU_relu                          -            -  
58_layer2.0.convs.Conv2d_1               24.336k   19.079424M  
59_layer2.0.bns.BatchNorm2d_1              104.0         52.0  
60_layer2.0.ReLU_relu                          -            -  
61_layer2.0.convs.Conv2d_2               24.336k   19.079424M  
62_layer2.0.bns.BatchNorm2d_2              104.0         52.0  
63_layer2.0.ReLU_relu                          -            -  
64_layer2.0.AvgPool2d_pool                     -            -  
65_layer2.0.Conv2d_conv3                106.496k   83.492864M  
66_layer2.0.BatchNorm2d_bn3               1.024k        512.0  
67_layer2.0.downsample.Conv2d_0         131.072k  102.760448M  
68_layer2.0.downsample.BatchNorm2d_1      1.024k        512.0  
69_layer2.0.ReLU_relu                          -            -  
70_layer2.1.Conv2d_conv1                106.496k   83.492864M  
71_layer2.1.BatchNorm2d_bn1                416.0        208.0  
72_layer2.1.ReLU_relu                          -            -  
73_layer2.1.convs.Conv2d_0               24.336k   19.079424M  
74_layer2.1.bns.BatchNorm2d_0              104.0         52.0  
75_layer2.1.ReLU_relu                          -            -  
76_layer2.1.convs.Conv2d_1               24.336k   19.079424M  
77_layer2.1.bns.BatchNorm2d_1              104.0         52.0  
78_layer2.1.ReLU_relu                          -            -  
79_layer2.1.convs.Conv2d_2               24.336k   19.079424M  
80_layer2.1.bns.BatchNorm2d_2              104.0         52.0  
81_layer2.1.ReLU_relu                          -            -  
82_layer2.1.Conv2d_conv3                106.496k   83.492864M  
83_layer2.1.BatchNorm2d_bn3               1.024k        512.0  
84_layer2.1.ReLU_relu                          -            -  
85_layer2.2.Conv2d_conv1                106.496k   83.492864M  
86_layer2.2.BatchNorm2d_bn1                416.0        208.0  
87_layer2.2.ReLU_relu                          -            -  
88_layer2.2.convs.Conv2d_0               24.336k   19.079424M  
89_layer2.2.bns.BatchNorm2d_0              104.0         52.0  
90_layer2.2.ReLU_relu                          -            -  
91_layer2.2.convs.Conv2d_1               24.336k   19.079424M  
92_layer2.2.bns.BatchNorm2d_1              104.0         52.0  
93_layer2.2.ReLU_relu                          -            -  
94_layer2.2.convs.Conv2d_2               24.336k   19.079424M  
95_layer2.2.bns.BatchNorm2d_2              104.0         52.0  
96_layer2.2.ReLU_relu                          -            -  
97_layer2.2.Conv2d_conv3                106.496k   83.492864M  
98_layer2.2.BatchNorm2d_bn3               1.024k        512.0  
99_layer2.2.ReLU_relu                          -            -  
100_layer2.3.Conv2d_conv1               106.496k   83.492864M  
101_layer2.3.BatchNorm2d_bn1               416.0        208.0  
102_layer2.3.ReLU_relu                         -            -  
103_layer2.3.convs.Conv2d_0              24.336k   19.079424M  
104_layer2.3.bns.BatchNorm2d_0             104.0         52.0  
105_layer2.3.ReLU_relu                         -            -  
106_layer2.3.convs.Conv2d_1              24.336k   19.079424M  
107_layer2.3.bns.BatchNorm2d_1             104.0         52.0  
108_layer2.3.ReLU_relu                         -            -  
109_layer2.3.convs.Conv2d_2              24.336k   19.079424M  
110_layer2.3.bns.BatchNorm2d_2             104.0         52.0  
111_layer2.3.ReLU_relu                         -            -  
112_layer2.3.Conv2d_conv3               106.496k   83.492864M  
113_layer2.3.BatchNorm2d_bn3              1.024k        512.0  
114_layer2.3.ReLU_relu                         -            -  
115_layer3.0.Conv2d_conv1               212.992k  166.985728M  
116_layer3.0.BatchNorm2d_bn1               832.0        416.0  
117_layer3.0.ReLU_relu                         -            -  
118_layer3.0.convs.Conv2d_0              97.344k   19.079424M  
119_layer3.0.bns.BatchNorm2d_0             208.0        104.0  
120_layer3.0.ReLU_relu                         -            -  
121_layer3.0.convs.Conv2d_1              97.344k   19.079424M  
122_layer3.0.bns.BatchNorm2d_1             208.0        104.0  
123_layer3.0.ReLU_relu                         -            -  
124_layer3.0.convs.Conv2d_2              97.344k   19.079424M  
125_layer3.0.bns.BatchNorm2d_2             208.0        104.0  
126_layer3.0.ReLU_relu                         -            -  
127_layer3.0.AvgPool2d_pool                    -            -  
128_layer3.0.Conv2d_conv3               425.984k   83.492864M  
129_layer3.0.BatchNorm2d_bn3              2.048k       1.024k  
130_layer3.0.downsample.Conv2d_0        524.288k  102.760448M  
131_layer3.0.downsample.BatchNorm2d_1     2.048k       1.024k  
132_layer3.0.ReLU_relu                         -            -  
133_layer3.1.Conv2d_conv1               425.984k   83.492864M  
134_layer3.1.BatchNorm2d_bn1               832.0        416.0  
135_layer3.1.ReLU_relu                         -            -  
136_layer3.1.convs.Conv2d_0              97.344k   19.079424M  
137_layer3.1.bns.BatchNorm2d_0             208.0        104.0  
138_layer3.1.ReLU_relu                         -            -  
139_layer3.1.convs.Conv2d_1              97.344k   19.079424M  
140_layer3.1.bns.BatchNorm2d_1             208.0        104.0  
141_layer3.1.ReLU_relu                         -            -  
142_layer3.1.convs.Conv2d_2              97.344k   19.079424M  
143_layer3.1.bns.BatchNorm2d_2             208.0        104.0  
144_layer3.1.ReLU_relu                         -            -  
145_layer3.1.Conv2d_conv3               425.984k   83.492864M  
146_layer3.1.BatchNorm2d_bn3              2.048k       1.024k  
147_layer3.1.ReLU_relu                         -            -  
148_layer3.2.Conv2d_conv1               425.984k   83.492864M  
149_layer3.2.BatchNorm2d_bn1               832.0        416.0  
150_layer3.2.ReLU_relu                         -            -  
151_layer3.2.convs.Conv2d_0              97.344k   19.079424M  
152_layer3.2.bns.BatchNorm2d_0             208.0        104.0  
153_layer3.2.ReLU_relu                         -            -  
154_layer3.2.convs.Conv2d_1              97.344k   19.079424M  
155_layer3.2.bns.BatchNorm2d_1             208.0        104.0  
156_layer3.2.ReLU_relu                         -            -  
157_layer3.2.convs.Conv2d_2              97.344k   19.079424M  
158_layer3.2.bns.BatchNorm2d_2             208.0        104.0  
159_layer3.2.ReLU_relu                         -            -  
160_layer3.2.Conv2d_conv3               425.984k   83.492864M  
161_layer3.2.BatchNorm2d_bn3              2.048k       1.024k  
162_layer3.2.ReLU_relu                         -            -  
163_layer3.3.Conv2d_conv1               425.984k   83.492864M  
164_layer3.3.BatchNorm2d_bn1               832.0        416.0  
165_layer3.3.ReLU_relu                         -            -  
166_layer3.3.convs.Conv2d_0              97.344k   19.079424M  
167_layer3.3.bns.BatchNorm2d_0             208.0        104.0  
168_layer3.3.ReLU_relu                         -            -  
169_layer3.3.convs.Conv2d_1              97.344k   19.079424M  
170_layer3.3.bns.BatchNorm2d_1             208.0        104.0  
171_layer3.3.ReLU_relu                         -            -  
172_layer3.3.convs.Conv2d_2              97.344k   19.079424M  
173_layer3.3.bns.BatchNorm2d_2             208.0        104.0  
174_layer3.3.ReLU_relu                         -            -  
175_layer3.3.Conv2d_conv3               425.984k   83.492864M  
176_layer3.3.BatchNorm2d_bn3              2.048k       1.024k  
177_layer3.3.ReLU_relu                         -            -  
178_layer3.4.Conv2d_conv1               425.984k   83.492864M  
179_layer3.4.BatchNorm2d_bn1               832.0        416.0  
180_layer3.4.ReLU_relu                         -            -  
181_layer3.4.convs.Conv2d_0              97.344k   19.079424M  
182_layer3.4.bns.BatchNorm2d_0             208.0        104.0  
183_layer3.4.ReLU_relu                         -            -  
184_layer3.4.convs.Conv2d_1              97.344k   19.079424M  
185_layer3.4.bns.BatchNorm2d_1             208.0        104.0  
186_layer3.4.ReLU_relu                         -            -  
187_layer3.4.convs.Conv2d_2              97.344k   19.079424M  
188_layer3.4.bns.BatchNorm2d_2             208.0        104.0  
189_layer3.4.ReLU_relu                         -            -  
190_layer3.4.Conv2d_conv3               425.984k   83.492864M  
191_layer3.4.BatchNorm2d_bn3              2.048k       1.024k  
192_layer3.4.ReLU_relu                         -            -  
193_layer3.5.Conv2d_conv1               425.984k   83.492864M  
194_layer3.5.BatchNorm2d_bn1               832.0        416.0  
195_layer3.5.ReLU_relu                         -            -  
196_layer3.5.convs.Conv2d_0              97.344k   19.079424M  
197_layer3.5.bns.BatchNorm2d_0             208.0        104.0  
198_layer3.5.ReLU_relu                         -            -  
199_layer3.5.convs.Conv2d_1              97.344k   19.079424M  
200_layer3.5.bns.BatchNorm2d_1             208.0        104.0  
201_layer3.5.ReLU_relu                         -            -  
202_layer3.5.convs.Conv2d_2              97.344k   19.079424M  
203_layer3.5.bns.BatchNorm2d_2             208.0        104.0  
204_layer3.5.ReLU_relu                         -            -  
205_layer3.5.Conv2d_conv3               425.984k   83.492864M  
206_layer3.5.BatchNorm2d_bn3              2.048k       1.024k  
207_layer3.5.ReLU_relu                         -            -  
208_layer4.0.Conv2d_conv1               851.968k  166.985728M  
209_layer4.0.BatchNorm2d_bn1              1.664k        832.0  
210_layer4.0.ReLU_relu                         -            -  
211_layer4.0.convs.Conv2d_0             389.376k   19.079424M  
212_layer4.0.bns.BatchNorm2d_0             416.0        208.0  
213_layer4.0.ReLU_relu                         -            -  
214_layer4.0.convs.Conv2d_1             389.376k   19.079424M  
215_layer4.0.bns.BatchNorm2d_1             416.0        208.0  
216_layer4.0.ReLU_relu                         -            -  
217_layer4.0.convs.Conv2d_2             389.376k   19.079424M  
218_layer4.0.bns.BatchNorm2d_2             416.0        208.0  
219_layer4.0.ReLU_relu                         -            -  
220_layer4.0.AvgPool2d_pool                    -            -  
221_layer4.0.Conv2d_conv3              1.703936M   83.492864M  
222_layer4.0.BatchNorm2d_bn3              4.096k       2.048k  
223_layer4.0.downsample.Conv2d_0       2.097152M  102.760448M  
224_layer4.0.downsample.BatchNorm2d_1     4.096k       2.048k  
225_layer4.0.ReLU_relu                         -            -  
226_layer4.1.Conv2d_conv1              1.703936M   83.492864M  
227_layer4.1.BatchNorm2d_bn1              1.664k        832.0  
228_layer4.1.ReLU_relu                         -            -  
229_layer4.1.convs.Conv2d_0             389.376k   19.079424M  
230_layer4.1.bns.BatchNorm2d_0             416.0        208.0  
231_layer4.1.ReLU_relu                         -            -  
232_layer4.1.convs.Conv2d_1             389.376k   19.079424M  
233_layer4.1.bns.BatchNorm2d_1             416.0        208.0  
234_layer4.1.ReLU_relu                         -            -  
235_layer4.1.convs.Conv2d_2             389.376k   19.079424M  
236_layer4.1.bns.BatchNorm2d_2             416.0        208.0  
237_layer4.1.ReLU_relu                         -            -  
238_layer4.1.Conv2d_conv3              1.703936M   83.492864M  
239_layer4.1.BatchNorm2d_bn3              4.096k       2.048k  
240_layer4.1.ReLU_relu                         -            -  
241_layer4.2.Conv2d_conv1              1.703936M   83.492864M  
242_layer4.2.BatchNorm2d_bn1              1.664k        832.0  
243_layer4.2.ReLU_relu                         -            -  
244_layer4.2.convs.Conv2d_0             389.376k   19.079424M  
245_layer4.2.bns.BatchNorm2d_0             416.0        208.0  
246_layer4.2.ReLU_relu                         -            -  
247_layer4.2.convs.Conv2d_1             389.376k   19.079424M  
248_layer4.2.bns.BatchNorm2d_1             416.0        208.0  
249_layer4.2.ReLU_relu                         -            -  
250_layer4.2.convs.Conv2d_2             389.376k   19.079424M  
251_layer4.2.bns.BatchNorm2d_2             416.0        208.0  
252_layer4.2.ReLU_relu                         -            -  
253_layer4.2.Conv2d_conv3              1.703936M   83.492864M  
254_layer4.2.BatchNorm2d_bn3              4.096k       2.048k  
255_layer4.2.ReLU_relu                         -            -  
256_avgpool                                    -            -  
257_fc                                    2.049M       2.048M  
----------------------------------------------------------------------------------------------------
                           Totals
Total params            25.69912M
Trainable params        25.69912M
Non-trainable params          0.0
Mult-Adds             4.25519621G
====================================================================================================
                                   Kernel Shape  ...    Mult-Adds
Layer                                            ...             
0_conv1                           [3, 64, 7, 7]  ...  118013952.0
1_bn1                                      [64]  ...         64.0
2_relu                                        -  ...          NaN
3_maxpool                                     -  ...          NaN
4_layer1.0.Conv2d_conv1         [64, 104, 1, 1]  ...   20873216.0
...                                         ...  ...          ...
253_layer4.2.Conv2d_conv3     [832, 2048, 1, 1]  ...   83492864.0
254_layer4.2.BatchNorm2d_bn3             [2048]  ...       2048.0
255_layer4.2.ReLU_relu                        -  ...          NaN
256_avgpool                                   -  ...          NaN
257_fc                             [2048, 1000]  ...    2048000.0

[258 rows x 4 columns]
(1, 1000)
