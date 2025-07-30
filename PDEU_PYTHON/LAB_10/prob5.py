with open('source.txt', 'r') as src, open('dest.txt', 'w') as dest:
    for line in src:
        dest.write(line.upper())
