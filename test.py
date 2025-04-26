from lib import main as wekoptics
import matplotlib.pyplot as plt


plt.imshow(wekoptics.gen(swap_axes=True), cmap='gray')
plt.show()