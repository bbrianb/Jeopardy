import csv
import tkinter as tk


# noinspection PyUnusedLocal
def left_click(event):
    global click_count
    global root
    global category

    click_count += 1
    print(f'left click {click_count}')
    if click_count == 1:
        category = tk.Label(root, text='JEOPARDY!', font=('Haettenschweiler', 160), bg='blue', fg='white')
        category.grid(column=0, row=0, columnspan=6, rowspan=6, sticky=tk.NSEW)
    elif click_count < 13:
        if click_count % 2 == 1:
            category.config(text='JEOPARDY!', font=('Haettenschweiler', 160))
        else:
            category.config(text=categories_r1[click_count//2-1], font=('Arial Black', 100))
    else:
        print('it should keep working')
        category.grid_remove()


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
    global categories_r1
    global root
    global click_count

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
    root = tk.Tk()
    tile_height = 150
    tile_width = 300
    root.geometry(f'{tile_width*6}x{tile_height*6}')
    # root.attributes("-fullscreen", True)
    root.title('Jeopardy')

    borders = tk.Frame(root, bg='black')
    borders.grid(rowspan=6, columnspan=6, sticky=tk.NSEW)

    board = []
    for row in range(6):
        board.append([])
        if row == 0:
            text = 'JEOPARDY!'
            text_color = 'white'
        else:
            text = f'${200*row}'
            text_color = 'yellow'
        for column in range(6):
            label = tk.Label(root, text=text, font=('Haettenschweiler', 40), bg='blue', fg=text_color)
            label.grid(row=row, column=column, sticky=tk.EW, ipadx=59, ipady=43, padx=2, pady=2)
            board[-1].append(label)

    root.bind('<Button-1>', left_click)
    click_count = 0

    root.mainloop()


if __name__ == '__main__':
    global click_count
    global categories_r1
    global root
    global category
    main()
