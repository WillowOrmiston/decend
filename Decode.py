
from lark import Visitor, Lark, Tree, Token

DOWN = '-'
RIGHT = '/'
LEFT = '*'

VOWEL = '~'
CONS = '^'

CALL = '['
RET = ']'
# 012345
# 112345
# 212345 -- row # and column #
# set up table? yes ---   
# a list of list of string
# a string is text ex- th -- string of characters 0 or more
table = [
    ['', '', '', 'H', 'R', '', ''],
    ['P', 'B', 'M', '', '', '', ''],
    ['', '', '', 'F', 'V', '', ''],
    ['', '', '', 'th', 'TH', '', ''],
    ['T', 'D', 'N', 'S', 'Z', 'L', ''],
    ['', 'CH', '', 'SH', 'ZH', '', 'J'],
    ['K', 'G', 'NG', '', '', '', ''],
]
# vowel is set up -1 cause its offset from cons 
vowels = ['OO', 'o', 'Ou', 'AH', 'UH', 'A', 'e', 'I', 'E']

class Output:
    def __init__(self):
        self.res = ''
        # x,y 
        # 0 indexing,0 is the first item cause its based off of offset 
        self.pos = (3, 0)

    def add(self, tree):
        if isinstance(tree, Tree):
            match tree.data:
                
                case 'rec':
                    # retain position from last turn
                    last = self.pos
                    for i in tree.children:
                        self.add(i)
                    self.pos = last
                case 'word':
                    for i in tree.children:
                        self.add(i)
                case 'start':
                    for i in tree.children:
                        self.add(i)
                case _:
                    print(tree.data)
        else:
            match str(tree):
                # positive in y axis is down?
                case '-':
                    self.pos = (self.pos[0], self.pos[1] + 1)
                case '/':
                    self.pos = (self.pos[0] + 1, self.pos[1])
                case '.':
                    self.pos = (self.pos[0] - 1, self.pos[1])
                # ok so self.pos[0] is x axis self.pos[1] is y axis
                # ^ needs both x and y axis 
                case '^':
                    self.res += table[self.pos[1]][self.pos[0]]
                case '~':
                    self.res += vowels[self.pos[0] + 1]
                case '[' | ']':
                    pass

parser = Lark.open('grammar.lark')

def decode(msg):
    tree = parser.parse(msg)
    out = Output()
    out.add(tree)
    return out.res

def main():
    #  this is a while loop awawawa
    while True:
        cmd, *msgs = input("^-^--> ").split()
        match cmd:
            case 'enc' | 'encode':
                # TODO: implement the encoder
                raise NotImplementedError(f'command: encoding')
            case 'dec' | 'decode':
                for msg in msgs:
                    res = decode(msg)
                    print(res, end=' ')
                print()
            case 'help':
                print('please type a command (enc, dec, help)')
            case _:
                raise NotImplementedError(f'command: {cmd}')


if __name__ == '__main__':
    main()
