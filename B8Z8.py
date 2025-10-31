import matplotlib.pyplot as plt

def b8zs_scramble(bits):
    signal = []
    last = 1
    i = 0
    while i < len(bits):
        if bits[i:i+8] == [0]*8:
            signal += [0, 0, 0, last, -last, 0, -last, last]
            i += 8
        else:
            if bits[i] == 1:
                signal.append(last)
                last *= -1
            else:
                signal.append(0)
            i += 1
    return signal

bits = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
encoded = b8zs_scramble(bits)

plt.step(range(len(encoded)), encoded, where='post')
plt.ylim(-1.5, 1.5)
plt.title("B8ZS Scrambling")
plt.xlabel("Bit Index")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
