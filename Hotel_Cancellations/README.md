# Predicting Hotel Cancellations

## Introduction
This project is an exploratory data analysis on a data set of hotel reservation data. The goal is to determine if there are any indicators that can be used by the hotels to predict cancellations. The main variables of focus in this analysis are the number of adults on the reservation, the number of children, the number of weekend nights booked, the number of weekday nights, the average price per night for the stay, and of course, whether the reservation was cancelled or not.

## Methods
Included in the analysis is a probability mass function of the average price per night of the room for both cancelled and fulfilled reservations to visually interpret any price ranges where cancellations may be more or less common.
In addition, a cumulative distribution function of the length of stay in weekdays was created to observe any trends in how long reservations tend to be, both cancelled and fulfilled.
A normal probability plot was created to ensure that the data being sampled followed a relatively normal distribution of adults listed in the reservation.
Two correlation plots were created, one for the correlation between the number of weekdays spent at the hotel and the price, and another for the correlation between the number of weeknights spent at the hotel and the price.
A permutation test was run to determine if the difference in mean price of cancelled and fulfilled reservations was due to simple random sampling.
Finally, a least squares multiple regression was performed to determine how each of the variables correlated with the cancellation status.
