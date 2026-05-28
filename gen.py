


W = 5

for i in range(4):
    for digit in range(10):
        print(f'body:has(td[d{i}="{digit}"]:hover) {{--node-i-d{i}: {digit}}}')
