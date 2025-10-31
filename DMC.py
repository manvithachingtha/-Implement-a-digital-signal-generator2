import matplotlib.pyplot as plt  # Optional: for plotting

def delta_modulate(analog):
    delta = 0.1  # You can adjust this step size
    prev = analog[0]
    bits = [1]  # Start with 1 to represent the first sample
    for x in analog[1:]:
        if x >= prev:
            bits.append(1)
            prev += delta
        else:
            bits.append(0)
            prev -= delta
    return bits

# Example analog input
analog = [0.2, 0.5, 0.8, 0.3, 0.1]

# Run Delta Modulation
bits = delta_modulate(analog)
print("Delta Modulation Output:", bits)

# Optional: Plot the digital output
plt.step(range(len(bits)), bits, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Delta Modulation")
plt.xlabel("Sample Index")
plt.ylabel("Bit Value")
plt.grid(True)
plt.show()
