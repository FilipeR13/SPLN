import sys

def comment_duplicate_lines(input_lines):
    seen = set()
    result_lines = []
    for line in input_lines:
        if line in seen:
            result_lines.append(f"//{line}")
        else:
            result_lines.append(line)
            seen.add(line)
    return result_lines

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            input_lines = file.readlines()
        result_lines = comment_duplicate_lines(input_lines)
        output_file = input_file.replace('.txt', '_filtered.txt')
        with open(output_file, 'w') as file:
            file.writelines(result_lines)
        print(''.join(result_lines))
    else:
        input_lines = sys.stdin.readlines()
        result_lines = comment_duplicate_lines(input_lines)
        print(''.join(result_lines))

if __name__ == "__main__":
    main()