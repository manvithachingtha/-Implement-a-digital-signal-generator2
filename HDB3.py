import matplotlib.pyplot as plt

def hdb3_scramble(bits):
    signal = []
    last = 1
    zero_count = 0
    pulse_count = 0
    for bit in bits:
        if bit == 1:
            last *= -1
            signal.append(last)
            pulse_count += 1
            zero_count = 0
        else:
            zero_count += 1
            if zero_count == 4:
                if pulse_count % 2 == 0:
                    signal[-3] = last
                    signal += [0, 0, 0, -last]
                    last *= -1
                else:
                    signal += [0, 0, 0, last]
                pulse_count = 0
                zero_count = 0
            else:
                signal.append(0)
    return signal

bits = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
encoded = hdb3_scramble(bits)

plt.step(range(len(encoded)), encoded, where='post')
plt.ylim(-1.5, 1.5)
plt.title("HDB3 Scrambling")
plt.xlabel("Bit Index")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
