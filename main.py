from random import randint


def attack(char_name: str, char_class: str) -> str:
    dmg: int = 5
    if char_class == 'warrior':
        dmg += randint(3, 5)
    elif char_class == 'mage':
        dmg += randint(5, 10)
    elif char_class == 'healer':
        dmg += randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {dmg}')


def defence(char_name: str, char_class: str) -> str:
    block: int = 10
    if char_class == 'warrior':
        block += randint(5, 10)
    elif char_class == 'mage':
        block += randint(-2, 2)
    elif char_class == 'healer':
        block += randint(2, 5)
    return (f'{char_name} блокировал {block} урона')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        sta: int = 80 + 25
        return (f'{char_name} применил '
                f'специальное умение «Выносливость {sta}»')
    if char_class == 'mage':
        atk: int = 5 + 40
        return (f'{char_name} применил специальное умение «Атака {atk}»')
    if char_class == 'healer':
        prot: int = 10 + 30
        return (f'{char_name} применил специальное умение «Защита {prot}»')
    return (f'{char_name} не применил умение')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя. '
                'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа ').lower()
    return char_class


def main() -> None:
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()
