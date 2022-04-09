# General data

# Imports
import plotly.express as px
import panel as pn
import pandas as pd
import datetime as dt
import os
if not os.path.exists("Images"):
    os.mkdir("Images")
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import yfinance as yf
import requests
from panel.interact import interact
from panel import widgets
import json
from MCForecastTools import MCSimulation

pd.options.plotting.backend = 'holoviews'
pn.extension()
import hvplot.pandas


# Setup all DataFrames
# Gold

gold = yf.download('GC=F', period='max')
gold_data = pd.DataFrame(gold['Close']).dropna().rename(columns={"Close": "Gold"})

# Oil

oil = yf.download("CL=F", period='max')
oil_data = pd.DataFrame(oil['Close']).dropna().rename(columns={"Close": "Oil"})

# S&P 500

snp = yf.download('^GSPC', period='max')
snp_data = pd.DataFrame(snp['Close']).dropna().rename(columns={"Close": "S&P 500"})

# Setup all DataFrames (for Alex)
# Gold

gold = yf.download('GC=F', period='max')
gold_data1 = pd.DataFrame(gold['Close']).dropna().rename(columns={"Close": "close"})

# Oil

oil = yf.download("CL=F", period='max')
oil_data1 = pd.DataFrame(oil['Close']).dropna().rename(columns={"Close": "close"})

# S&P 500

snp = yf.download('^GSPC', period='max')
snp_data1 = pd.DataFrame(snp['Close']).dropna().rename(columns={"Close": "close"})

today = pd.to_datetime('today')

# Slice out Data
# GFC

gold_data_gfc = gold_data.loc["2006-06-01":"2010-01-01"]
oil_data_gfc = oil_data.loc["2006-06-01":"2010-01-01"]
snp_data_gfc = snp_data.loc["2006-06-01":"2010-01-01"]

# 9/11 and Afghan

gold_data_911 = gold_data.loc["2000-10-07":"2005-08-30"]
oil_data_911 = oil_data.loc["2000-10-07":"2005-08-30"]
snp_data_911 = snp_data.loc["2000-10-07":"2005-08-30"]

# COVID-19

gold_data_covid = gold_data.loc["2018-12-31":today]
oil_data_covid = oil_data.loc["2018-12-31":today]
snp_data_covid = snp_data.loc["2018-12-31":today]

# Potential long-term effects of war from the analysis of previous war data? Ukraine Russia War
# Afghanistan war

gold_data_afghan = gold_data1.loc["2015-10-01":"2021-08-30"]
oil_data_afghan = oil_data1.loc["2015-10-01":"2021-08-30"]
snp_data_afghan = snp_data1.loc["2015-10-01":"2021-08-30"]

# Iraq war

gold_data_iraq = gold_data1.loc["2007-05-01":"2012-12-15"]
oil_data_iraq = oil_data1.loc["2007-05-01":"2012-12-15"]
snp_data_iraq = snp_data1.loc["2007-05-01":"2012-12-15"]

# What are the current short-term effects of war? (Ukraine Russia War)

gold_data_short = gold_data.loc["2022-02-24":today]
oil_data_short = oil_data.loc["2022-02-24":today]
snp_data_short = snp_data.loc["2022-02-24":today]

# Concat by every event
# GFC
event_gfc = pd.concat(
    [gold_data_gfc, oil_data_gfc, snp_data_gfc], axis="columns", join="inner"
)
# 9/11

event_911 = pd.concat(
    [gold_data_911, oil_data_911, snp_data_911], axis="columns", join="inner"
)

# COVID-19

event_covid = pd.concat(
    [gold_data_covid, oil_data_covid, snp_data_covid], axis="columns", join="inner"
)

# Potential long-term effects of war from the analysis of previous war data? Ukraine Russia War

# What are the current short-term effects of war? (Ukraine Russia War)

event_short = pd.concat(
    [gold_data_short, oil_data_short, snp_data_short], axis="columns", join="inner"
)
################# Vinay's Code

################# Abdul's Code

################# Andrew's Code

################# Alex's Code 

# Slice event_long data

