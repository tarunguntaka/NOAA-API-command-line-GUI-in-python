# NOAA-API-command-line-GUI-in-python


# Project Description
The deliverable for this project will be a piece of software that fetches data from a web API and allows
a user to interact with it using the command line or a GUI (a command line will likely be easier).

# STEPS to run 

- STEP-1: RUN THE MAIN.PY
- STEP-2 : YOU CAN SEE 4 TYPES OF FUNCTIONS AVAILABLE
Enter 1 for Command line utility that will count the number of stations in a given lat-lon rectangle
Enter 2 for Command line utility that can fetch temperature data or data belongs to TEMP dataset for a given city on a given date
Enter 3 to Give a weather report(Daily Summaries) for a given area(Zip code) on a specified day
Enter 4 to Fetch all stations for a given area(ZIP CODE) on a specified day
Enter 5 to exit the program

- STEP-3: ENTER YOUR CHOICE

IF YOUR CHOICE IS 1:
    ENTER THE LATITUDE START BOND OR LOWER BOUND-
    ENTER THE LATITUDE END BOUND OR UPPER BOUND-
    ENTER THE LONGITUDE START BOUND OR LOWER BOUND-
    ENTER THE LONGITUDE END BOUND OR UPPER BOUND-

THE RESULT IS THE NUMBER OF STATIONS IN THE REGION FORMED BY THE BOUNDS AND MAKE SURE IT FORMS A RECTANGLE
MAKE SURE THE BOUND ARE VALID AND ARE SUPPORTED

IF YOUR CHOICE IS 2:
    ENTER THE CITY NAME- EXAMPLE - Houston(FIRST LETTER SHOULD BE IN CAPS)
    Enter your country name, if country is US(United States) please enter your state and country name together with a space: - EXAMPLE - 'AE' OR IF CITY IS IN US, EXAMPLE- 'TX US' (ALL LETTERS IN CAPS)
    Enter the date in iso format(yyyy-mm-dd):

THE RESULT IS THE CORRESPONDING STATION NAMES, DATE, DATATYPES RELATED TO TEMP DATASET AND THEIR VALUES
THIS FUNCTION WORKS FIRST BY FINDING THE CITIES WHICH SUPPORT TEMP DATASET ON THAT DAY
NEXT THE CITY NAMES ARE LINKED TO THEIR CITYID AND STORED IN A DICTIONARY
THIS DICTIONARY IS USED TO GRAB CITYID FOR PROCESSING THE TEMPERATURE DATASET RESULTS

IF YOUR CHOICE IS 3:
    ENTER THE ZIP CODE- EXAMPLE-28801(VALID ZIP CODE)
    ENTER THE DATE-(VALID ISO DATE)

THE RESULT IS THE CORRESPONDING STATION NAMES ALONG WITH CORRESPONDING DATATYPES AND THEIR VALUES
THIS FUNCTION WORKS DIRECTLY BY TAKING THE ZIP CODE AND DATE AND RETURNS THE ABOVE RESULTS

IF YOUR CHOICE IS 4:
    ENTER THE ZIP CODE
    ENTER THE DATE IN ISO FORMAT

THE RESULT IS THE NO OF STATIONS IN THAT PARTICULAR REGION(ZIP CODE) AND THEIR CORRESPONDING NAMES
THIS FUNCTION WORKS DIRECTLY BY TAKING THE ZIP CODE AND DATE AND RETURNS THE ABOVE RESULTS.

IF YOUR CHOICE IS 5:

EXITS THE PROGRAM
