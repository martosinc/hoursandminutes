n = int(input())
print(f'Прошло {n // 60} часов' + ' ' + ('и ' + str(n % 60) + ' минуты' if n % 60 != 0 else ''))