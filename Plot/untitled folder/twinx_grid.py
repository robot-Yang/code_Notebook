import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

t = np.arange(0.0, 10.01, 0.01)
_, ax1 = plt.subplots()
ax2 = ax1.twinx()

title = 'sin'
s1 = np.sin(np.pi*t)
ax1.plot(t, s1, 'b.')
ax1.set_ylabel(title, color='b', fontsize=18)

title = 'linear'
s2 = t * 1.6
ax2.plot(t, s2, 'g-')
ax2.set_ylabel(title, color='g', fontsize=18)

# 左右縦軸の tick 数を等しくして同じ位置となるようにしている
ax1.set_yticks(np.linspace(-1.0, 1.0, 5))
ax2.set_yticks(np.linspace(0, 20, 5))
ax1.set_ylim(-1.06, 1.06)
ax2.set_ylim(-0.6, 20.6)

ax1.tick_params(labelsize=18)
ax2.tick_params(labelsize=18)
ax1.set_xlabel('time (s)', fontsize=18)
ax1.grid(True, which='both') 
plt.xlim(-0.2, 10.2)
plt.subplots_adjust(left=0.18, right=0.86, bottom=0.14, top=0.94)
plt.show()