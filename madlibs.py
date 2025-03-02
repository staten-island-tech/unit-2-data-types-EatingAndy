print('name a celebrity, 2 verbs, a noun, and a number, respectively')

a = input()
b = input()
c = input()
d = input()
e = int(input())

def madlib():
    print(f'''Hello {a}, why were you {b} to those kids over there?
    I saw you {c} to those kids too. You were also bringing them to your {d}.
    There were like {e} of them.''')
madlib()

