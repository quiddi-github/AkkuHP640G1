import matplotlib.pyplot as plt

plt.plot([0, 20, 36, 45, 64, 127],[100, 89, 81, 76,66,31])
plt.ylabel('Akkustand in %')
plt.xlabel('Zeit in min.')
plt.axis((0, 130, 0, 110))
plt.suptitle('HP 640 G1 Akkufüllstand')
plt.show()