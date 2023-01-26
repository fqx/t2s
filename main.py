# This is a Python script to convert Traditional Chinese to Simplified Chinese of srt file.
import opencc, sys


if __name__ == '__main__':
    converter = opencc.OpenCC('t2s')
    filename = sys.argv[1]
    new_file = []
    with open(filename, 'r') as f:
        content = f.readlines()
    i = 1
    for line in content:
        if i % 4 == 3:
            line = converter.convert(line)
        new_file.append(line)
        i += 1
    with open(filename, 'w') as f:
        f.writelines(new_file)

