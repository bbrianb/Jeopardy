import csv
import time
import tkinter as tk


class KeyPress:
    def __init__(self, key):
        self.key = key
        self.penalty = False

    # noinspection PyUnusedLocal
    def pressed(self, event):
        global key_pressed

        if current_state == 'waiting for response' and not self.penalty and key_pressed == '':
            key_pressed += self.key
            click_or_key(None)
        else:
            self.penalty = True
            time.sleep(0.2)
            self.penalty = False


class Object:
    def __init__(self, clue):
        self.clue = clue

    # noinspection PyUnusedLocal
    def clicked(self, event):
        global current_clue
        current_clue = self.clue


# noinspection PyUnusedLocal
def click_or_key(event):
    global event_count
    global full_screen
    global current_clue
    global current_state
    global key_pressed

    event_count += 1
    if event_count == 1:
        full_screen = tk.Label(root, text='JEOPARDY!', font=('Haettenschweiler', 160), bg='blue', fg='white')
        full_screen.grid(column=0, row=0, columnspan=6, rowspan=6, sticky=tk.NSEW)
    elif event_count < 13:
        if event_count % 2 == 1:
            full_screen.config(text='JEOPARDY!', font=('Haettenschweiler', 160))
        else:
            full_screen.config(text=categories_r1[event_count // 2 - 1], font=('Arial Black', 100))
    elif event_count == 13:
        for i, label in enumerate(category_labels):
            label.config(text=categories_r1[i].upper(), font=('Haettenschweiler', 20))
        full_screen.grid_remove()
        current_clue = ''
        current_state = 'waiting for clue'
    else:
        if current_state == 'waiting for clue' and current_clue != '':
            buzz.grid_remove()
            time.sleep(1)
            full_screen.config(text=current_clue)
            full_screen.grid()
            current_state = 'reading clue'
        elif current_state == 'reading clue':
            buzz.grid(column=2, row=5, columnspan=2, sticky=tk.NSEW)
            buzz.tkraise()
            key_pressed = ''
            current_state = 'waiting for response'
        elif current_state == 'waiting for response':
            print(key_pressed)
            current_state = 'evaluating response'
    print(f'{event_count=}, {current_state=}')


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
    global event_count
    global current_state
    global category_labels

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
    for team_name, c in enumerate(categories_r1):
        print(team_name + 1, c)

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
    teams = ['Sea', 'Sand', 'Sun']
    team_money = [0, 0, 0]
    team_labels = []

    root = tk.Tk()
    tile_height = 150
    tile_width = 280
    root.geometry(f'{int(tile_width * 6.75)}x{tile_height * 6}')
    # root.attributes("-fullscreen", True)
    root.title('Jeopardy')

    borders = tk.Frame(root, bg='black')
    borders.grid(rowspan=6, columnspan=7, sticky=tk.NSEW)

    print(clues_r1)

    category_labels = []
    pad = 51
    for row in range(6):
        if row == 0:
            text = 'JEOPARDY!'
            text_color = 'white'
        else:
            text = f'${200 * row}'
            text_color = 'yellow'
        for column in range(6):
            clue = clues_r1[row - 1][column]
            obj = Object(clue)
            label = tk.Label(root, text=text, font=('Haettenschweiler', 40), bg='blue', fg=text_color)
            if row != 0:
                label.bind('<Button-1>', obj.clicked)
            label.grid(row=row, column=column, sticky=tk.EW, ipadx=pad, ipady=43, padx=2, pady=2)
            if row == 0:
                category_labels.append(label)
        if row % 2 == 0:
            team_labels.append(tk.Label(root, text=teams[int(row/2)], font=('Haettenschweiler', 40), bg='blue',
                                        fg='white'))
            team_labels[-1].grid(row=row, column=6, sticky=tk.NSEW, ipadx=pad, padx=2, pady=2)
        else:
            team_labels.append(tk.Label(root, text=f'${team_money[int((row-1)/2)]}', font=('Haettenschweiler', 30),
                                        bg='blue', fg='white'))
            team_labels[-1].grid(row=row, column=6, sticky=tk.NSEW, ipadx=pad, padx=2, pady=2)

    global buzz
    buzz = tk.Label(root, text='Buzz in!', font=('Haettenschweiler', 40), bg='white', fg='black')

    root.bind('<Button-1>', click_or_key)
    q, v, p = KeyPress('q'), KeyPress('v'), KeyPress('p')
    root.bind('q', q.pressed)
    root.bind('v', v.pressed)
    root.bind('p', p.pressed)

    event_count = 0

    current_state = 'introduction'

    root.mainloop()


if __name__ == '__main__':
    global event_count
    global categories_r1
    global root
    global full_screen
    global current_clue
    global current_state
    global buzz
    global key_pressed
    global category_labels
    main()
