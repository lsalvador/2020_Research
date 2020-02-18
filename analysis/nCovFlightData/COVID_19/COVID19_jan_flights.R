# Link Chinese and American Gravity models with an airport travel network. Networks created are
# separated by day. Reports the busiest airports, ranked, everyday in January.
# Noah Legall, Liliana Salvador PhD

install.packages("dplyr")
library(dplyr)

## 1. read in the data. do some processing to the first column name.
#January Flight data between China and North America
flight_data <- read.csv("CBP CN to US Daily Pax & Flights 20191229-20200129.csv",header = TRUE,fileEncoding = 'UTF-8-BOM')

#Chinese Airport to prefecture data table
air_to_prefect <- read.csv("Airport Name Lookup - Name-Match-Lookup-Table_v2.csv",header = TRUE)

#US county data that corresponds with the arrivals in the data set.
us_county_names <- read.csv("USArrivalCountyNames.csv", header = TRUE)

#join the data to the original data
prefect_flight <- flight_data %>% left_join(air_to_prefect, by = c("DepartureAirportName" = "airport"))
prefect_county_flight <- prefect_flight %>% left_join(us_county_names, by = c("USFirstPortofEntry"))
drop <- c("notes","Name","china","ADM0_country","airport_type")
prefect_county_flight <- prefect_county_flight[, !(names(prefect_county_flight) %in% drop)]
names(prefect_county_flight)[names(prefect_county_flight) == "DIRECT"] <- "DirectOrIndirect"
names(prefect_county_flight)[names(prefect_county_flight) == "OpenFlights_Airport_ID"] <- "OpenFlightDepartureAirportID"
names(prefect_county_flight)[names(prefect_county_flight) == "OpenFlights_Name"] <- "OpenFlightDepartureAirportName"
names(prefect_county_flight)[names(prefect_county_flight) == "OpenFlights_Name"] <- "OpenFlightDepartureAirportName"
names(prefect_county_flight)[names(prefect_county_flight) == "ADM1_province"] <- "DepartureAirportProvince"
names(prefect_county_flight)[names(prefect_county_flight) == "ADM2_prefecture"] <- "DepartureAirportPrefecture"
write.csv(prefect_county_flight,file="Jan_UScounty_CNprefecture.csv")