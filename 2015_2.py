with open("2015_2_input.txt") as file:
    presents = file.readlines()

paper_total = 0
ribbon_total = 0

for present in presents:
    l, w, h = sorted(map(int, present.split("x")))
    lw, wh, hl = (l*w), (w*h), (h*l)
    present_sqft = (2*lw + 2*wh + 2*hl) + min([lw, wh, hl])
    paper_total += present_sqft
    ribbon = (l*2 + w *2) + l*w*h
    ribbon_total += ribbon

print(f'Sqft of wrapping paper needed:{paper_total}')
print(f'Ribbon needed:{ribbon_total}')
