


import requests
import time
import sys
# from requests.utils import dump

base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2"

token = "tMRsggVkaElGAoPVgdaNWxwNSJxPhBml"

all_stations = base_url+"/stations"

data = base_url+"/datasets"


#- Command line utility that will count the number of stations in a given lat-lon rectangle
def stations_rect(ext):
    station_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
    url= f"{station_url}?extent={ext[0]},{ext[1]},{ext[2]},{ext[3]}"
    res1 = requests.get(url,headers={"token":token})
    res1_j = res1.json()
    #print(res1_j)
    res1_count = res1_j['metadata']['resultset']['count']
    return res1_count

#print(stations_rect([35.4444,-86.9999,35.8888,-86.7777]))

# - Give a weather report for a given area on a specified day

#def weather_report(year,month,day):
year= "2012"
month= "05"
day = "23"

date = f"{year}-{month}-{day}"

res2 = requests.get(data,headers={"token":token})
#print(res2)
res2_j = res2.json()
#print(res2_j)
res2_results = res2_j['results']
#
# for name in res2_results:
#     print(name['name'], name['id'])




data_url = base_url+"/data"
datatypes_url = base_url+"/datatypes"
url2 = f"{data_url}?datasetid=GHCND&locationid=ZIP:28790&startdate=2010-05-01&enddate=2010-05-01"
url3 = f"{datatypes_url}/PRECIP_15"
res3 = requests.get(url2,headers={"token":token})
#print(res3)
res3_j = res3.json()
#print(res3_j)
# res3_results = res3_j['results']
# for result in res3_results:
#     print(result['datatype'], result['value'])

# - Command line utility that can fetch temperature data for a given city on a given date (or any other kind of data)
location_url = base_url+"/locations"
#url4 = f"{datatypes_url}?locationid=ZIP:28801&datacategoryid=TEMP&limit=100&startdate=2010-05-01&enddate=2010-05-01&limit=25"
#url5 = f"{location_url}?locationcategoryid=&datacategoryid=TEMP&startdate=2010-05-01&enddate=2010-05-01&limit=25"
#url6 for temp for a city
#url6 = f"{data_url}?datasetid=GSOM&locationid=FIPS:37&startdate=2010-05-01&enddate=2010-05-31"


#TEMPARATURE DATA FOR A GIVEN CITY

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def temp_city(city,country_c,date):
    url7 = f"{location_url}?locationcategoryid=CITY&datacategoryid=TEMP&startdate={date}&enddate={date}"
    res4 = requests.get(url7, headers={"token": token})
    print(res4)
    res4_j = res4.json()
    #print(res4_j)

    city_id = {}
    city_count = res4_j['metadata']['resultset']['count']
    res4_results = res4_j['results']

    offset = 1
    limit = 1000

    while len(city_id) < city_count:
        start = time.time()
        u = f"{location_url}?locationcategoryid=CITY&datacategoryid=TEMP&startdate={date}&enddate={date}&offset={offset}&limit={limit}"
        res5 = requests.get(u, headers={"token": token})
        res5_json = res5.json()
        results1 = res5_json['results']
        for result in results1:
            city_id[result['name']] = result['id']
        offset += len(results1)
        end = time.time()
        elapsed = end - start
        print(f"{offset} - {elapsed}seconds")
    #print(city_id)
    cid= city_id[f"{city}, {country_c}"]
    url66 = f"{data_url}?datasetid=GHCND&locationid={cid}&startdate={date}&enddate={date}"
    ress = requests.get(url66,headers={"token":token})
    ress_j = ress.json()
    #print(ress_j)
    ress_results = ress_j['results']
    print("--STATION NAME--DATE--DATATYPE--VALUE--")
    for result in ress_results:
        print(result['station'],result['date'],result['datatype'], result['value'])
    print("--------------------------------------------------------------")


#--------------------------------------------------------------------------------------------------------------------------------------
#precipitation of a stations based in a certain Zip code
#station_id ={}

def Weather_report_zip(zipc,date):
    #https: // www.ncdc.noaa.gov / cdo - web / api / v2 / data?datasetid = GHCND & locationid = ZIP:28801 & startdate = 2010 - 05 - 01 & enddate = 2010 - 05 - 0
    url = f"{data_url}?datasetid=GHCND&locationid=ZIP:{zipc}&startdate={date}&enddate={date}"
    res = requests.get(url,headers={"token":token})
    res_j = res.json()
    #print(res_j)
    res_results = res_j['results']
    print("--STATION NAME--DATATYPE--VALUE--DATE--")
    for result in res_results:
        print(result['station'],result['datatype'], result['value'],result['date'])
    print("--------------------------------------------------------------")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def all_stations(zipc,date):
    station_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
    url = f"{station_url}?locationid=ZIP:{zipc}&startdate={date}&enddate={date}"
    res = requests.get(url, headers={"token": token})
    res_j = res.json()
    #print(res_j)
    res_results = res_j['results']
    for result in res_results:
        print(result['name'], result['id'])
    print("--------------------------------------------------------------")

