# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal, on=['year','month','day'])

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