gold_data_afghan['symbol'] = 'GC=F'
oil_data_afghan['symbol'] = 'CL=F'
snp_data_afghan['symbol'] = '^GSPC'

gold_data_iraq['symbol'] = 'GC=F'
oil_data_iraq['symbol'] = 'CL=F'
snp_data_iraq['symbol'] = '^GSPC'

# Format Data for Gold Afghan
def format_MCSimulation(gold_data_afghan):
    ticker_list = gold_data_afghan['symbol'].unique()
    df_ = pd.DataFrame()
    for ticker in ticker_list:
        df_ticker_reformatted_gold_afghan = gold_data_afghan[gold_data_afghan['symbol'] == ticker]
        df_ticker_reformatted_gold_afghan.columns = pd.MultiIndex.from_product([[ticker],gold_data_afghan.columns])
        if df_.empty:
            df_ = df_ticker_reformatted_gold_afghan
        else:
            df_ = pd.concat([df_,
                            df_ticker_reformatted_gold_afghan],
                            axis = 1,
                            join='inner')

    return df_
df_ticker_reformatted_gold_afghan = format_MCSimulation(gold_data_afghan)

# Format Data for Oil Afghan
def format_MCSimulation(oil_data_afghan):
    ticker_list = oil_data_afghan['symbol'].unique()
    df_ = pd.DataFrame()
    for ticker in ticker_list:
        df_ticker_reformatted_oil_afghan = oil_data_afghan[oil_data_afghan['symbol'] == ticker]
        df_ticker_reformatted_oil_afghan.columns = pd.MultiIndex.from_product([[ticker],oil_data_afghan.columns])
        if df_.empty:
            df_ = df_ticker_reformatted_oil_afghan
        else:
            df_ = pd.concat([df_,
                            df_ticker_reformatted_oil_afghan],
                            axis = 1,
                            join='inner')

    return df_
df_ticker_reformatted_oil_afghan = format_MCSimulation(oil_data_afghan)

# Format Data for S&P 500 Afghan
def format_MCSimulation(snp_data_afghan):
    ticker_list = snp_data_afghan['symbol'].unique()
    df_ = pd.DataFrame()
    for ticker in ticker_list:
        df_ticker_reformatted_snp_afghan = snp_data_afghan[snp_data_afghan['symbol'] == ticker]
        df_ticker_reformatted_snp_afghan.columns = pd.MultiIndex.from_product([[ticker],snp_data_afghan.columns])
        if df_.empty:
            df_ = df_ticker_reformatted_snp_afghan
        else:
            df_ = pd.concat([df_,
                            df_ticker_reformatted_snp_afghan],
                            axis = 1,
                            join='inner')

    return df_
df_ticker_reformatted_snp_afghan = format_MCSimulation(snp_data_afghan)

# Format Data for Gold Iraq

def format_MCSimulation(gold_data_iraq):
    ticker_list = gold_data_iraq['symbol'].unique()
    df_ = pd.DataFrame()
    for ticker in ticker_list:
        df_ticker_reformatted_gold_iraq = gold_data_iraq[gold_data_iraq['symbol'] == ticker]
        df_ticker_reformatted_gold_iraq.columns = pd.MultiIndex.from_product([[ticker],gold_data_iraq.columns])
        if df_.empty:
            df_ = df_ticker_reformatted_gold_iraq
        else:
            df_ = pd.concat([df_,
                            df_ticker_reformatted_gold_iraq],
                            axis = 1,
                            join='inner')

    return df_
df_ticker_reformatted_gold_iraq = format_MCSimulation(gold_data_iraq)

# Format Data for Oil Iraq

def format_MCSimulation(oil_data_iraq):
    ticker_list = oil_data_iraq['symbol'].unique()
    df_ = pd.DataFrame()
    for ticker in ticker_list:
        df_ticker_reformatted_oil_iraq = oil_data_iraq[oil_data_iraq['symbol'] == ticker]
        df_ticker_reformatted_oil_iraq.columns = pd.MultiIndex.from_product([[ticker],oil_data_iraq.columns])
        if df_.empty:
            df_ = df_ticker_reformatted_oil_iraq
        else:
            df_ = pd.concat([df_,
                            df_ticker_reformatted_oil_iraq],
                            axis = 1,
                            join='inner')

    return df_
