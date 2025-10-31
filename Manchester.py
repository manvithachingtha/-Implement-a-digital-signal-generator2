import matplotlib.pyplot as plt

def manchester_encode(bits):
    signal = []
    for bit in bits:
        signal += [1, 0] if bit == 1 else [0, 1]
    return signal

bits = [1, 0, 1, 1, 0, 0, 1, 0]
encoded = manchester_encode(bits)

plt.step(range(len(encoded)), encoded, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Manchester Encoding")
plt.xlabel("Time")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
