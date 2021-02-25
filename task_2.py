line_1 = input().split()
line_2 = input().split()
final_list = line_1 + line_2
print(' '.join(x for x in set(final_list) if final_list.count(x) > 1))
