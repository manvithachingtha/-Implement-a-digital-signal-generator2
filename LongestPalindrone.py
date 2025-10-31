import matplotlib.pyplot as plt

def longest_palindrome(bits):
    s = ''.join(map(str, bits))
    n = len(s)
    start = 0
    max_len = 1
    for i in range(n):
        for j in range(i + max_len, n + 1):
            if s[i:j] == s[i:j][::-1]:
                start = i
                max_len = j - i
    return start, start + max_len  # Return indices

# Input binary stream
bits = [1, 0, 1, 1, 0, 0, 1, 0]

# Find longest palindrome indices
start, end = longest_palindrome(bits)
print("Longest Palindrome:", bits[start:end])

# Plotting
colors = ['red' if start <= i < end else 'blue' for i in range(len(bits))]
plt.bar(range(len(bits)), bits, color=colors)
plt.ylim(-0.5, 1.5)
plt.title("Longest Palindrome in Bit Stream")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid(True)
plt.show()

