#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Print a gorgeous millipede
"""

from __future__ import print_function

from argparse import ArgumentParser
import sys


def millipede(size, comment=None, reverse=False, template='default'):
    """
    Output the millipede
    """
    padding_offsets = [2, 1, 0, 1, 2, 3, 4, 4, 3]

    templates = {
            'frozen': {'body': '╔═(❄❄❄)═╗', 'bodyr': '╚═(❄❄❄)═╝'},
            'love': {'body': '╔═(♥♥♥)═╗', 'bodyr': '╚═(♥♥♥)═╝'},
            'corporate': {'body': '╔═(©©©)═╗', 'bodyr': '╚═(©©©)═╝'},
            'musician': {'body': '╔═(♫♩♬)═╗', 'bodyr': '╚═(♫♩♬)═╝'},
            'bocal': {'body': '╔═(🐟🐟🐟)═╗', 'bodyr': '╚═(🐟🐟🐟)═╝'},
            'default': {'body': '╔═(███)═╗', 'bodyr': '╚═(███)═╝'},
        }

    print(template)
    if template not in templates:
        template = templates.get('default')
    else:
        print(templates[template])
        template = templates.get(template)


    head = "    ╔⊙ ⊙╗\n" if reverse else "    ╚⊙ ⊙╝\n"
    body = "".join([
        "{}{}\n".format(
            " " * padding_offsets[(x + 3) % 9 if reverse else x % 9],
            template['body'] if reverse else template['bodyr']
        )
        for x in range(size)
    ])

    output = ""
    if reverse:
        output += body + head
        if comment:
            output += "\n" + comment + "\n"
    else:
        if comment:
            output += comment + "\n\n"
        output += head + body

    return output


def main():
    """
    Entry point
    """
    parser = ArgumentParser(description='Millipede generator')
    parser.add_argument('size', metavar='s',
                        type=int,
                        help='the size of the millipede')
    parser.add_argument('comment', metavar='c',
                        help='the comment', nargs="?")
    parser.add_argument('-r', '--reverse',
                        action='store_true',
                        help='reverse the millipede')
    parser.add_argument('-t', '--template',
                        help='customize your millipede')

    args = parser.parse_args()

    sys.stdout.write(
        millipede(args.size, comment=args.comment, reverse=args.reverse, template=args.template)
    )
