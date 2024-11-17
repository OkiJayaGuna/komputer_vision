import matplotlib.pyplot as plt
import matplotlib.patches as patches

a, b = plt.subplots()

merah = patches.Rectangle((0, 0.5), 1, 0.5, facecolor='red')
b.add_patch(merah)

putih = patches.Rectangle((0, 0), 1, 0.5, facecolor='white')
b.add_patch(putih)

plt.show()