# def all_reports(zipc,date):
#     station_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
#     url = f"{station_url}?locationid=ZIP:{zipc}&startdate={date}&enddate={date}"
#     res = requests.get(url, headers={"token": token})
#     res_j = res.json()
#     print(res_j)
#     res_results = res_j['results']
#     for result in res_results:
#         print(result['name'], result['id'])
#     print("--------------------------------------------------------------")
#     stations ={}
#     res_meta = res_j['metadata']
#     res_count = res_meta['resultset']['count']
#     offset = 1
#     limit =1000
#     while(len(stations)<res_count):
#         start = time.time()
#         url = f"{station_url}?locationid=ZIP:{zipc}&startdate={date}&enddate={date}&offset={offset}&limit={limit}"
#         res1 = requests.get(url,headers={"token":token})
#         res1_j = res1.json()
#         results = res1_j['results']
#         for result in results:
#             stations[result['name']] = result['id']
#         offset += len(results)
#         end = time.time()
#         elapsed = end - start
#         print(f"{offset} - {elapsed}seconds")
#     print(stations)
#     for v in stations.values():
#         url_p15 = f"{data_url}?datasetid=GHCND&stationid={v}&units=metric&startdate={date}&enddate={date}"
#         url_phly = f"{data_url}?datasetid=PRECIP_15&stationid={v}&units=metric&startdate={date}&enddate={date}"
#         #url_nexrad2= f"{data_url}?datasetid=NEXRAD2&stationid={v}&units=metric&startdate={date}&enddate={date}"
#         #url_nexrad3 = f"{data_url}?datasetid=NEXRAD3&stationid={v}&units=metric&startdate={date}&enddate={date}"
#         urls = [url_p15,url_phly]
#         for i in range(len(urls)):
#             res = requests.get(urls[i],headers={"token":token})
#             res_j = res.json()
#             if len(res_j) ==0:
#                 print(f"no output for this station--stationid--{v}")
#             else:
#                 results = res_j['results']
#                 for result in results:
#                     print(f"STATIONID----{v}--DATATYPE----{result['datatype']}--VALUE----{result['value']}")
#                     #print(result)
def main():
    done = False
    while (done == False):
        print("-------------Welcome to NOAA API-------------")
        print("Enter 1 for Command line utility that will count the number of stations in a given lat-lon rectangle\n"
              "Enter 2 for Command line utility that can fetch temperature data or data belongs to TEMP dataset for a given city on a given date\n"
              "Enter 3 to Give a weather report(Daily Summaries) for a given area(Zip code) on a specified day\n"
              "Enter 4 to Fetch all stations for a given area(ZIP CODE) on a specified day\n"
              "Enter 5 to exit the program")

        c = int(input("Enter Your choice : "))
        if c == 1:
            print("Enter the latitude longitude bounds such as the points form a rectangle 47.5204,-122.2047,47.6139,-122.1065")
            lat1 = float(input("Enter the latitude start bond: "))
            lat2 = float(input("Enter the latitude end bond: "))
            lon1 = float(input("Enter the longitude start bond: "))
            lon2 = float(input("Enter the longitude end bond: "))
            ext = [lat1,lon1,lat2,lon2]
            # count = stations_rect(ext)
            # print(f"There are {count} number of stations within these bounds")
            try:
                count = stations_rect(ext)
                print(f"There are {count} number of stations within these bounds")
            except:
                print("Error!!! Please make sure the values form a rectangle, Thank you!")

        elif c == 2:
            city_n = input("Enter your city name: ")
            city_code = input("Enter your country name, if country is US(United States) please enter your state and country name together with a space: ")
            date = input("Enter the date in iso format(yyyy-mm-dd): ")
            #temp_city(city_n,city_code,date)
            try:
                temp_city(city_n, city_code, date)
            except:
                print("--------ERROR------------")
                print("Please Enter the city name with Starting Letter in CAPS-- example - Houston\n"
                      "Please Enter the country code properly and all letters in CAPS. If the city is in US enter the state name too-- example- TX US\n"
                      "Please Enter the date in iso format only -- (yyyy-mm-dd)")
        elif c ==3:
            zipc = input("Enter the zip code: ")
            date = input("Enter the date in iso format(yyyy-mm-dd): ")
            #Weather_report_zip(zipc,date)
            try:
                Weather_report_zip(zipc,date)
            except:
                print("--------ERROR------------")
                print("Please Enter a Valid zip code\n"
                      "Please Enter the date in iso format only -- (yyyy-mm-dd)")
        elif c==4:
            zipc = input("Enter the zip code: ")
            date = input("Enter the date in iso format(yyyy-mm-dd): ")
            all_stations(zipc,date)
            # try:
            #     all_reports(zipc,date)
            # except:
            #     print("--------ERROR------------")
            #     print("Please Enter a Valid zip code\n"
            #           "Please Enter the date in iso format only -- (yyyy-mm-dd)")
        elif c==5:
            sys.exit()

main()
#Zanesville
#OH US




#
# burl = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&stationid=COOP:010008&units=metric&startdate=2010-05-01&enddate=2010-05-31"
# res = requests.get(burl,headers={"token": token})
# res_j = res.json()
# print(res_j)