import matplotlib.pyplot as plt
import matplotlib.patches as patches

a, b = plt.subplots()

hitam = patches.Rectangle((0, 0.66), 1, 0.33, facecolor='black')
b.add_patch(hitam)

putih = patches.Rectangle((0, 0.33), 1, 0.33, facecolor='white')
b.add_patch(putih)

hijau = patches.Rectangle((0, 0), 1, 0.33, facecolor='green')
b.add_patch(hijau)

merah = patches.Polygon([[0, 0], [0, 1], [0.5, 0.5]], closed=True, facecolor='red')
b.add_patch(merah)


plt.show()