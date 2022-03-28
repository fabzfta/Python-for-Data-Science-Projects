#In this exercise we find the median of incomes by zip-code, in order to take a look on business data by a demographic perspective
#databases: licenses, wards, zip_demo

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on="zip") \
            			.merge(wards, on="ward")

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({'income':'median'}))

# Only a few aldermen represent businesses in areas where the median income is greater than $62,000, which is the median income for the state of Illinois.


