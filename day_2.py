n_valid = 0
n_valid_2 = 0

for line in open('2.txt'):
    lo_hi, char, password = line.strip().split()
    lo, hi = map(int, lo_hi.split('-'))
    char = char.rstrip(':')

    n_matches = sum(int(c == char) for c in password)
    n_valid += int(lo <= n_matches <= hi)

    n_matches_2 = int(password[lo - 1] == char) + int(password[hi - 1] == char)
    n_valid_2 += int(n_matches_2 == 1)


print(n_valid)
print(n_valid_2)
