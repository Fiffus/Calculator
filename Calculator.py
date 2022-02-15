import pygame


pygame.init()
pygame.font.init()
label_font = pygame.font.SysFont('', 50, bold=True)
font = pygame.font.SysFont('', 40, bold=True)
small_font = pygame.font.SysFont('', 30, bold=True)
is_running = True
WIDTH = 450
HEIGHT = 650
BLACK = 35, 35, 35
BLUE = 90, 90, 210
YELLOW = 210, 210, 90
DARKER_BLUE = 60, 60, 133
LIGHT_GRAY = 150, 150, 150
FPS = 20
user_input = ''
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)


class Button:
    def __init__(self, positions, color, text, size):
        self.positions = positions
        self.color = color
        self.text = text
        self.size = size
        self.rect = pygame.rect.Rect(self.positions, self.size)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def highlight(self, mouse):
        if self.rect.collidepoint(mouse):
            self.set_color(DARKER_BLUE)
        else:
            self.set_color(BLUE)

    def set_text(self, mouse, positions):
        if self.rect.collidepoint(mouse):
            if len(split_string(self.text)) == 1:
                show = font.render(self.text, True, LIGHT_GRAY, None)
                screen.blit(show, (self.positions[0] + positions[0], self.positions[1] + positions[1]))
            if len(split_string(self.text)) > 1:
                show = small_font.render(self.text, True, LIGHT_GRAY, None)
                screen.blit(show, (self.positions[0] + positions[0], self.positions[1] + positions[1]))
        else:
            if len(split_string(self.text)) == 1:
                show = font.render(self.text, True, BLACK, None)
                screen.blit(show, (self.positions[0] + positions[0], self.positions[1] + positions[1]))
            if len(split_string(self.text)) > 1:
                show = small_font.render(self.text, True, BLACK, None)
                screen.blit(show, (self.positions[0] + positions[0], self.positions[1] + positions[1]))

    def get_pressed(self, mouse, click):
        if self.rect.collidepoint(mouse):
            if click:
                return True
            else:
                return False

    def close(self, mouse, click):
        global is_running
        if self.get_pressed(mouse, click):
            is_running = False

    def calculate(self, mouse, click):
        global user_input
        if self.get_pressed(mouse, click):
            try:
                user_input = str(eval(user_input))
            except Exception as error:
                print(error)

    def add_item(self, mouse, click):
        global user_input
        if self.get_pressed(mouse, click):
            user_input += self.text

    def clear(self, mouse, click):
        global user_input
        if self.get_pressed(mouse, click):
            user_input = ''

    def render(self):
        self.rect.x = self.positions[0]
        self.rect.y = self.positions[1]
        self.rect = pygame.draw.rect(screen, self.color, self.rect)


def split_string(string):
    return [char for char in string]


def edges():
    pygame.draw.line(screen, YELLOW, (0, 0), (0, HEIGHT), 4)
    pygame.draw.line(screen, YELLOW, (0, 0), (WIDTH, 0), 4)
    pygame.draw.line(screen, YELLOW, (WIDTH - 2, HEIGHT), (WIDTH - 2, 0), 4)
    pygame.draw.line(screen, YELLOW, (WIDTH, HEIGHT - 2), (0, HEIGHT - 2), 4)


def main():
    global is_running
    global user_input
    global FPS
    n_1 = Button([26, 220], BLUE, '1', [80, 60])
    n_2 = Button([132, 220], BLUE, '2', [80, 60])
    n_3 = Button([238, 220], BLUE, '3', [80, 60])
    n_4 = Button([26, 306], BLUE, '4', [80, 60])
    n_5 = Button([132, 306], BLUE, '5', [80, 60])
    n_6 = Button([238, 306], BLUE, '6', [80, 60])
    n_7 = Button([26, 392], BLUE, '7', [80, 60])
    n_8 = Button([132, 392], BLUE, '8', [80, 60])
    n_9 = Button([238, 392], BLUE, '9', [80, 60])
    n_0 = Button([132, 478], BLUE, '0', [80, 60])
    equals = Button([344, 564], BLUE, '=', [80, 60])
    clear = Button([132, 564], BLUE, 'Clear', [80, 60])
    plus = Button([344, 220], BLUE, '+', [80, 60])
    minus = Button([344, 306], BLUE, '-', [80, 60])
    division = Button([344, 392], BLUE, '/', [80, 60])
    multiplication = Button([344, 478], BLUE, '*', [80, 60])
    close = Button([26, 564], BLUE, 'Close', [80, 60])
    clock = pygame.time.Clock()
    while is_running:
        clock.tick(FPS)
        keyboard = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                close.close(mouse, click)
                n_1.add_item(mouse, click)
                n_2.add_item(mouse, click)
                n_3.add_item(mouse, click)
                n_4.add_item(mouse, click)
                n_5.add_item(mouse, click)
                n_6.add_item(mouse, click)
                n_7.add_item(mouse, click)
                n_8.add_item(mouse, click)
                n_9.add_item(mouse, click)
                n_0.add_item(mouse, click)
                plus.add_item(mouse, click)
                minus.add_item(mouse, click)
                division.add_item(mouse, click)
                multiplication.add_item(mouse, click)
                equals.calculate(mouse, click)
                clear.clear(mouse, click)
        if keyboard[pygame.K_ESCAPE]:
            is_running = False

        screen.fill(BLACK)

        edges()
        pygame.draw.line(screen, YELLOW, (0, 196), (WIDTH, 196), 4)

        label = label_font.render(user_input, True, YELLOW, None)
        center = label.get_rect(center=(WIDTH//2, 105))
        screen.blit(label, center)

        n_1.render()
        n_1.highlight(mouse)
        n_1.set_text(mouse, [32, 21])
        n_2.render()
        n_2.highlight(mouse)
        n_2.set_text(mouse, [32, 21])
        n_3.render()
        n_3.highlight(mouse)
        n_3.set_text(mouse, [32, 21])
        n_4.render()
        n_4.highlight(mouse)
        n_4.set_text(mouse, [32, 21])
        n_5.render()
        n_5.highlight(mouse)
        n_5.set_text(mouse, [32, 21])
        n_6.render()
        n_6.highlight(mouse)
        n_6.set_text(mouse, [32, 21])
        n_7.render()
        n_7.highlight(mouse)
        n_7.set_text(mouse, [32, 21])
        n_8.render()
        n_8.highlight(mouse)
        n_8.set_text(mouse, [32, 21])
        n_9.render()
        n_9.highlight(mouse)
        n_9.set_text(mouse, [32, 21])
        n_0.render()
        n_0.highlight(mouse)
        n_0.set_text(mouse, [32, 21])
        equals.render()
        equals.highlight(mouse)
        equals.set_text(mouse, [30, 16])
        clear.render()
        clear.highlight(mouse)
        clear.set_text(mouse, [8, 21])
        plus.render()
        plus.highlight(mouse)
        plus.set_text(mouse, [30, 16])
        minus.render()
        minus.highlight(mouse)
        minus.set_text(mouse, [33, 18])
        division.render()
        division.highlight(mouse)
        division.set_text(mouse, [35, 18])
        multiplication.render()
        multiplication.highlight(mouse)
        multiplication.set_text(mouse, [32, 24])
        close.render()
        close.highlight(mouse)
        close.set_text(mouse, [8, 21])

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
