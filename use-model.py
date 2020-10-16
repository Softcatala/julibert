#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="models/roberta/output/",
    tokenizer="models/roberta/"
)

# The sun <mask>.
# =>

sentences = [ \
    "El meu cotxe és molt millor del que molts <mask>.",
    "El tribunal considera provat que els acusats van <mask> gairebé 24 milions d'euros.",
    "Els principals responsables de l'empresa que <mask> la depuradora.",
    "El meu pare és el més <mask> del grup",
    "El cotxe està <mask>.",
    "Tinc tanta son que a les cinc tinc <mask>.",
]

for sentence in sentences:
    results = fill_mask(sentence)
    print(results)
