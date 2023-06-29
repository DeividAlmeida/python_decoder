def transform_file_to_array(file):
  lines = []

  for line in file:
    line = line.decode('utf-8').strip()
    lines.append(line)

  return lines

def count_digits_frequency(digits):
  frequency = {}

  for digit in digits:
    for i, char in enumerate(digit):
      if i < 3:
        if char not in frequency :
          frequency[char] = [0, 0, 0]
        frequency[char][i] += 1

  return frequency


def rank_digits_by_score(frequency):
  scores = {}

  for digit, counts in frequency.items():
    total_score = sum(counts)
    score = ( counts[0] * 3 + counts[1] * 2 + counts[2]) / total_score
    scores[digit] = score

  sorted_digits = sorted(scores, key=scores.get, reverse=True)
  return "".join(sorted_digits)
