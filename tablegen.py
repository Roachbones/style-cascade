


W = 5

for x in range(W):
    print('<tr>',end='')
    for y in range(W):
        i = x * W + y
        s = '0'*9+str(i)
        print(f'<td class=n d1={s[-1]} d2={s[-2]} d3={s[-3]} d4={s[-4]}></td>',end='')
    print('</tr>',end='')
