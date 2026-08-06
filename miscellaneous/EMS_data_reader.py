import matplotlib.pyplot as plt

f1 = open("V1.txt", "r")
f2 = open("V2.txt", "r")
f3 = open("V3.txt", "r")
f4 = open("V4.txt", "r")
f5 = open("X.txt", "r")

text1 = f1.read()
text2 = f2.read()
text3 = f3.read()
text4 = f4.read()
text5 = f5.read()

cut1 = text1[26:-2]
cut2 = text2[26:-2]
cut3 = text3[26:-2]
cut4 = text4[26:-2]
cut5 = text5[26:-2]

splcut1 = cut1.split(" ")
splcut2 = cut2.split(" ")
splcut3 = cut3.split(" ")
splcut4 = cut4.split(" ")
splcut5 = cut5.split(" ")

x = []
y1 = []
y2 = []
y3 = []
y4 = []
for i in range(len(splcut1)):
    y1.append(float(splcut1[i]))
    y2.append(float(splcut2[i]))
    y3.append(float(splcut3[i]))
    y4.append(float(splcut4[i]))
    x.append(float(splcut5[i]))

r1 = open("V1_column.txt", "w")
r2 = open("V2_column.txt", "w")
r3 = open("V3_column.txt", "w")
r4 = open("V4_column.txt", "w")
r5 = open("X_column.txt", "w")

for j in range(len(y1)):
    r1.write(str(y1[j]) + "\n")
    r2.write(str(y2[j]) + "\n")
    r3.write(str(y3[j]) + "\n")
    r4.write(str(y4[j]) + "\n")
    r5.write(str(x[j]) + "\n")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

fig1, ax1 = plt.subplots()
ax1.plot(x, y1)
ax1.set_title("V1")
plt.axhline(y=0)
plt.axvline(x=0)

fig2, ax2 = plt.subplots()
ax2.plot(x, y2)
ax2.set_title("V2")
plt.axhline(y=0)
plt.axvline(x=0)

fig3, ax3 = plt.subplots()
ax3.plot(x, y3)
ax3.set_title("V3")
plt.axhline(y=0)
plt.axvline(x=0)

fig4, ax4 = plt.subplots()
ax4.plot(x, y4)
ax4.set_title("V4")
plt.axhline(y=0)
plt.axvline(x=0)


plt.show()
