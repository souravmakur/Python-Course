def counter(s):
  vowel_count = 0
  consonant_count = 0

  for i in s:
    if i in "aeiouAEIOU":
      vowel_count = vowel_count + 1
    else:
      consonant_count = consonant_count + 1
  ans = f"There are {vowel_count} vowels and {consonant_count} consonants in {s}"
  return "".join(ans)

alphabets = "abcdefghijklmnopqrstuvwxyz"
print(counter(alphabets))