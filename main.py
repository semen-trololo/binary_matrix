#pip install bext
#pip install colorama
import sys
import random
import time

# Подключаем дополнительные модули
try:
    import bext, colorama
except ImportError:
    print('Для запуска программы нужны модули bext и colorama.')
    sys.exit()
    
    
def rendom_sred():
    return ((random.randint(0, width) + random.randint (0, width) + random.randint (0, width))//3)


class Drop:
    def __init__ (self):
        self.x = rendom_sred() # Начальное положение по горизонтали
        self.y = -1 # Начальное положение по вертикали - за верхней границей экрана
        self.drop_type = random.randint (0, 1) # Тип: антикапля или капля
        self.timeout = random.randint (1, 4) # Задержка до следующего перемещения
        self.wait_count = random.randint (1, 4) # Счетчик паузы
               
    def renew (self):
        if self.drop_type == 1:
            self.__init__()
            self.drop_type = 0
        else:
            self.__init__()
            self.drop_type = 1
            
    def move(self):
        if drop.wait_count < drop.timeout: # Пока рано перемещать
            drop.wait_count += 1 # Увеличиваем счётчик паузы
            return False
        else: # Уже можно перемещать
            drop.wait_count = 0 # Сбрасываем счётчик паузы
            drop.y += 1 # Перемещаем каплю или антикаплю на шаг вниз
            return True
        
    def draw(self):
        if self.drop_type == 1:
            symbol = gen_tmp.__next__()
            if symbol > 31:
                con_print(self.x, self.y, green, chr(symbol))
            else:
                con_print(self.x, self.y, green, chr((31 - symbol) + symbol))
            self.zero_draw() # Рисуем яркий ноль
        else:
            con_print (self.x, self.y, green, ' ')
            
    def zero_draw(self):
        if (self.y < height):
            con_print (self.x, self.y+1, yellow, '0')


def is_rb_corner (x, y):
    if x == width and y == height:
        return True
    else:
        return False


def con_print (x, y, color, symbol):
    if not is_rb_corner (x, y):
        bext.goto (x, y)
        sys.stdout.write (color)
        print(symbol, end='')

bext.title('Matrix') # Меняем заголовок консольного окна
bext.clear() # Очищаем консольное окно
bext.hide() # Скрываем курсор в консольном окне
width, height = bext.size() # Получаем размер консольного окна
width -= 1
height -= 1

green = colorama.Fore.GREEN
lgreen = colorama.Fore.LIGHTGREEN_EX
yellow = colorama.Fore.YELLOW
# Создаём массив капель и антикапель
drops = []
for i in range(1, width*2//3):
    drop = Drop()
    drops.append(drop)

def read_file_gen():
    with open("matrix22.exe", "rb") as f:
        bytes_read = f.read()
    for b in bytes_read:
        yield b
    f.close()
gen_tmp = read_file_gen()
while True:
    for drop in drops:
        if drop.move(): # Проверяем перемещение элемента
            drop.draw() # Отображаем элемент
            if drop.y >= height: # Достигли дна
                drop.renew() # Обновляем элемент
    key = bext.getKey (blocking=False) # Проверяем, нажата ли клавиша
    if key == 'esc': # Если нажата ESC, то выходим из программы
        bext.clear()
        sys.exit()
    time.sleep(0.02) # Задержка
