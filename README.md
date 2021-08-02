<div align = "center">

<h3>Becode AI & web dev training

group assignment: Deployment & POST/GET requests</h3>


<img width = "200" src = /assets/BeCode_Logo.png>
</div>

# Immo Eliza: Deployment and web dev collaboration
Website that takes several features and predicts the price of a house

## Table of contents
[Description](#Description)  
[Installation](#Installation)  
[Usage](#Usage)  
[Output](#Output)  
[How it works](#How-it-works)  
[Examples](#Examples)  
[Authors](#Authors)

## Description
The website will ask for 13 input values, of which 8 are obligatory and 5 optional. With the collected data (in the form of a dictionary), a prediction is made, based on a machine learning model that is derived from the database.

## Installation
No installation required: when the website is run, the container provides all the necessities.

## Usage
On the website, the user is asked to fill out the 8 obligatory and 5 optional data. When they ask for the calculation, the prediction is returned.

## Output
The user gets an estimate of the price.

## How it works

When the prediction is called, a .pkl file is created that contains the actual model, based on data that have been scraped from ImmoWeb.be and afterwards have been cleaned. NaN-values have been filled out or deleted, outliers omitted, and columns that had little correlation to the price were dropped as well. That database is then used to train the model (which is saved in the .pkl-file), which is in its turn applied to the data that the user provides.

The user-data are also cleaned, the shape is equalized to that of the model and the prediction is made.

## Examples

## Authors
Pauwel De Wilde

## Special thanks
Thanks to Jesús Bueno for a lot of debugging, pieces of code, information and help.