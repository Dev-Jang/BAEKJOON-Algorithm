#4673
def generate():
    generated_num = set()

    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        generated_num.add(i)

    return generated_num

natural_num = set(range(1, 10001))
self_num = natural_num - generate()

for i in sorted(self_num):
    print(i)