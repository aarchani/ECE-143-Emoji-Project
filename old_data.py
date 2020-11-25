import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
import os
import emoji

# temp1 = pd.read_csv(os.path.join(sys.path[0], 'commentInteractions_cleaned.csv'))
# temp2 = pd.read_csv(os.path.join(sys.path[0], 'comments2emoji_frequency_matrix_cleaned.csv'))
temp3 = pd.read_csv(os.path.join(sys.path[0], '__readervswriter.csv'))
# temp4 = pd.read_csv(os.path.join(sys.path[0], 'ijstable.csv'))
# temp5 = pd.read_csv(os.path.join(sys.path[0], 'votes_cleaned.csv'))

# print(temp1.columns)
# print(temp2.columns)
# print(temp3.columns)
# print(temp4.columns)
# print(temp5.columns)

prop = FontProperties(fname = 'C:\\Windows\\Fonts\\seguiemj.ttf')


emoji_list = []
error_list =[':dancing_woman:',':person_raising_both_hands_in_celebration:', ':clapping_hands_sign:',':christmas_tree:',':multiple_musical_notes:',':thumbs_up_sign:',
            ':face_throwing_a_kiss:', ':face_with_stuck-out_tongue_and_winking_eye:',':ok_hand_sign:',':wrapped_present:',':person_with_folded_hands:',':thumbs_down_sign:',
            ':disappointed_but_relieved_face:',':face_with_cold_sweat:']

sub_list = [':woman_dancing:',':raising_hands:',':clapping_hands:',':Christmas_tree:',':musical_notes:',':thumbs_up:',':face_blowing_a_kiss:', ':winking_face_with_tongue:',
            ':OK_hand:',':wrapped_gift:',':folded_hands:',':thumbs_down:',':sad_but_relieved_face:',':downcast_face_with_sweat:']

for i in range(len(temp3['description'])):
    if ':'+str(temp3['description'][i]).lower().replace(' ','_')+':' not in error_list:
        emoji_list.append(emoji.emojize(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
        # emoji_list.append(emojis.encode(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
    else:
        ind = error_list.index(':'+str(temp3['description'][i]).lower().replace(' ','_')+':')
        emoji_list.append(emoji.emojize(sub_list[ind]))
        # emoji_list.append(emojis.encode(sub_list[ind]))

# print(emoji_list)
p1 = plt.bar(range(len(temp3['s.writer'])),temp3['count'])
# Make labels
for rect1, label in zip(p1, emoji_list):
    height = rect1.get_height()
    plt.annotate(
        label,
        (rect1.get_x() + rect1.get_width()/2, height),
        ha="center",
        va="bottom",
        fontsize=15,
        fontproperties=prop
    )

plt.show()