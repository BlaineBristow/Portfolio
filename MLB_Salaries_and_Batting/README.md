# Analyzing the Offensive Performance and Salaries of MLB Players

## Introduction
This project focuses on compiling information on MLB players from the 2021 season. This will include data from 3 sources: basic information (position, handedness, height, weight, etc.), batting statistics, and salary for the year. The data is pulled from 3 sources, a flat file, an api, and directly off a website.

## Methods
This project required cleaning and formatting of each of the 3 datasets described above. The flat file includes data for more years than we are interested in, so it needed to be trimmed down to just include data from 2021. In addition, there appears to be some inaccuracy surrounding some names. For example, JP Feyereisen appears in the flat file as just “Feyereisen”, and Ji Man Choi appears as just “Ji”. The data from the API includes far more information than necessary, especially since much of it is duplicated information, just in a different format. The data from the website needed to be cleaned to remove any team-specific data for players that played for more than one team. Once all this data is cleaned and combined, some insights that could be gained from the data set include if highly paid players bat better than lower paid players on average, or if players that grew up in certain areas play better on average.
