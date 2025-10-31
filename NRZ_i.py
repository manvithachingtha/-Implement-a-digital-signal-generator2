import matplotlib.pyplot as plt

def nrz_i_encode(bits):
    signal = []
    level = 0
    for bit in bits:
        if bit == 1:
            level = 1 - level
        signal.append(level)
    return signal

bits = [1, 0, 1, 1, 0, 0, 1, 0]
encoded = nrz_i_encode(bits)

plt.step(range(len(encoded)), encoded, where='post')
plt.ylim(-0.5, 1.5)
plt.title("NRZ-I Encoding")
plt.xlabel("Bit Index")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
