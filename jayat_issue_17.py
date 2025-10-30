#typing speed and accuracy test

import time

text = "python makes coding fun and powerful"
print("Type this:\n", text)
input("Press Enter when ready...")

start = time.time()
typed = input("\nStart typing:\n")
end = time.time()

elapsed = end - start
words = len(typed.split())
wpm = words / (elapsed / 60)
accuracy = sum(1 for a, b in zip(typed, text) if a == b) / len(text) * 100

print(f"\nTime: {elapsed:.2f}s")
print(f"WPM: {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")
