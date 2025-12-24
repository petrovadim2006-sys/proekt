#!/usr/bin/env python
"""
pycowsay -- display a message using a talking cow
"""

import sys
import textwrap

def cowsay(message: str, cow: str = 'default') -> str:
    # message - строка, cow - строка, возвращает строку
    """Return a cow saying message."""
    bubble = make_bubble(message)
    cow = draw_cow(cow)
    return bubble + cow

def make_bubble(message):
    """Put message in a speech bubble."""
    message = message.strip()
    lines = textwrap.wrap(message, 40)
    
    if len(lines) == 1:
        line = lines[0]
        bubble = ['< {} >'.format(line)]
    else:
        bubble = ['/ ' + lines[0] + ' \\']
        for line in lines[1:-1]:
            bubble.append('| ' + line + ' |')
        bubble.append('\\ ' + lines[-1] + ' /')
    
    width = max(len(l) for l in bubble)
    bubble = [' ' + l.ljust(width) + ' ' for l in bubble]
    bubble.insert(0, ' ' + '_' * width)
    bubble.append(' ' + '-' * width)
    
    return '\n'.join(bubble) + '\n'

def draw_cow(cow='default'):
    """Return a cow drawing."""
    # Словарь COWS хранит всех доступных коров
    # Вынесен в отдельную переменную для удобства добавления новых животных
    cows = {
        'default': r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||''',
        'tux': r'''
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/''',
        'stegosaurus': r'''
         \
          \
           \
            \
             .
            .'`'.
      .--.  |   |
    .'    \  \ /  /|
    |\     \  Y  / '
     \  .-./  ` /  /
      `'`'`\   /  /
            \.'`.'
              | |
              | |
              | |
              |_|'''
    }
    
    if cow not in cows:
        raise ValueError('Unknown cow: {}'.format(cow))
    
    return cows[cow]

def list_cows():
    """Return list of available cows."""
    return ['default', 'tux', 'stegosaurus']

def main():
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    else:
        message = sys.stdin.read()
    
    try:
        print(cowsay(message))
    except ValueError as e:
        print('Error:', e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()