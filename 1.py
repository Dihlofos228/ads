'''# O(N ** 2)
def strcounter(s):
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(f'{sym} - {count}')'''

'''# O(N)
def strcounter(s):
    sym_dict = {}
    for sym in s:
        sym_dict[sym] = 1 + sym_dict.get(sym, 0)

    for sym, count in sym_dict.items():
        print(f'{sym} - {count}')'''

# O(N)
def strcounter(s):
    for sym in set(s):
        print(f'{sym} - {s.count(sym)}')


strcounter('zxc')