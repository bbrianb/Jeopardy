import csv


def print_line(arr, start=''):
    if not start:
        start = f'{arr[0]:>4} '
        arr = arr[1:]
    print(start, end='')
    for i in arr[:-1]:
        print(f'{i:<20}', end='')
    print(arr[-1])


def print_clues_and_responses(arr):
    for line in arr[:5]:
        print_line(line)
    for line in arr[6:]:
        print_line(line)


def main():
    path = 'test.csv'
    with open(path) as file:
        csv_file = csv.reader(file)
        game = []
        for lines in csv_file:
            game.append(lines)

        print(path)
        print(game[1][0])
        print(game[3][0])
        round_1_categories = game[5]
        print_line(round_1_categories, ' '*5)
        print_clues_and_responses(game[7:18])
        print(f'{game[18][0]}: {round_1_categories[int(game[20][0])]}, ${game[20][1]}')

        print(game[22][0])
        round_2_categories = game[23]
        print_line(round_2_categories, ' '*5)


if __name__ == '__main__':
    main()
