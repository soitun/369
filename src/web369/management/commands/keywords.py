# -*- encoding: utf-8 -*-

import re
import operator
from optparse import make_option

from django.core.management.base import BaseCommand

from web369.models import CommentItem

RE_WORDS = re.compile(r'\w+')


stopwords = ['ana', 'antai', 'apie', 'ar', 'arba', 'argi', 'aure', 'be', 'bei',
             'bemaž', 'bene', 'bent', 'bet', 'beveik', 'bus', 'buvo', 'būtent',
             'būti', 'd', 'dali', 'dar', 'destis', 'dėl', 'gal', 'gali', 'gi',
             'idant', 'iki', 'ir', 'itin', 'iš', 'jau', 'jei', 'jeigu', 'jo',
             'jog', 'jos', 'juk', 'juo', 'jų', 'kad', 'kada', 'kadangi', 'kai',
             'kaip', 'kažin', 'kitų', 'ko', 'kol', 'kone', 'kuo', 'kuone',
             'kuri', 'ligi', 'lyg', 'm', 'ne', 'nebe', 'nebent', 'negi',
             'negu', 'nei', 'nejau', 'nejaugi', 'nelyginant', 'nes', 'net',
             'nors', 'nr', 'nuo', 'nė', 'o', 'pagal', 'pat', 'per', 'po',
             'prie', 'rasi', 'savo', 'su', 'tai', 'taigi', 'taip', 'tarsi',
             'tartum', 'tarytum', 'tačiau', 'te', 'tegu', 'tegul', 'tiek',
             'tik', 'tiktai', 'todėl', 'turi', 'už', 'užtai', 'va', 'val',
             'veik', 'vien', 'vis', 'vos', 'vėl', 'ypač', 'yra', 'čia', 'į'
             'še', 'šio', 'šit', 'šitai', 'šiuo', 'štai', 'šį',

             'labai', 'reikia', 'tikrai', 'dabar', 'visi', 'daug', 'mano',
             'nieko', 'kiek', 'daugiau', 'kirie', 'galima', 'gerai', 'pats',
             'viskas', 'tada', 'butu', 'metu', 'manau', 'tokia', 'nera',
             'geriau', 'viena', 'vienas', 'toks', 'irgi', 'koks', 'kurie',
             'teis', 'darbo', 'juos', 'viso', 'kokia', 'niekas', 'pati',
             'tiesiog', 'jiems', 'atrodo', 'buti', 'visa', 'tokie', 'nori',
             'visai', 'patys', 'musu', 'kuris', 'tokiu', 'moni', 'toki',
             'kodel', 'pries', 'reik', 'nereikia', 'kart', 'neturi', 'lietuvi',
             'kalba', 'jums', 'save', 'metus', 'toliau', 'laiko', 'visiems',
             'visus', 'negali', 'tavo', 'visada', 'matyt', 'prad', 'tuos',
             'kuriuos', 'todel', 'kita', 'kurios', 'vaiko', 'straipsnis',
             'labiau', 'kiti', 'lietuvos', 'lietuvoje', 'lietuva', 'valstyb',
             'zmones', 'darbas', 'vaik', 'vald', 'lietuviai', 'zmoniu',
             'vaikai', 'vaikas', 'gyventi', '2011', 'pinigus', 'visos',
             'geras', 'tiesa', 'gaila', 'tokios',
             ]

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    option_list = BaseCommand.option_list + (
        make_option('--limit',
            action='store',
            dest='limit',
            default=50,
            help='Limit to'),
        )


    def handle(self, *args, **options):
        all_words = {}
        for content in CommentItem.objects.values_list('subject_title', flat=True):
            if content:
                words = RE_WORDS.findall(content)
                for word in words:
                    word = word.lower()
                    if not word in stopwords and len(word) > 3:
                        if word in all_words:
                            all_words[word] += 1
                        else:
                            all_words[word] = 1
        limit = int(options['limit'])
        if limit == 0:
            limit = -1
        for word, hits in sorted(all_words.iteritems(),
                                 key=operator.itemgetter(1),
                                 reverse=True):
            print hits, word
            limit -= 1
            if limit == 0:
                break