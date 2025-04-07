# ai_price_project

A simple, fast, and explainable ML-based tool that estimates product prices based on size, brand rating, and category — inspired by real-world B2B pricing systems like those used at PROS.

SmartPrice is a command-line app that:

- Trains a machine learning model using historical product pricing data

- Takes user input (size, brand rating, category) (currently using a fake file with info)

- Predicts a likely price using a linear regression model

How It Works:

- Loads a dataset (data.csv) of past product sales

- Trains a linear regression model on size, brand rating, and category

- Accepts user input via command-line

- Predicts price and prints it

This was built to practice important skills in trained models that use data to learn and make predictions. While not deep-learning or gen ai, the project provides me a simple intro to models that achieve objectives that are related to the type of (much more complex) models PROS uses
