import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

# -------------------- ENCODING --------------------

def encode_nrz_l(data):
    return [1 if bit == '1' else -1 for bit in data]

def encode_nrz_i(data):
    signal = []
    last = -1
    for bit in data:
        if bit == '1':
            last *= -1
        signal.append(last)
    return signal

def encode_manchester(data):
    signal = []
    for bit in data:
        if bit == '1':
            signal.extend([-1, 1])
        else:
            signal.extend([1, -1])
    return signal

def encode_diff_manchester(data):
    signal = []
    last = -1
    for bit in data:
        if bit == '0':
            last *= -1
        signal.extend([last, -last])
    return signal

def encode_ami(data):
    signal = []
    last = 1
    for bit in data:
        if bit == '1':
            signal.append(last)
            last *= -1
        else:
            signal.append(0)
    return signal

def plot_signal(signal, title, filename):
    t = np.arange(0, len(signal), 1)
    plt.figure(figsize=(10, 2))
    plt.step(t, signal, where='post')
    plt.ylim(-2, 2)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()  # Show the graph
    plt.close()

    # Auto-open the image (platform-specific)
    try:
        if os.name == 'posix':
            os.system(f'xdg-open {filename}')  # Linux
        elif os.name == 'mac':
            os.system(f'open {filename}')      # macOS
        elif os.name == 'nt':
            os.startfile(filename)             # Windows
    except Exception as e:
        print(f"⚠️ Could not open image automatically: {e}")

# -------------------- DECODING --------------------

def decode_nrz_l_from_image(image_path, bit_count):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    step = width // bit_count
    bits = ''
    for i in range(bit_count):
        col = img[:, i * step + step // 2]
        avg = np.mean(col)
        bits += '1' if avg < 128 else '0'
    return bits

def decode_nrz_i_from_image(image_path, bit_count):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    step = width // bit_count
    bits = ''
    last = None
    for i in range(bit_count):
        col = img[:, i * step + step // 2]
        avg = np.mean(col)
        level = 1 if avg < 128 else -1
        if last is None:
            bits += '1' if level == 1 else '0'
        else:
            bits += '1' if level != last else '0'
        last = level
    return bits

def decode_manchester_from_image(image_path, bit_count):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    step = width // (2 * bit_count)
    bits = ''
    for i in range(bit_count):
        left = np.mean(img[:, i * 2 * step + step // 2])
        right = np.mean(img[:, i * 2 * step + 3 * step // 2])
        bits += '1' if left < right else '0'
    return bits

def decode_diff_manchester_from_image(image_path, bit_count):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    step = width // (2 * bit_count)
    bits = ''
    last_transition = None
    for i in range(bit_count):
        left = np.mean(img[:, i * 2 * step + step // 2])
        right = np.mean(img[:, i * 2 * step + 3 * step // 2])
        transition = left != right
        if last_transition is None:
            bits += '1'
        else:
            bits += '0' if transition else '1'
        last_transition = transition
    return bits

def decode_ami_from_image(image_path, bit_count):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    step = width // bit_count
    bits = ''
    for i in range(bit_count):
        col = img[:, i * step + step // 2]
        avg = np.mean(col)
        bits += '0' if avg > 200 else '1'
    return bits

# -------------------- MAIN --------------------

def main():
    data = input("Enter binary data (e.g., 10110011): ").strip()
    bit_count = len(data)
    print("\nChoose encoding scheme:")
    print("1. NRZ-L\n2. NRZ-I\n3. Manchester\n4. Differential Manchester\n5. AMI")
    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        signal = encode_nrz_l(data)
        scheme = "NRZ-L"
    elif choice == '2':
        signal = encode_nrz_i(data)
        scheme = "NRZ-I"
    elif choice == '3':
        signal = encode_manchester(data)
        scheme = "Manchester"
        bit_count *= 2
    elif choice == '4':
        signal = encode_diff_manchester(data)
        scheme = "Differential Manchester"
        bit_count *= 2
    elif choice == '5':
        signal = encode_ami(data)
        scheme = "AMI"
    else:
        print("Invalid choice.")
        return

    filename = f"{scheme}_encoded.png"
    plot_signal(signal, f"{scheme} Encoding", filename)
    print(f"\n✅ Signal encoded and saved as {filename}")

    decode = input("Do you want to decode the signal from image? (yes/no): ").strip().lower()
    if decode == 'yes':
        if scheme == "NRZ-L":
            decoded = decode_nrz_l_from_image(filename, len(data))
        elif scheme == "NRZ-I":
            decoded = decode_nrz_i_from_image(filename, len(data))
        elif scheme == "Manchester":
            decoded = decode_manchester_from_image(filename, len(data))
        elif scheme == "Differential Manchester":
            decoded = decode_diff_manchester_from_image(filename, len(data))
        elif scheme == "AMI":
            decoded = decode_ami_from_image(filename, len(data))
        else:
            print("Decoding not supported.")
            return
        print("🔁 Decoded signal:", decoded)

if __name__ == "__main__":
    main()


