import sys
import argparse

def comment_duplicate_lines(input_lines, spaces=False, comment=False):
    seen = set()
    result_lines = []
    print(input_lines)
    for line in input_lines:
        if not spaces:
            line = line.strip()
        if line == '\n' and comment:
            result_lines.append('#\n')
        elif line not in seen:
            result_lines.append(line)
            seen.add(line)
    return result_lines

def main():

    parser = argparse.ArgumentParser(description="Remove repetitive lines from input.")
    parser.add_argument('input_file', nargs='?', help="Input file (default: stdin)")
    parser.add_argument('-s', '--spaces', action='store_true', help="Consider spaces in line comparison")
    parser.add_argument('-p', '--comment', action='store_true', help="Comment empty lines with #")
    args = parser.parse_args()

    if args.input_file:
        with open(args.input_file, 'r') as file:
            input_lines = file.readlines()
        result_lines = comment_duplicate_lines(input_lines, args.spaces, args.comment)
        output_file = args.input_file.replace('.txt', '_filtered.txt')
        with open(output_file, 'w') as file:
            file.writelines(result_lines)
        print(''.join(result_lines))
    else:
        input_lines = sys.stdin.readlines()
        result_lines = comment_duplicate_lines(input_lines, args.spaces, args.comment)
        print(''.join(result_lines))

if __name__ == "__main__":
    main()