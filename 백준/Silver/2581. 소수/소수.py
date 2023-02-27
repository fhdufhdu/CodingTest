from sys import stdin, stdout

read = stdin.readline
write = stdout.write

def sosu_list(start, end):
    sosu = [True for i in range(end+1)]
    sosu[0] = False
    sosu[1] = False
    result = []
    for number, is_sosu in enumerate(sosu):
        if is_sosu:
            if start <= number <= end:
                result.append(number)
            a_num = number * 2
            while a_num <= end:
                sosu[a_num] = False
                a_num += number
    
    return result

s = int(read().rstrip())
e = int(read().rstrip())

sosu = sosu_list(s, e)
if len(sosu) == 0:
    write("-1")
else:
    m = min(sosu)
    s = sum(sosu)
    write(f"{s}\n{m}")