import csv
import tkinter as tk


# noinspection PyUnusedLocal
def left_click(event):
    global click_count
    click_count += 1
    print(f'left click {click_count}')
    if click_count == 1:
        global frame
        frame.pack_forget()
        global root
        category = tk.Label(root, text=categories_r1[0], font=('Arial Black', 80))
        category.pack()


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
    global categories_r1
    categories_r1 = game[5]
    for i, c in enumerate(categories_r1):
        print(categories_r1[i])
        print(c)
        categories_r1[i] = c.upper()
    print(categories_r1)

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

    global root
    root = tk.Tk()
    root.geometry('1800x900')
    # root.attributes("-fullscreen", True)
    root.title('Jeopardy')

    global frame
    frame = tk.Frame(root)

    for i in range(6):
        frame.columnconfigure(i, weight=1)

    board = [[]]
    for i in range(6):
        board[0].append(tk.Label(frame, text="JEOPARDY!", font=('Haettenschweiler', 40)))
        board[0][-1].grid(row=0, column=i)

    for i in range(5):
        board.append([])
        for j in range(6):
            board[-1].append(tk.Label(frame, text=f'${100 * i + 100}', font=('Haettenschweiler', 40)))
            board[-1][-1].grid(row=i + 1, column=j)

    frame.pack(fill='x')

    root.bind('<Button-1>', left_click)

    global click_count
    click_count = 0

    root.mainloop()


if __name__ == '__main__':
    global click_count
    global frame
    global categories_r1
    global root
    main()
