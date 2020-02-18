-COVID-19 January Flight Dataset Dictionary-

This dataset is primarily to espouse the connection between Chinese airports and United States airports
during the month of January. This month coincides with increased reported transmission of the COVID-19 virus that 
originated in the city of Wuhan, part of the Hubei province in China. The hope is that this dataset can 
be used to link Chinese prefecture level data with United States county level data in an effort to do 
some spatial analysis on the spread of COVID-19 in America during the month of January.

The dataset is referred to as 'Jan_UScounty_CNprefecture.csv'

To recreate this dataset, you will need these datasets in a working directory folder (however, you should have these files already in the folder you are reading this Data Description file in):
1. CBP CN to US Daily Pax & Flights 20191229-20200129.csv
2. Airport Name Lookup - Name-Match-Lookup-Table_v2.csv
3. USArrivalCountyNames.csv*

*This table was created by looking at the unique arrival airports and researching their corresponding county and state data.

You can run this R script in RStudio to create the dataset:
1. COVID19_jan_flights.R

Here are the detailed descriptions of each column of data in the file:
ArrivalDate: This records the date of the departure flight from China to the arrival flight in United States.
USFirstPortifEntry: The United States arrival flight Port of Entry. They are defined additionally by the U.S. Customs and Border Protection Port of Entry Codes, the four digit numbers within the parantheses.
TotalPax: Records the number of passengers from departure flight in China to the arrival flight in America. We found that multiple rows correspond to the same flight but with different flight numbers. This field should be summed up by identical rows
DepartureAptCode: The three letter code of the departure airport in China
DepartureAirportName: The full name of the Chinese departure airport
DepartureCtryCode: Code of the departure Country. Should only contain 'CN' for China. Although this is redundant, we still keep it in the dataset because it was apart of the original data file we were given, and might be useful in other contexts.
DepartureCtryName: Name of the departure Country. Should only contain 'China'. Although this is redundant, we still keep it in the dataset because it was apart of the original data file we were given, and might be useful in other contexts.
LastConnectionAirport: Last Airport Name before coming to the United States arrival airport
LastConxCtryCode: Last Connection Country Code. Two letter abbreviation
LastConxCtryName: Last Connection Country Name. Full name is spelled out.
AirlineCode: Two Letter code to distinguish which airline was responsible for the flight from a Chinese departure airport to a US arrival airport
FlightNumber: Symbolizes the route the flight takes to get to the arrival airport
DirectOrIndirect: Records if this flight is direct or indirect from the departure airport to the arrival airport. Direct flights go directly from China to America, while Indirect Flights make multiple connection flights before Arriving in America.
OpenFlightsAirportID: Unique OpenFlights API identifier for the departure airport. These IDs correlate to Chinese departure airports
OpenFlightsName: Name of the departure Airport from the OpenFlights API. These names correspond to Chinese departure airports
DepartureAirportProvince: The Chinese province the departure airport is located in. Contain Chinese Provinces
DepartureAirportPrefecture: The Chinese prefecture the departure airport is located in. Contain Chinese Prefectures
USArrivalCounty: The U.S. county the arrival airport is located in. Contains only U.S. Counties, and if the arrival airport is not a county it is recorded as Other. Reference USArrivalTerritoryOrPreclear for specific information
USArrivalState: The U.S. state the arrival airport is located in. Contains only U.S. States, and if the arrival airport is not a state it is recorded as Other. Reference USArrivalTerritoryOrPreclear for specific information
USArrivalTerritoryOrPreclear: U.S. Territories and U.S. Customs and Border Protections are not considered States or Counties. Records specific information about where the arrival airport is. 

For anymore questions regarding the data, please email noahaus@uga.edu. 