#buoy play
'''The following uses a library called buoyant to donwload csv data from https://sdf.ndbc.noaa.gov/. 
This does not get realtime data as of yet, another approach will need to be investigated to get 
real time data.
'''

from buoyant import Buoy
import json
from datetime import datetime
import time
from apscheduler.scheduler import Scheduler

def get_buoy_data(buoy_id):
	buoy = Buoy(buoy_id)
	#buoy.refresh()
	significant_wave_height_meters = buoy.waves.get('sea_surface_wave_significant_height')
	#print(buoy.waves)

	significant_wave_height_feet = significant_wave_height_meters // .3048 
	significant_wave_height_inches = significant_wave_height_meters / .3048 % 1 * 12

	print("SURF REPORT FOR " +  str(buoy_id) + " " + str(datetime.now()))
	print("*significant waves height for this buoy is" + " " + str(significant_wave_height_feet) + "feet " + str(significant_wave_height_inches) + " inches")
	#print(buoy.waves.get('sea_surface_wave_significant_height'))
	print("*significant wave period for this buoy is" + " " + str(buoy.waves.get('sea_surface_wave_peak_period')))
	

#get_buoy_data(46025)

def buoy_timer(run_minutes):
    """Periodically checks buoy information."""
    listen = True # listen boolean
    start = datetime.now() # start time
    while(listen): #while listen = True, run loop
        get_buoy_data(46025)
        get_buoy_data(46054)
        now = datetime.now()
        duration = (now - start)
        seconds = duration.total_seconds()
        minutes = int(seconds/60)
        if minutes >= run_minutes: #check run time
            print("Finished.")
            listen = False

        time.sleep(30) #Wait N minutes to check again.    
    return
run_minutes = float(input("Enter run duration in minutes:"))
buoy_timer(run_minutes)


#SCRATCH
#example methods
#print(dir(Buoy))
#print(buoy.air_pressure_at_sea_level)
#print(buoy.coords)
#To Do: will need to print buoy name




#print("sea_surface_wave_mean_period" + " " + buoy.waves.get('sea_surface_wave_mean_period'))
#print("sea_surface_swell_wave_period" + " " + buoy.waves.get('sea_surface_swell_wave_period'))
#print("sea_surface_wind_wave_significant_height" + " " + buoy.waves.get('sea_surface_wind_wave_significant_height'))
#print("sea_surface_wind_wave_period" + buoy.waves.get('sea_surface_wind_wave_period'))
#print("sea_surface_wave_to_direction" + buoy.waves.get('sea_surface_wave_to_direction'))
#print("sea_surface_swell_wave_to_direction" + " " + buoy.waves.get('sea_surface_swell_wave_to_direction'))
#print("sea_surface_wind_wave_to_direction" + " " + buoy.waves.get('sea_surface_wind_wave_to_direction'))

#investigate waves dict
# Print contents of dict in json like format
#print(json.dumps(buoy.waves, indent=4))

'''the following data points are available
	"sea_surface_wave_significant_height": 0.89,
    "sea_surface_wave_peak_period": 14.81,
    "sea_surface_wave_mean_period": 7.47,
    "sea_surface_swell_wave_significant_height": 0.87,
    "sea_surface_swell_wave_period": 14.8,
    "sea_surface_wind_wave_significant_height": 0.19,
    "sea_surface_wind_wave_period": 4.0,
    "sea_water_temperature": null,
    "sea_surface_wave_to_direction": 346.0,
    "sea_surface_swell_wave_to_direction": 346.0,
    "sea_surface_wind_wave_to_direction": 59.0,
    "number_of_frequencies": 46.0,
    "center_frequencies: [long list]
    "bandwidths": [long list]
    mean_wave_direction: [146.0]
    "principal_wave_direction": [155.0,
    "calculation_method": "UNKNOWN
'''

'''
# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()

def job_function():
    print("Hello World")
    print(datetime.datetime.now())
    time.sleep(20)

# Schedules job_function to be run once each minute
sched.add_cron_job(job_function,  minute='0-59')
'''




