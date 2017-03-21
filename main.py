#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Name: Will Tribble
  Student ID: 10540462
  Email: wltribbl@go.olemiss.edu
  Course Information: CSCI 343 - Section 01
  Program Source File Name: main.py
  Programming Assignment: 02
  References: Getting rid of punctuation > http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
  Program Description: this program takes political convention speeches and analyzes their sentiment score.
  Due Date: Friday, 2/24/2017, 11:59 am

  In keeping with the honor code policies of the University of Mississippi, the School of
  Engineering, and the Department of Computer and Information Science, I affirm that I have
  neither given nor received assistance on this programming assignment. This assignment
  represents my individual, original effort.
  ... My Signature is on File.
"""

# import division, just in case
from __future__ import division
# importing the ability to plot data graphically
import matplotlib.pyplot as mplot


# user input to decide which file to examine, and make it all lowercase
print ("\nWhich speech would you like to examine?")
print ("d08 \td12 \td16 \tr08 \tr12 \tr16")
whichSpeech = input("\nEnter one of the above choices:\t")
whichSpeech = whichSpeech.lower()
whichSpeech += ".txt"

# open the file, read it, get rid of punctuation, split it on whitespace
speech = open(whichSpeech, "r")
speech = speech.read()
speech = speech.translate({ord(c): " " for c in "1234567890.,?!'-:;"}).translate({ord(c): " " for c in '"'})
speech = speech.lower()
speech = speech.split()


# opening the sentiment score sheet and splitting it for iteration
lexiconList = open("sent_lexicon.csv", "r")
lexiconList = lexiconList.read()
lexiconList = lexiconList.split("\n")
lexiconDict = {}

# iterate through the lexicon and split it after each comma
for index in range(0, len(lexiconList)):
    # ensure that no empty data lines will get in the way of what we are doing
    if len(lexiconList[index]) == 0:
        del(lexiconList[index])
        continue

    lexiconList[index] = lexiconList[index].split(",")

    # convert the lexicon words into strings and values into numbers
    lexiconList[index][0] = str(lexiconList[index][0])
    lexiconList[index][1] = float(lexiconList[index][1])

    # add the lexicon words/ratings into a dictionary for easier reference
    lexiconDict[lexiconList[index][0]] = lexiconList[index][1]

# create a dicitonary of the unique words in the speech
uniqueWords = {}

# adding the words and their counts to the dicitonary of unique words
for index in range(0, len(speech)):
    try:
        existenceTest = lexiconDict[speech[index]]
        try:
            uniqueWords[speech[index]] += 1
        except:
            uniqueWords[speech[index]] = 1
    except:
        continue

# initialize total word count
totalSum = 0

# go through the specificied speech, count the words, determine their score, and find a total score
for word, wordCount in uniqueWords.items():
    # word counting and score retrieval from the lexicon, ensuring that only words that have scores are counted
    try:
        rating = lexiconDict[word]
    except:
        continue

    # as the program goes through each unique word of the speech, it'll compare that word's score to a range variable, then add the number of times it appears to that range's count
    if (rating >= -1 and rating < -0.6):
        totalSum += wordCount
        try:
            negative += wordCount
        except:
            negative = wordCount
    elif (rating >= -0.6 and rating < -0.2):
        totalSum += wordCount
        try:
            weaklyNegative += wordCount
        except:
            weaklyNegative = wordCount
    elif (rating >= -0.2 and rating <= 0.2):
        totalSum += wordCount
        try:
            neutral += wordCount
        except:
            neutral = wordCount
    elif (rating > 0.2 and rating <= 0.6):
        totalSum += wordCount
        try:
            weaklyPositive += wordCount
        except:
            weaklyPositive = wordCount
    elif (rating > 0.6 and rating <= 1):
        totalSum += wordCount
        try:
            positive += wordCount
        except:
            positive = wordCount
    else:
        continue


# take the total scores from each range and find the percentage of the speech they comprise
negative /= totalSum
weaklyNegative /= totalSum
neutral /= totalSum
weaklyPositive /= totalSum
positive /= totalSum

negative *= 100
weaklyNegative *= 100
neutral *= 100
weaklyPositive *= 100
positive *= 100


# setting the plot axes into lists
xaxis = [1.1, 2.1, 3.1, 4.1, 5.1]
yaxis = [negative, weaklyNegative, neutral, weaklyPositive, positive]

# plotting the data
mplot.xlabel("Sentiment")
mplot.ylabel("Percent of Words")
mplot.xticks([(i + 1.5) for i in range(5)], ["Negative", "Weak Negative", "Neutral", "Weak Postiive", "Positive"])
mplot.title("Sentiment Distribution for " + str(whichSpeech))
mplot.bar(xaxis, yaxis)
mplot.show()
