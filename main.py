# This is a Python script to convert Traditional Chinese to Simplified Chinese of srt file.
import opencc, sys, re
re_srt = re.compile('srt$')

if __name__ == '__main__':
    converter = opencc.OpenCC('t2s')
    filename = sys.argv[1]
    new_file = []
    is_srt = False
    if re_srt.search(filename):
        is_srt = True
    if is_srt:
        with open(filename, 'r') as f:
            content = f.readlines()
    else: # txt
        with open(filename, 'r') as f:
            content = f.read().split()
    i = 1
    for line in content:
        if (not is_srt) or i % 4 == 3:
            line = converter.convert(line)
            if not is_srt:
                line += '\n'
        new_file.append(line)
        i += 1
    with open(filename, 'w') as f:
        f.writelines(new_file)

