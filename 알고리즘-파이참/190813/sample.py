def check_name(stir):
    new_stir = []
    ls = []
    count = 0
    for i in stir:
        new_stir = stir.split('.') or stir.split('i') or stir.split('?')
        for j in new_stir:
            if j[0] == j[0].captitalize():
                count += 1
            ls = ls.append(count)

print(check_name)('Annyung Hasae Yo! LoL!')
