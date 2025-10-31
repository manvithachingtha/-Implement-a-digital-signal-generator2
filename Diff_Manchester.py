import matplotlib.pyplot as plt

def diff_manchester_encode(bits):
    signal = []
    last = 1
    for bit in bits:
        if bit == 0:
            signal += [last, 1 - last]
        else:
            last = 1 - last
            signal += [last, 1 - last]
    return signal

bits = [1, 0, 1, 1, 0, 0, 1, 0]
encoded = diff_manchester_encode(bits)

plt.step(range(len(encoded)), encoded, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Differential Manchester Encoding")
plt.xlabel("Time")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
