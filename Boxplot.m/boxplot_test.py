import matplotlib.pyplot as plt
import numpy as np

SUS0 = [72.5000,   72.5000,   27.5000,   50.0000,   77.5000,   50.0000,   87.5000,   42.5000]
SUS1 = [95.0000,   70.0000,   70.0000,   75.0000,   82.5000,   70.0000,   87.5000,   87.5000]
SUS0 = [i/25 for i in SUS0]
SUS1 = [i/25 for i in SUS1]
anthrop0 = [3.0000,    2.0000,    1.8000,    2.0000,    3.2000,    1.0000,    2.6000,    0.6000]
anthrop1 = [1.4000,    1.2000,    0.6000,    2.6000,    1.2000,    1.0000,    1.4000,    1.4000]
animacy0 = [3.1667,    2.3333,    2.5000,    2.0000,    3.0000,    1.0000,    2.8333,    1.5000]
animacy1 = [1.8333,    2.3333,    0.6667,    2.1667,    2.3333,    1.1667,    1.6667,    1.6667]
likeability0 = [3.4000,    3.0000,    2.0000,    2.4000,    3.6000,    2.6000,    3.2000,    1.6000]
likeability1 = [3.0000,    3.4000,    2.8000,    2.6000,    3.4000,    2.8000,    2.4000,    2.4000]
intelligence0 = [3.4000,    2.6000,    2.0000,    2.4000,    3.0000,    1.4000,    3.0000,    1.6000]
intelligence1 = [1.4000,    2.8000,    1.8000,    2.6000,    2.8000,    1.6000,    2.2000,    2.2000]
safety0 = [2.0000,    1.3333,    2.3333,    2.3333,    2.6667,    2.0000,    1.6667,    2.0000]
safety1 = [1.6667,    1.3333,    2.3333,    2.3333,    1.3333,    2.0000,    1.6667,    1.6667]

Torso = [SUS0, anthrop0, animacy0, likeability0, intelligence0, safety0]
Joystick = [SUS1, anthrop1, animacy1, likeability1, intelligence1, safety1] 

ticks = ['SUS', 'Anthropomorphism', 'Animacy', 'Likeability', 'Perceived Intelligence', 'Perceived safety']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(Torso, positions=np.array(range(len(Torso)))*2.0-0.4, sym='k+', widths=0.6)
bpr = plt.boxplot(Joystick, positions=np.array(range(len(Joystick)))*2.0+0.4, sym='k+', widths=0.6)
set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Torso')
plt.plot([], c='#2C7BB6', label='Joystick')
plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len (ticks)*2)
# plt.ylim(0, 8)
plt.tight_layout()

plt.savefig('boxcompare.pdf')
plt.show()