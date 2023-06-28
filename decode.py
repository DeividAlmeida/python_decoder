def count_digits_frequency(digits):
  frequency = {str(d): [0, 0, 0] for d in range(10)}

  for digit in digits:
    for i, char in enumerate(digit):
      frequency[char][i] += 1

  return frequency


def rank_digits_by_score(frequency):
  scores = {}

  for digit, counts in frequency.items():
    total_score = sum(counts)
    if total_score > 0:
      score = ( counts[0] * 3 + counts[1] * 2 ) / total_score
      scores[digit] = score

  sorted_digits = sorted(scores, key=scores.get, reverse=True)
  return "".join(sorted_digits)


digits = [
  "319", "680", "180", "690", "129", "620", "762", "689", "762", "318",
  "368", "710", "720", "710", "629", "168", "160", "689", "716", "731",
  "736", "729", "316", "729", "729", "710", "769", "290", "719", "680",
  "318", "389", "162", "289", "162", "718", "729", "319", "790", "680",
  "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"
]

frequency = count_digits_frequency(digits)
sorted_digits = rank_digits_by_score(frequency)

print(sorted_digits)
