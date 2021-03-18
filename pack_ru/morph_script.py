# -*- coding: utf8 -*-
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
print(morph.parse('курицы'))
