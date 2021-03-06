# Introduction

Welcome to project Julibert, Softcatalà playground of BERT models 

BERT models were introduced by Google in 2018 and achieved state-of-the-art performance on a number of natural language understanding tasks:

* GLUE (General Language Understanding Evaluation) task set (consisting of 9 tasks)
* SQuAD (Stanford Question Answering Dataset) v1.1 and v2.0.
* SWAG (Situations With Adversarial Generations)

Google [has published](https://github.com/google-research/bert) two sets of models:

* Single language models for English and Chineses
* [Multilingual models](https://github.com/google-research/bert/blob/master/multilingual.md) where a single model covers 104 languages

It has been prove the multilingual models perform poorly comparared to single language models. Serveral linguistics communities like [French](https://camembert-model.fr/), [Finish](https://arxiv.org/abs/1912.07076) or [Spanish](https://skimai.com/roberta-language-model-for-spanish/) have been working on creating the language specific models that outperform Google multilingual models.

# Challenges for minority languages

BERT represents serveral problems for minority languages:

* It's expensive to train: <em>Training of BERT-base was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total), and training of BERT-large was performed on 16 Cloud TPUs (64 TPU chips total). Each pretraining took 4 days to complete</em>. 
* It's expensive to do predictions

Since BERT was publised several derviated versions have been published to solve these problems: Roberta, MiniBert, etc.

# Goals of the project

This project has two goals

## Create a Catalan BERT alike model for Catalan language 

Publish a Catalan model at https://huggingface.co/models and make available to the NLP community.

## Evaluate its use as part of our grammar correction system

We have the hypotesis that we can leverage on BERT alike models to improve LanguageTool grammar correction capatibities. Basically using BERT to understand if a word in a sentence is possibe in a BERT model.

# Models

## Roberta model

We train the model using the [SpanBerta instrucctions](https://skimai.com/roberta-language-model-for-spanish/)

The scripts in Python are in the repository

* Corpus: Oscar Catalan Corpus (3,8G)
* Tokenizer: ByteLevelBPETokenizer
* Model type: Roberta
* Vocabulary size: 50265
* Steps: 500000

https://www.softcatala.org/pub/softcatala/julibert/julibert-2020-10-11.zip

## Calbert model

A Catalan ALBERT (A Lite BERT). See: https://github.com/codegram/calbert

* Corpus: Oscar Catalan Corpus (3,8G)
* Tokenizer: SentencePiece
* Model type: Alebert
* Vocabulary size: 30000

# Usage

From Linux command line:

```
wget https://www.softcatala.org/pub/softcatala/julibert/julibert-2020-11-10.zip
unzip julibert-2020-11-10.zip 


pip install transformers torch

```

From Python 3:

```
from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="julibert/",
    tokenizer="julibert/"
)

predict = fill_mask("El tribunal considera provat que els acusats van <mask> gairebé 24 milions d'euros.")
print(predict)

```

Result:

```
[
{'sequence': "<s>El tribunal considera provat que els acusats van costar gairebé 24 milions d'euros.</s>", 'score': 0.33576342463493347, 'token': 14808 },
{'sequence': "<s>El tribunal considera provat que els acusats van invertir gairebé 24 milions d'euros.</s>", 'score': 0.06258589774370193, 'token': 14388 },
{'sequence': "<s>El tribunal considera provat que els acusats van pagar gairebé 24 milions d'euros.</s>", 'score': 0.05679689720273018, 'token': 4030}, 
{'sequence': "<s>El tribunal considera provat que els acusats van guanyar gairebé 24 milions d'euros.</s>", 'score': 0.03947337344288826, 'token': 3246}, 
{'sequence': "<s>El tribunal considera provat que els acusats van recaptar gairebé 24 milions d'euros.</s>", 'score': 0.035779498517513275, 'token': 14638}


```

# Contact

Email address: Jordi Mas: jmas@softcatala.org


