# Introduction

Welcome to project Julivert, Softcatalà playground of BERT models 

BERT models were introduced by Google in 2018 and achieved state-of-the-art performance on a number of natural language understanding tasks:

* GLUE (General Language Understanding Evaluation) task set (consisting of 9 tasks)
* SQuAD (Stanford Question Answering Dataset) v1.1 and v2.0.
* SWAG (Situations With Adversarial Generations)

Google [has published](https://github.com/google-research/bert) two sets of models:

* Single language models for English and Chineses
* [Multilingual models](https://github.com/google-research/bert/blob/master/multilingual.md) where a single model covers 104 languages

It has been prove the multilingual models perform poorly comparared to single language models. Serveral linguistics communities like French, Finish or Spainish have been working on creating the language specific models that outperform Google multilingual models.

# Challenges for minority languages

BERT represents serveral problems for minority languages:

* It's expensive to train: <em>Training of BERT-base was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total), and training of BERT-large was performed on 16 Cloud TPUs (64 TPU chips total). Each pretraining took 4 days to complete</em>. 
* It's expensive to do predictions

Since BERT was publised several derviated versions have been published to solve these problems: Roberta, MiniBert, etc.

# Goals of the project

This project has two goals

## Create a Catalan BERT alike model for Catalan language 

Publish a Catalan model at https://huggingface.co/models and make available to the NLP community.

## Evalute its use as part of our grammar correction system

We have the hypotesis that we can leverage on BERT alike models to improve LanguageTool grammar correction capatibities. Basically using BERT to understand if a word in a sentence is possibe in a BERT model.
