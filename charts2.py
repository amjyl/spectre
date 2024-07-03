import numpy as np
import matplotlib.pyplot as plt

wls = np.array(list(range(450, 851, 2)))
values1 = []
values2 = []
values3 = []
for i in range(1, 202):
    original_image = np.load(fr"C:\Users\domas\OneDrive\Desktop\results3\figure_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.npy")
    roi1 = original_image[44:44+36, 1247:1247+297] # лист верхний
    roi2 = original_image[460:568, 1164:1285] # лист посередине
    roi3 = original_image[165:209, 1083:1715] # лист нижний
    values1.append(roi1.mean(axis=0).mean())
    values2.append(roi2.mean(axis=0).mean())
    values3.append(roi3.mean(axis=0).mean())
values1 = np.array(values1)
values2 = np.array(values2)
values3 = np.array(values3)
fig, ax = plt.subplots()
ax.plot(wls, values1, color='r', label='лист верхний')
ax.plot(wls, values2, color='g', label='лист посередине')
ax.plot(wls, values3, color='b', label='лист нижний')
ax.set(xlabel='wl (nm)', ylabel='value')
ax.grid()
plt.legend(fontsize='9')
fig.savefig(r"C:\Users\domas\Downloads\res.png")
plt.show()