df_ticker_reformatted_oil_iraq = format_MCSimulation(oil_data_iraq)

# Format Data for S&P 500 Iraq

def format_MCSimulation(snp_data_iraq):
    ticker_list = snp_data_iraq['symbol'].unique()
    df_ = pd.DataFrame()
    for ticker in ticker_list:
        df_ticker_reformatted_snp_iraq = snp_data_iraq[snp_data_iraq['symbol'] == ticker]
        df_ticker_reformatted_snp_iraq.columns = pd.MultiIndex.from_product([[ticker],snp_data_iraq.columns])
        if df_.empty:
            df_ = df_ticker_reformatted_snp_iraq
        else:
            df_ = pd.concat([df_,
                            df_ticker_reformatted_snp_iraq],
                            axis = 1,
                            join='inner')

    return df_
df_ticker_reformatted_snp_iraq = format_MCSimulation(snp_data_iraq)

# Monte Carlo Simulation for potential long-term effects of war from the analysis of previous war data
# Gold Afghan

monte_carlo_gold_afghan = MCSimulation(
    portfolio_data = df_ticker_reformatted_gold_afghan,
    num_simulation = 1000,
    num_trading_days = 252
)

# Oil Afghan

monte_carlo_oil_afghan = MCSimulation(
    portfolio_data = df_ticker_reformatted_oil_afghan,
    num_simulation = 1000,
    num_trading_days = 252
)

# S&P 500 Afghan

monte_carlo_snp_afghan = MCSimulation(
    portfolio_data = df_ticker_reformatted_snp_afghan,
    num_simulation = 1000,
    num_trading_days = 252
)

# Gold Iraq

monte_carlo_gold_iraq = MCSimulation(
    portfolio_data = df_ticker_reformatted_gold_iraq,
    num_simulation = 1000,
    num_trading_days = 252
)

# Oil Iraq

monte_carlo_oil_iraq = MCSimulation(
    portfolio_data = df_ticker_reformatted_oil_iraq,
    num_simulation = 1000,
    num_trading_days = 252
)

# S&P 500 Iraq

monte_carlo_snp_iraq = MCSimulation(
    portfolio_data = df_ticker_reformatted_snp_iraq,
    num_simulation = 1000,
    num_trading_days = 252
)

# Running Monte Carlo Simulations
# Gold Afghan
monte_carlo_gold_afghan.calc_cumulative_return()
# Oil Afghan
monte_carlo_oil_afghan.calc_cumulative_return()
# S&P500 Afghan
monte_carlo_snp_afghan.calc_cumulative_return()
# Gold Iraq
monte_carlo_gold_iraq.calc_cumulative_return()
# Oil Iraq
monte_carlo_oil_iraq.calc_cumulative_return()
# S&P500 Iraq
monte_carlo_snp_iraq.calc_cumulative_return()

# Compute summary statistics from the simulated monthly returns
simulated_gold_afghan_returns_data = {
    "mean": list(monte_carlo_gold_afghan.simulated_return.mean(axis='columns')),
    "median": list(monte_carlo_gold_afghan.simulated_return.median(axis='columns')),
    "min": list(monte_carlo_gold_afghan.simulated_return.min(axis='columns')),
    "max": list(monte_carlo_gold_afghan.simulated_return.max(axis='columns'))
}


simulated_oil_afghan_returns_data = {
    "mean": list(monte_carlo_oil_afghan.simulated_return.mean(axis='columns')),
    "median": list(monte_carlo_oil_afghan.simulated_return.median(axis='columns')),
    "min": list(monte_carlo_oil_afghan.simulated_return.min(axis='columns')),
    "max": list(monte_carlo_oil_afghan.simulated_return.max(axis='columns'))
}

