import matplotlib.pyplot as plt  # ✅ Make sure this import is included

def nrz_l_encode(bits):
    # 1 → High (1), 0 → Low (0)
    return [1 if bit == 1 else 0 for bit in bits]

# Input binary sequence
bits = [1, 0, 1, 1, 0, 0, 1, 0]

# Encode using NRZ-L
encoded_signal = nrz_l_encode(bits)

# Plotting
plt.step(range(len(encoded_signal)), encoded_signal, where='post')
plt.ylim(-0.5, 1.5)
plt.title("NRZ-L Encoding")
plt.xlabel("Bit Index")
plt.ylabel("Signal Level")
plt.grid(True)
plt.show()
