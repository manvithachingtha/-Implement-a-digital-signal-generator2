import matplotlib.pyplot as plt

def pcm_encode(analog):
    min_val = min(analog)
    max_val = max(analog)
    levels = 8  # 3-bit PCM
    step = (max_val - min_val) / (levels - 1)

    quantized = []
    for x in analog:
        index = int(round((x - min_val) / step))
        index = max(0, min(index, levels - 1))
        quantized.append(index)

    bits = []
    for q in quantized:
        bits += [int(b) for b in format(q, '03b')]
    return bits, quantized

# Input analog signal
analog = [0.2, 0.5, 0.8, 0.3, 0.1]

# Encode using PCM
bits, quantized_levels = pcm_encode(analog)
print("PCM Output (bit stream):", bits)

# Plot quantized levels
plt.step(range(len(quantized_levels)), quantized_levels, where='post')
plt.ylim(-1, 8)
plt.title("PCM Quantized Levels")
plt.xlabel("Sample Index")
plt.ylabel("Quantization Level (0–7)")
plt.grid(True)
plt.show()