simulated_snp_afghan_returns_data = {
    "mean": list(monte_carlo_snp_afghan.simulated_return.mean(axis='columns')),
    "median": list(monte_carlo_snp_afghan.simulated_return.median(axis='columns')),
    "min": list(monte_carlo_snp_afghan.simulated_return.min(axis='columns')),
    "max": list(monte_carlo_snp_afghan.simulated_return.max(axis='columns'))
}

simulated_gold_iraq_returns_data = {
    "mean": list(monte_carlo_gold_iraq.simulated_return.mean(axis='columns')),
    "median": list(monte_carlo_gold_iraq.simulated_return.median(axis='columns')),
    "min": list(monte_carlo_gold_iraq.simulated_return.min(axis='columns')),
    "max": list(monte_carlo_gold_iraq.simulated_return.max(axis='columns'))
}

simulated_oil_iraq_returns_data = {
    "mean": list(monte_carlo_oil_iraq.simulated_return.mean(axis='columns')),
    "median": list(monte_carlo_oil_iraq.simulated_return.median(axis='columns')),
    "min": list(monte_carlo_oil_iraq.simulated_return.min(axis='columns')),
    "max": list(monte_carlo_oil_iraq.simulated_return.max(axis='columns'))
}

simulated_snp_iraq_returns_data = {
    "mean": list(monte_carlo_snp_iraq.simulated_return.mean(axis='columns')),
    "median": list(monte_carlo_snp_iraq.simulated_return.median(axis='columns')),
    "min": list(monte_carlo_snp_iraq.simulated_return.min(axis='columns')),
    "max": list(monte_carlo_snp_iraq.simulated_return.max(axis='columns'))
}

# Create a DataFrames with the summary statistics

df_simulated_returns_gold_afghan = pd.DataFrame(simulated_gold_afghan_returns_data).rename(columns={'mean':'Gold After Afghan War'})

df_simulated_returns_oil_afghan = pd.DataFrame(simulated_oil_afghan_returns_data).rename(columns={'mean':'Oil After Afghan War'})

df_simulated_returns_snp_afghan = pd.DataFrame(simulated_snp_afghan_returns_data).rename(columns={'mean':'S&P 500 After Afghan War'})
    
df_simulated_returns_gold_iraq = pd.DataFrame(simulated_gold_iraq_returns_data).rename(columns={'mean':'Gold After Iraq War'})

df_simulated_returns_oil_iraq = pd.DataFrame(simulated_oil_iraq_returns_data).rename(columns={'mean':'Oil After Iraq War'})

df_simulated_returns_snp_iraq = pd.DataFrame(simulated_snp_iraq_returns_data).rename(columns={'mean':'S&P 500 After Iraq War'})

# Configure data
# Gold after Afghan

plot_gold_afghan = df_simulated_returns_gold_afghan[['Gold After Afghan War']]

# Oil after Afghan

plot_oil_afghan = df_simulated_returns_oil_afghan[['Oil After Afghan War']]

# S&P 500 after Afghan

plot_snp_afghan = df_simulated_returns_snp_afghan[['S&P 500 After Afghan War']]

# Gold after Iraq

plot_gold_iraq = df_simulated_returns_gold_iraq[['Gold After Iraq War']]

# Oil after Iraq

plot_oil_iraq = df_simulated_returns_oil_iraq[['Oil After Iraq War']]

# S&P 500 after Iraq

plot_snp_iraq = df_simulated_returns_snp_iraq[['S&P 500 After Iraq War']]

combined_df_iraq = pd.concat([plot_gold_iraq, plot_oil_iraq, plot_snp_iraq])

combined_df_afghan = pd.concat([plot_gold_afghan, plot_oil_afghan, plot_snp_afghan])

# Alex's functions

def alex_plot_afghan():
    plot1 = combined_df_afghan.hvplot(label="Monte Carlo Simulation of Gold, Oil, and S&P 500 after the Afghanistan War (252 days = 1 year)", width = 800)
    return plot1

def alex_plot_iraq():
    plot2 = combined_df_iraq.hvplot(label="Monte Carlo Simulation of Gold, Oil, and S&P 500 after the Iraq War (252 days = 1 year)", width = 800)
    return plot2

################# Jack's Code