import os
import sys

input_file=sys.argv[1]
ff = open(input_file, "r")
lines = ff.readlines()
ff.close()

tot_books, tot_lib, day_scan = list(map(int, lines[0].split()))
books = list(map(int, lines[1].split()))
# library = defaultdict(list)
library = dict()
for i in range(tot_lib):
    no_of_b, sign_time, max_ship = list(map(int, lines[2*i+2].split()))
    temp = list(set(map(int, lines[2*i+3].split())))
    if sign_time >= day_scan:
        continue
    # temp = sorted(temp, key=lambda tup: books[tup[0]])
    temp.sort(key=lambda x: books[x], reverse=True)
    # temp = set(temp)
    library[i] = [no_of_b, sign_time, max_ship, temp]

hr_fun = []
weigts_0 = [8/9, 2/9, 1/9]  # try for different values

for i in library:
    summ = 1/(library[i][1]**weigts_0[0])
    ne = 0
    for j in library[i][3]:
        ne += books[j]
    summ *= ne**weigts_0[1]
    summ *= library[i][2]**weigts_0[2]
    hr_fun.append((i, summ))
hr_fun.sort(key=lambda x: x[1], reverse=True)
# print(hr_fun)
open_lib = []
open_set = set()


output = open("out.txt", "w")
# output.write("\n\n")
day = 0
iters = 0
while(day < day_scan and iters < len(library)):

    temp = hr_fun[iters]
    lib = temp[0]

    current_day = day+library[lib][1]
    time_rem = day_scan-current_day
    if time_rem <= 0:
        iters += 1
        continue
    kk = library[lib][3]
    kkk = list(set(kk)-open_set)
    kkk.sort(key=lambda x: books[x], reverse=True)
    max_per_day = library[lib][2]
    if len(kkk) <= 0:
        iters += 1
        continue

    output.write(str(lib))
    output.write(" ")
    best = len(kkk)
    if len(kkk) > time_rem*max_per_day:
        best = time_rem*max_per_day
        open_set = open_set | set(kkk[:time_rem*max_per_day])
        output.write(str(time_rem*max_per_day))
        output.write("\n")
    else:
        open_set = open_set | set(kkk)
        output.write(str(len(kkk)))
        output.write("\n")
    open_lib.append(lib)
    for i in kkk[:best]:
        output.write(str(i))
        output.write(" ")
    output.write("\n")
    # open_set.difference(library[lib][3])
    day += library[lib][1]
    iters += 1
kk = len(open_lib)
output.close()
output = open("kk.txt", "w")
with open("out.txt", "r") as ff:
    output.write(str(kk))
    output.write("\n")
    for lines in ff:
        output.write(lines)

os.system("rm out.txt")
output.close()