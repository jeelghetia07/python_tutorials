with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
    for line in inp:
        words = line.split()
        filtered = ['' if word.lower() in ['a', 'an', 'the'] else word for word in words]
        out.write(' '.join(filtered) + '\n')
