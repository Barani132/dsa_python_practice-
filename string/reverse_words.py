# Problem: Reverse Words in a String
# Category: String

s = "hello world"

result = " ".join(s.split()[::-1])

print("Input:", s)
print("Output:", result)
