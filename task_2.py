line_1 = input().split()
line_2 = input().split()
final_list = [x for x in line_1 if x in line_2]
final_list = list(dict.fromkeys(final_list))
print(' '.join(map(str, final_list)))
