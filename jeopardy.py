import csv
import tkinter as tk


def print_line(arr, start=''):
    if not start:
        start = f'{arr[0]:>4} '
        arr = arr[1:]
    print(start, end='')
    for i in arr[:-1]:
        print(f'{i:<20}', end='')
    print(arr[-1])


def print_clues_and_responses(arr):
    print(arr[0][0])
    for line in arr[1:6]:
        print_line(line)
    print(arr[6][0])
    for line in arr[7:]:
        print_line(line)


def print_doubles(categories, line):
    print(f'{categories[int(line[0])]}, ${line[1]}')


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
    categories_r1 = game[5]
    print_line(categories_r1, ' ' * 5)
    print_clues_and_responses(game[6:18])
    print(game[18][0])
    print_doubles(categories_r1, game[20])

    print(game[22][0])
    categories_r2 = game[24]
    print_line(categories_r2, ' ' * 5)
    print_clues_and_responses(game[25:37])
    print(game[37][0])
    print_doubles(categories_r2, game[39])
    print_doubles(categories_r2, game[40])
    # if input('Start Game? (y/n) ') == 'n':
    #    quit()

    root = tk.Tk()

    root.geometry('1800x900')
    # root.attributes("-fullscreen", True)
    root.title('Jeopardy')

    frame = tk.Frame(root)
    for i in range(6):
        frame.columnconfigure(i, weight=1)

    board = [[]]
    for i in range(6):
        board[0].append(tk.Label(frame, text="JEOPARDY!", font=('Haettenschweiler', 40)))
        board[0][-1].grid(row=0, column=i, sticky=tk.W + tk.E)

    for i in range(5):
        board.append([])
        for j in range(6):
            board[-1].append(tk.Label(frame, text=str(100 * i + 100), font=('Haettenschweiler', 40)))
            board[-1][-1].grid(row=i+1, column=j, sticky=tk.W + tk.E)

    frame.pack(fill='x')

    root.mainloop()


if __name__ == '__main__':
    main()
