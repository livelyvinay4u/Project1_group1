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
import numpy as np

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

#subplots
def gfc_subplots():
    
    event_gfc_pct_change = event_gfc.pct_change().dropna()
    event_gfc_normalized = (event_gfc_pct_change - event_gfc_pct_change.min())/(event_gfc_pct_change.max() - event_gfc_pct_change.min())
    event_gfc_standardize = (event_gfc_normalized-event_gfc_normalized.mean())/event_gfc_normalized.std()
 
    event_gfc_subplots = event_gfc_standardize.hvplot(x='Date',
                                                     y=["Gold","Oil","S&P 500"],
                                                     value_label='Closing Price',
                                                     subplots=True,
                                                     width=600,
                                                     height=400,
                                                     shared_axes=False).cols(2)
    return event_gfc_subplots


#line plot
def gfc_lineplot():
    event_gfc_pct_change = event_gfc.pct_change().dropna()
    event_gfc_normalized = (event_gfc_pct_change - event_gfc_pct_change.min())/(event_gfc_pct_change.max() - event_gfc_pct_change.min())
    event_gfc_standardize = (event_gfc_normalized-event_gfc_normalized.mean())/event_gfc_normalized.std()
       
    event_gfc_lineplot = event_gfc_standardize.hvplot.line(x="Date",
                                                          y=["Gold","Oil","S&P 500"],
                                                          value_label="Close Price",
                                                          legend='top',
                                                          height=500,
                                                          width=1320)

    return event_gfc_lineplot


###Joint plots###
#S&P 500 vs Gold

def gfc_jointplot_snp_gold():
    event_gfc_pct_change = event_gfc.pct_change().dropna()
    event_gfc_normalized = (event_gfc_pct_change - event_gfc_pct_change.min())/(event_gfc_pct_change.max() - event_gfc_pct_change.min())
    event_gfc_standardize = (event_gfc_normalized - event_gfc_normalized.mean())/event_gfc_normalized.std()
    
    snp_vs_gold = sns.jointplot(x="S&P 500",
                                y="Gold",
                                data=event_gfc_standardize,
                                height = 10,
                                kind='reg'
                               )

    return snp_vs_gold


#S&P 500 vs Oil

def gfc_jointplot_snp_oil():
    event_gfc_pct_change = event_gfc.pct_change().dropna()
    event_gfc_normalized = (event_gfc_pct_change - event_gfc_pct_change.min())/(event_gfc_pct_change.max() - event_gfc_pct_change.min())
    event_gfc_standardize = (event_gfc_normalized - event_gfc_normalized.mean())/event_gfc_normalized.std()
    
    snp_vs_oil = sns.jointplot(x="S&P 500",
                               y="Oil",
                               data=event_gfc_standardize,
                               height = 10,
                               kind='reg'
                              )

    return snp_vs_oil


#Gold vs Oil

def gfc_jointplot_gold_oil():
    event_gfc_pct_change = event_gfc.pct_change().dropna()
    event_gfc_normalized = (event_gfc_pct_change - event_gfc_pct_change.min())/(event_gfc_pct_change.max() - event_gfc_pct_change.min())
    event_gfc_standardize = (event_gfc_normalized - event_gfc_normalized.mean())/event_gfc_normalized.std()
    
    oil_vs_gold = sns.jointplot(x="Oil",
                                y="Gold",
                                data=event_gfc_standardize,
                                height = 10,
                                kind='reg'
                               )
    
    return oil_vs_gold


################# Abdul's Code
Ukraine_Russia_war = event_short
Ukraine_Russia_war
Afghan_war= event_911
Afghan_war
Afghan_war=Afghan_war.loc["2001-10-07":"2001-12-01"]
Afghan_war
Afghan_war.hvplot(x='Date', y='', title= 'Short-term effects of Afghan War', value_label='Percentage Change')
Ukraine_Russia_war.loc["2022-02-24":"2022-04-05"]
Ukraine_Russia_war.hvplot(x='Date', y=['Gold',"Oil","S&P 500"], title= 'Short-term effects of Ukraine/Russian War', value_label='Percentage Change')
################# Andrew's Code COVID




# calc cum daily returns

# Interactive Chart with date slider at the bottom - cum returns
def cum_returns():
    # % Change variables
    # Drop NaN values
    covid_pct_change = event_covid.pct_change()
    covid_pct_change.dropna()
    cum_covid_return = (1+ covid_pct_change).cumprod()
    cum_df = cum_covid_return.copy()
    cum_df1 = cum_df.reset_index()
    cum_df1.columns=['Date','Gold','Oil','S&P 500']
    fig = px.line(cum_df1, x='Date', y=cum_df1.columns[1:4], title='Cumulative Return of Gold, Oil and S&P500 Index During COVID')
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
                ])
        )
    )
    return fig



# vol chart
def vol_plt():
    # % Change variables
    # Drop NaN values
    covid_pct_change = event_covid.pct_change()
    covid_pct_change.dropna()
    # Define the minumum of periods
    min_periods = 5
    # Volatility calc
    vol = covid_pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 
    vol_covid = vol.hvplot(
        figsize=(20, 10), 
        title = "Volatility of Gold, Oil and the S&P 500 Index during COVID"
        )
    return vol_covid

# scatter matrix
def scatter_matrix():
    # % Change variables
    # Drop NaN values
    covid_pct_change = event_covid.pct_change().dropna()
    scatter_matrix_covid = pd.plotting.scatter_matrix(
        covid_pct_change, 
        diagonal='kde', 
        alpha=1,figsize=(15,15)
        )
    return scatter_matrix_covid

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

#line plots

def event_911_lineplot():
    
    plt.xlabel("Years")
    plt.title ("Prices of Commodities during 911")
    plt.plot(oil_data.loc["2000-10-07":"2005-08-30"], label="Oil")
    plt.plot(snp_data.loc["2000-10-07":"2005-08-30"], label="S&P 500")
    plt.plot(gold_data.loc["2000-10-07":"2005-08-30"], label="Gold")
    plt.legend()
    plt.grid()

#gold price

def event_911_goldplot():
    gold_plot = gold_data_911.hvplot.line(x="Date",value_label='Closing Price',color='red',title="Gold close prices")
    return gold_plot

#oil price 

def event_911_oilplot():
    oil_plot = oil_data_911.hvplot.line(x="Date",value_label='Closing Price',color='yellow',title="Oil close prices")

    return oil_plot

#snp 500

def event_911_snp500():
    snp_plot = snp_data_911.hvplot.line(x="Date",value_label='Closing Price',color='green',title="SNP 500 close prices")

    return snp_plot



