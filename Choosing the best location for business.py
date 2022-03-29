#You need a location with a great deal of space and relatively few businesses and people around to build your goat farm and to avoid complaints about the smell.
# 3 Databases: The land_use table has info on the percentage of vacant land by city ward. The census table has population by ward, and the licenses table lists businesses by ward.

# Merging land_use and census and merge resulting with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Grouping by ward, pop_2010, and vacant, then counting the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'],
                                   as_index=False).agg({'account':'count'})

# Sorting pop_vac_lic and printing the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant","account","pop_2010"],
                                             ascending=[False,True,True])

# Printing the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())


# The ward number seven would be the best place to build the goat farm!
