# World Events Effect on Gold, Oil and the S&P 500 Index


## Proposal
The aim of this project is to undertake a quantitative analysis of Gold, Oil and the S&P 500 Index trends from previous years and determine how they are affected by world events.

Specifically, we will be looking at the following:
* 911
* GCF
* COVID-19
* Ukraine Russia War

Using the knowledge obtained in Monash Fintech Bootcamp the group, Andrew, Alex, Vinay, Abdul and Jack, will read, clean, and analyse Gold, Oil and the S&P 500 Index data during these periods.

### Questions
* What are the trends of Gold, Oil and the S&P 500 Index in relation to man-made disasters? (GFC, 911)
* What are the trends of Gold, Oil and the S&P 500 Index in relation to natural disasters? (GFC, 911)
* What are the potential long-term effects of war from the analysis of previous war data? (Afganistan, Iraq Wars)
* What are the current short-term effects of war? (Ukraine Russia War)

### Sources of Data

For this analysis our group sourced data from the yFinance python library.
yFinance is an open-source tool that uses Yahoo Finance's publicly avaliable API to provide financial data.

* [Gold, Oil and the S&P 500 Index Data](https://pypi.org/project/yfinance/)


# Analysis
## 911


## GFC


## COVID

See below the cumulative return of Gold, Oil and the S&P 500 Index during the COVID-19 pandemic.

![Cumulative Return](Images/cumulative_return_covid.png)


Oil violitility has been very significant in 2020, especially around the Covid-19 timeline as per chart. 
We can note on 2020, the worldwide demand for oil fell rapidly as Governments closed businesses and restricted travel due to the COVID-19 pandemic
Additionally during this big spike in volatility. An oil price war occured between Saudi Arabia and Russia after the two countries failed to agree on oil production levels. Throughout the remainder of the COVID period oil remained more volatile than Gold and the S&P 500.

In previous events gold is considered a "safe haven" when stock prices begin to turn sour. In relation to COVID-19 gold prices rose around 28% from January 1 to August 14, 2020 reaching a max price of $2051.50 USD


![Volatility](Images/covid_volatility.png)

The above plot measures the change in variance in the returns over a specific period of time. The volatility is calculated by taking a rolling window standard deviation on the % change.

We note from this plot that the volatility of Oil price has increased significantly over the COVID-19 period compared to Oil and the S&P 500 Index.

