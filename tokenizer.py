#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tokenizers import ByteLevelBPETokenizer

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training

vocab_size=50265
path='data/src-train.txt'
# Customize training
tokenizer.train(files=path,
                vocab_size=50265,
                min_frequency=2,
                special_tokens=["<s>", "<pad>", "</s>", "<unk>", "<mask>"])

# Save files to disk
directory = "models/roberta"

if not os.path.exists(directory):
    os.makedirs(directory)

tokenizer.save(directory)
