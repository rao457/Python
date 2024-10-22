from collections import deque
def search(lines, pattern, history = 1):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
if __name__ == "__main__":
    with open('Python_Notes.txt', 'r', encoding='utf-8') as f:
        for line, prevlines in search(f, 'must', 1):
            print(line, end='', sep='   ')

            for pline in prevlines:
                print(pline, end='')
            print('.'*20)
