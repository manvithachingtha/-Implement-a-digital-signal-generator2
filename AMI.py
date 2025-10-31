import matplotlib.pyplot as plt

def ami_encode(bits):
    signal = []
    last = 1
    for bit in bits:
        if bit == 1:
            signal.append(last)
            last *= -1
        else:
            signal.append(0)
    return signal

bits = [1, 0, 1, 1, 0, 0, 1, 0]
encoded = ami_encode(bits)

plt.step(range(len(encoded)), encoded, where='post')
plt.ylim(-1.5, 1.5)
plt.title("AMI Encoding")
plt.xlabel("Bit Index")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
