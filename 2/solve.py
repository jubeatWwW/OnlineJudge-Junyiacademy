n = 15

cnt = 0
for i in range(0, n):
    if (not i % 15) or ((i % 3) and (i % 5)):
        cnt += 1

print(cnt)
