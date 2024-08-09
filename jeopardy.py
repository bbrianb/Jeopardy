import csv
import time
import tkinter as tk


class Object:
    def __init__(self, clue):
        self.clue = clue

    def clicked(self, event):
        global current_clue
        current_clue = self.clue


# noinspection PyUnusedLocal
def anywhere_click(event):
    global click_count
    global root
    global full_screen
    global current_clue
    global current_state

    click_count += 1
    if click_count == 1:
        full_screen = tk.Label(root, text='JEOPARDY!', font=('Haettenschweiler', 160), bg='blue', fg='white')
        full_screen.grid(column=0, row=0, columnspan=6, rowspan=6, sticky=tk.NSEW)
    elif click_count < 13:
        if click_count % 2 == 1:
            full_screen.config(text='JEOPARDY!', font=('Haettenschweiler', 160))
        else:
            full_screen.config(text=categories_r1[click_count // 2 - 1], font=('Arial Black', 100))
    elif click_count == 13:
        full_screen.grid_remove()
        current_state = 'waiting for clue'
        current_clue = ''
    else:
        if current_state == 'waiting for clue' and current_clue != '':
            current_state = 'reading clue'
            time.sleep(1)
            full_screen.config(text=current_clue)
            full_screen.grid()
        elif current_state == 'reading clue':
            current_state = 'waiting for response'


def print_line(arr, start=''):
    if not start:
        start = f'{arr[0]:>4} '
        arr = arr[1:]
    print(start, end='')
    for i in arr[:-1]:
        print(f'{i:<20}', end='')
    print(arr[-1])


def get_clues_and_responses(arr):
    print(arr[0][0])  # clues
    clues = arr[1:6]
    for line in clues:
        print_line(line)
    print(arr[6][0])  # responses
    responses = arr[7:]
    for line in responses:
        print_line(line)
    clues_out = []
    responses_out = []
    remove_dollar_column(clues, clues_out)
    remove_dollar_column(responses, responses_out)
    return clues_out, responses_out


def remove_dollar_column(clues, clues_out):
    for row in clues:
        clues_out.append(row[1:])


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
        print(i+1, c)

    print_line(categories_r1, ' ' * 5)
    clues_r1, responses_r1, = get_clues_and_responses(game[6:18])
    print(game[18][0])
    print_doubles(categories_r1, game[20])

    print(game[22][0])
    categories_r2 = game[24]
    print_line(categories_r2, ' ' * 5)
    clues_r2, responses_r2, = get_clues_and_responses(game[25:37])
    print(game[37][0])
    print_doubles(categories_r2, game[39])
    print_doubles(categories_r2, game[40])
    # if input('Start Game? (y/n) ') == 'n':
    #    quit()
    # team1 = input('Team 1 Name: ')
    # team2 = input('Team 1 Name: ')
    # team3 = input('Team 1 Name: ')
    team1 = 'Sea'
    team2 = 'Sand'
    team3 = 'Sun'

    root = tk.Tk()
    tile_height = 150
    tile_width = 300
    root.geometry(f'{tile_width*6}x{tile_height*6}')
    # root.attributes("-fullscreen", True)
    root.title('Jeopardy')

    borders = tk.Frame(root, bg='black')
    borders.grid(rowspan=6, columnspan=6, sticky=tk.NSEW)

    print(clues_r1)

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
            clue = clues_r1[row-1][column]
            obj = Object(clue)
            label = tk.Label(root, text=text, font=('Haettenschweiler', 40), bg='blue', fg=text_color)
            label.bind('<Button-1>', obj.clicked)
            label.grid(row=row, column=column, sticky=tk.EW, ipadx=59, ipady=43, padx=2, pady=2)

    root.bind('<Button-1>', anywhere_click)
    click_count = 0

    root.mainloop()


if __name__ == '__main__':
    global click_count
    global categories_r1
    global root
    global full_screen
    global current_clue
    global current_state
    main()
