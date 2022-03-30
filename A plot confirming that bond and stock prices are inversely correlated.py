#It is widespread knowledge that the price of bonds is inversely related to the price of stocks.
#Let's show this with some data!

import pandas as pd
import matplotlib.pyplot as plt

# Using melt on ten_yr, unpivoting everything besides the metric column
bond_perc = ten_yr.melt(id_vars=['metric'], var_name="date", value_name = "close")

# Using query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric =="close"')

# Merging (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji,bond_perc_close, on="date", how="inner", suffixes=["_dow","_bond"])


# Ploting only the close_dow and close_bond columns
dow_bond.plot(y=["close_dow","close_bond"], x='date', rot=90)
plt.show()

# According to the plot, often as the price of stocks increases, the price for bonds decreases.

