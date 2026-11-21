def reverse_slicing(s):
  return s[::-1]

def reverse_a_string(s):
  chars = list(s)
  i = 0
  j = len(chars) - 1

  while i < j:
    chars[i] , chars[j] = chars[j] , chars[i]
    i = i + 1
    j = j - 1
    return "".join(chars)

s = "Sourav"

print(reverse_slicing(s)) #vruoS
print(reverse_a_string(s)) #vruoS