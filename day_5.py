import sys

max_seat = -1
seats = set()
for line in open(sys.argv[1]):
    digits = line.strip().replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    seat = int(digits, 2)
    max_seat = max(seat, max_seat)
    print(line.strip(), seat)
    seats.add(seat)

print(max_seat)

for seat in range(min(seats), max(seats)):
    if seat not in seats and seat-1 in seats and seat+1 in seats:
        print(seat, 'missing')

