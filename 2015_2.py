with open("2015_2_input.txt") as file:
    presents = file.readlines()

paper_total = ribbon_total = 0

for present in presents:
    l, w, h = sorted(map(int, present.split("x")))
    paper_total += (2*l*w + 2*w*h + 2*h*l) + min([l*w, w*h, h*l])
    ribbon_total += (l*2 + w *2) + l*w*h

print(f'Sqft of wrapping paper needed:{paper_total}')
print(f'Ribbon needed:{ribbon_total}')
