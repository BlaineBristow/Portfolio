# Modeling the Correlation Between Mental Health and Music Listening Habits

## Introduction
There have been numerous studies on the positive effects of music on a person’s mental wellbeing. The goal of this research is to use survey responses to determine if a person’s favorite genres, genre diversity, and listening habits can give any indication of a person’s mental health.

## Methods
6 models were created, 2 for each question being addressed. The goal was to determine how the respondent’s mental health was affected by music, but with 4 different target columns, a method had to be used to paint a more overall picture of their mental health. 2 solutions were attempted. First, the 4 categories were summed, then the sum was broken into one of 3 categories (Good, Fair, and Poor) to create a categorical target column. This way a logistic regression model could be trained to put people into one of the 3 buckets based on their responses. The other attempt was to take the highest score of the 4 categories and train a linear regression model to predict the score. The highest score was used as people can be dealing with different mental health issues, and the categorical summing may not be an accurate depiction of the actual mental wellbeing of each respondent.
