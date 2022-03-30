#You have been given gdp, which is a table of quarterly GDP values of the US during the 1980s. Additionally, the table recession has been given to you. It holds the starting date of every US recession since 1980, and the date when the recession was declared to be over.
#Using merge_asof() to merge the tables and create a status flag if a quarter was during a recession.

# Merging gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp,recession,on="date")

# Creating a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Ploting a bar chart of gdp_recession
gdp_recession.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.show()

# We can see from the chart that there were a number of quarters early in the 1980s where a recession was an issue.

