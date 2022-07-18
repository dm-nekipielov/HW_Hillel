class colorizer:
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'default': '\033[0m'
    }

    def __init__(self, color='default'):
        self.color = color

    def __enter__(self):
        if self.color not in self.COLORS:
            self.color = 'default'
        print(self.COLORS[self.color], end='')
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.COLORS['default'], end='')


with colorizer('cyan'):
    print('Some colorized text')
print('Default color text')
