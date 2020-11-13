def num_to_words(n):  # supports up to 1000
    if n == 1000:
        return "one thousand"
    if n >= 100:
        if n % 100 == 0:
            return f"{num_to_words(n // 100)} hundred"
        return f"{num_to_words(n // 100)} hundred and {num_to_words(n % 100)}"
    if n >= 20:
        if n % 10 == 0:
            return ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n // 10]
        return f"{['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n // 10]}" \
               f"-{num_to_words(n % 10)}"
    return [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ][n]


def world_letter_count(s):
    return len(s.replace(" ", "").replace("-", ""))


s = 0
for i in range(1, 1001):
    s += world_letter_count(num_to_words(i))
    if i < 25:
        print(num_to_words(i))
print(s)
