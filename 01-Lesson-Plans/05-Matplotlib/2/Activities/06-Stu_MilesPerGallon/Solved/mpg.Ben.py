# Import Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
cars_df = pd.read_csv("../Resources/mpg.csv")
cars_df
cars_df = cars_df.set_index('car name')
cars_df = cars_df.loc[cars_df["horsepower"] != "?"]
cars_df['horsepower'] = pd.to_numeric(cars_df['horsepower'])
cars_df
cars_df.plot(kind="scatter" ,x="horsepower", y="mpg", grid=True, figsize=(20,10), title="Hp Vs. MPG")