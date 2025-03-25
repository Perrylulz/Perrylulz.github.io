import calendar
cal=calendar.Calendar()

#https://docs.python.org/3/library/calendar.html

#DATES
##################################################################################################################

ariesSeason = [ "3.21.07", "3.22.07", "3.23.07", "3.24.07", "3.25.07", "3.26.07", "3.27.07", "3.28.07", "3.29.07", "3.30.07", "3.31.07", "4.1.07", "4.2.07", "4.3.07", "4.4.07", "4.5.07", "4.6.07", "4.7.07", "4.8.07", "4.9.07", "4.10.07", "4.11.07", "4.12.07", "4.13.07", "4.14.07", "4.15.07", "4.16.07", "4.17.07", "4.18.07", "4.19.07",

"3.20.08", "3.21.08", "3.22.08", "3.23.08", "3.24.08", "3.25.08", "3.26.08", "3.27.08", "3.28.08", "3.29.08", "3.30.08", "3.31.08", "4.1.08", "4.2.08", "4.3.08", "4.4.08", "4.5.08", "4.6.08", "4.7.08", "4.8.08", "4.9.08", "4.10.08", "4.11.08", "4.12.08", "4.13.08", "4.14.08", "4.15.08", "4.16.08", "4.17.08", "4.18.08",

"3.20.09", "3.21.09", "3.22.09", "3.23.09", "3.24.09", "3.25.09", "3.26.09", "3.27.09", "3.28.09", "3.29.09", "3.30.09", "3.31.09", "4.1.09", "4.2.09", "4.3.09", "4.4.09", "4.5.09", "4.6.09", "4.7.09", "4.8.09", "4.9.09", "4.10.09", "4.11.09", "4.12.09", "4.13.09", "4.14.09", "4.15.09", "4.16.09", "4.17.09", "4.18.09", "4.19.09"
]

ariesDecan1 = ["3.21.07", "3.22.07", "3.23.07", "3.24.07", "3.25.07", "3.26.07", "3.27.07", "3.28.07", "3.29.07", "3.30.07", 
"3.20.08", "3.21.08", "3.22.08", "3.23.08", "3.24.08", "3.25.08", "3.26.08", "3.27.08", "3.28.08", "3.29.08", 
"3.20.09", "3.21.09", "3.22.09", "3.23.09", "3.24.09", "3.25.09", "3.26.09", "3.27.09", "3.28.09", "3.29.09"]

ariesDecan2 = ["3.31.07", "4.1.07", "4.2.07", "4.3.07", "4.4.07", "4.5.07", "4.6.07", "4.7.07", "4.8.07", "4.9.07", 
"3.30.08", "3.31.08", "4.1.08", "4.2.08", "4.3.08", "4.4.08", "4.5.08", "4.6.08", "4.7.08", "4.8.08",
"3.30.09", "3.31.09", "4.1.09", "4.2.09", "4.3.09", "4.4.09", "4.5.09", "4.6.09", "4.7.09", "4.8.09"]

ariesDecan3 = ["4.10.07", "4.11.07", "4.12.07", "4.13.07", "4.14.07", "4.15.07", "4.16.07", "4.17.07", "4.18.07", "4.19.07", 
"4.9.08", "4.10.08", "4.11.08", "4.12.08", "4.13.08", "4.14.08", "4.15.08", "4.16.08", "4.17.08", "4.18.08", 
"4.9.09", "4.10.09", "4.11.09", "4.12.09", "4.13.09", "4.14.09", "4.15.09", "4.16.09", "4.17.09", "4.18.09", "4.19.09"]

##################################################################################################################

taurusSeason = [ "4.20.07", "4.21.07", "4.22.07", "4.23.07", "4.24.07", "4.25.07", "4.26.07", "4.27.07", "4.28.07", "4.29.07", "4.30.07", "5.1.07", "5.2.07", "5.3.07", "5.4.07", "5.5.07", "5.6.07", "5.7.07", "5.8.07", "5.9.07", "5.10.07", "5.11.07", "5.12.07", "5.13.07", "5.14.07", "5.15.07", "5.16.07", "5.17.07", "5.18.07", "5.19.07", "5.20.07",

"4.19.08", "4.20.08", "4.21.08", "4.22.08", "4.23.08", "4.24.08", "4.25.08", "4.26.08", "4.27.08", "4.28.08", "4.29.08", "4.30.08", "5.1.08", "5.2.08", "5.3.08", "5.4.08", "5.5.08", "5.6.08", "5.7.08", "5.8.08", "5.9.08", "5.10.08", "5.11.08", "5.12.08", "5.13.08", "5.14.08", "5.15.08", "5.16.08", "5.17.08", "5.18.08", "5.19.08",

"4.20.09", "4.21.09", "4.22.09", "4.23.09", "4.24.09", "4.25.09", "4.26.09", "4.27.09", "4.28.09", "4.29.09", "4.30.09", "5.1.09", "5.2.09", "5.3.09", "5.4.09", "5.5.09", "5.6.09", "5.7.09", "5.8.09", "5.9.09", "5.10.09", "5.11.09", "5.12.09", "5.13.09", "5.14.09", "5.15.09", "5.16.09", "5.17.09", "5.18.09", "5.19.09", "5.20.09",
]

taurusDecan1 = [
"4.20.07", "4.21.07", "4.22.07", "4.23.07", "4.24.07", "4.25.07", "4.26.07", "4.27.07", "4.28.07", "4.29.07",

"4.19.08", "4.20.08", "4.21.08", "4.22.08", "4.23.08", "4.24.08", "4.25.08", "4.26.08", "4.27.08", "4.28.08",

"4.20.09", "4.21.09", "4.22.09", "4.23.09", "4.24.09", "4.25.09", "4.26.09", "4.27.09", "4.28.09", "4.29.09"
]

taurusDecan2 = [
"4.30.07", "5.1.07", "5.2.07", "5.3.07", "5.4.07", "5.5.07", "5.6.07", "5.7.07", "5.8.07", "5.9.07",

"4.29.08", "4.30.08", "5.1.08", "5.2.08", "5.3.08", "5.4.08", "5.5.08", "5.6.08", "5.7.08", "5.8.08",

"4.30.09", "5.1.09", "5.2.09", "5.3.09", "5.4.09", "5.5.09", "5.6.09", "5.7.09", "5.8.09", "5.9.09"
]


taurusDecan3 = [
"5.10.07", "5.11.07", "5.12.07", "5.13.07", "5.14.07", "5.15.07", "5.16.07", "5.17.07", "5.18.07", "5.19.07", "5.20.07",

"5.9.08", "5.10.08", "5.11.08", "5.12.08", "5.13.08", "5.14.08", "5.15.08", "5.16.08", "5.17.08", "5.18.08", "5.19.08",

"5.10.09", "5.11.09", "5.12.09", "5.13.09", "5.14.09", "5.15.09", "5.16.09", "5.17.09", "5.18.09", "5.19.09", "5.20.09"
]

#################################################################################################################

#Gemini (may 21 09, may 20 08, may 21 07)
#Cancer (jun 21 09, jun 21 08, jun 21 07)
#Leo ( jul 22 09, jul 22 08, jul 23 007)
#Virgo (aug 23 09, aug 22 08, aug 23 07)
#libra (sep 23 09, sep 22 08, sep 23 07)
#scoprio (oct 23 09, oct 23 08, oct 23 07)


# geminiSeason = [ "4.20.07", "4.21.07", "4.22.07", "4.23.07", "4.24.07", "4.25.07", "4.26.07", "4.27.07", "4.28.07", "4.29.07", "4.30.07", "4.31.07", "5.1.07", "5.2.07", "5.3.07", "5.4.07", "5.5.07", "5.6.07", "5.7.07", "5.8.07", "5.9.07", "5.10.07", "5.11.07", "5.12.07", "5.13.07", "5.14.07", "5.15.07", "5.16.07", "5.17.07", "5.18.07", "5.19.07", "5.20.07",

# "4.19.08", "4.20.08", "4.21.08", "4.22.08", "4.23.08", "4.24.08", "4.25.08", "4.26.08", "4.27.08", "4.28.08", "4.29.08", "4.30.08", "4.31.08", "5.1.08", "5.2.08", "5.3.08", "5.4.08", "5.5.08", "5.6.08", "5.7.08", "5.8.08", "5.9.08", "5.10.08", "5.11.08", "5.12.08", "5.13.08", "5.14.08", "5.15.08", "5.16.08", "5.17.08", "5.18.08", "5.19.08",

# "4.20.09", "4.21.09", "4.22.09", "4.23.09", "4.24.09", "4.25.09", "4.26.09", "4.27.09", "4.28.09", "4.29.09", "4.30.09", "4.31.09", "5.1.09", "5.2.09", "5.3.09", "5.4.09", "5.5.09", "5.6.09", "5.7.09", "5.8.09", "5.9.09", "5.10.09", "5.11.09", "5.12.09", "5.13.09", "5.14.09", "5.15.09", "5.16.09", "5.17.09", "5.18.09", "5.19.09", "5.20.09"
# ]

# geminiDecan1 = [

# ]

# geminiDecan2 = [

# ]


# geminiDecan3 = [

# ]

#################################################################################################################

print("")
print(f"Input your date of birth as so: month.day.year // Example, January 13th, 2008 -> 1.13.08")
print("")
date=str(input())

#INTERPRETATIONS
#taurus chaldean rulership =  mercury moon saturn
#gemini chaldean = jupiter mars sun
#cancer = venus mercury moon
#leo = saturn jupiter mars
# virgo = Sun Venus mercury
#Libra = moon saturn jupiter
#Scorpio= mars sun venus
#sagittarius = mercury moon saturn
#capricorn = jupiter mars sun
#aquarius venus mercury moon
#pisces = saturn jupiter mars

##################################################################################################################

if (date in ariesSeason):
    print(f"  ")
    print("\x1B[4m" + "ARIES SUN" + "\x1B[0m")
    print(f"Aries is an active, energetic sign. People with Sun in Aries are direct, straightforward, and uncomplicated. They expect the same from others and are baffled when they don’t always get it.")    
    
#1st decan
if(date in ariesDecan1):
    print(f"  ")
    print("\x1B[4m" + "DECAN 1:" + "\x1B[0m")
    print(f"  ")
    print(f"CHALDEAN: Mars")
    print(f"TRIPLICITY: Aries")
    print(f"  ")
    print(f"These people are bold, blunt, and brash. These natives are generally known to be quick to anger. They love a good fight (or at least a debate). However, they are also able to forgive and cool off just as quickly")


    #2nd decan
elif(date in ariesDecan2):
    print(f"  ")
    print("\x1B[4m" + "DECAN 2:" + "\x1B[0m")
    print(f"  ")
    print(f"CHALDEAN: Sun")
    print(f"TRIPLICITY: Leo")
    print(f"  ")
    print(f"You are fortunate to be born in this decan as the sun empowers you with constructive and creative abilities. These qualities steer your life abruptly. You would be ambitious, kind-hearted, idealistic, industrious and a born leader.")


    #3rd decan
elif (date in ariesDecan3): 
    print(f"  ")
    print("\x1B[4m" + "DECAN 3:" + "\x1B[0m")
    print(f"  ")
    print(f"CHALDEAN: Venus")
    print(f"TRIPLICITY: Sagittarius")
    print(f"  ")
    print(f"Placements here will be concerned with unification through harmony, rather than brute force. There's still drive and ambition seen here, but it's tempered with the awareness that you catch more flies with honey. Don't let all this Venusian softness fool you though, as hell hath no fury like a woman scorned. This placement can still bring out the brash side of Aries, but it will do so in a more cunning, subtle way. ")


#####################################################################################

if (date in taurusSeason):
    print(f"  ")
    print("\x1B[4m" + "TAURUS SUN"+ "\x1B[0m")
    print(f"Taurus Sun interpretation")    
    
#1st decan
if(date in taurusDecan1):
    print(f"  ")
    print("\x1B[4m" + "DECAN 1:" + "\x1B[0m")
    print(f"  ")
    print(f"CHALDEAN: Mercury")
    print(f"TRIPLICITY: Taurus")
    print(f"  ")
    print(f"Taurus Decan 1 interpretation")


    #2nd decan
elif(date in taurusDecan2):
    print(f"  ")
    print("\x1B[4m" + "DECAN 2:" + "\x1B[0m")
    print(f"  ")
    print(f"CHALDEAN: Moon")
    print(f"TRIPLICITY: Virgo")
    print(f"  ")
    print(f"Taurus Decan 2 interpretation")


    #3rd decan
elif (date in taurusDecan3): 
    print(f"  ")
    print("\x1B[4m" + "DECAN 3:" + "\x1B[0m")
    print(f"  ")
    print(f"CHALDEAN: Saturn")
    print(f"TRIPLICITY: Capricorn")
    print(f"  ")
    print(f"Taurus Decan 3 interpretation")

#####################################################################################

# if (date in geminiSeason):
#     print(f"  ")
#     print(f"Gemini Sun interpretation")    
    
# #1st decan
# if(date in geminiDecan1):
#     print(f"  ")
#     print(f"Gemini Decan 1 interpretation")
#     print(f"  ")

#     #2nd decan
# elif(date in geminiDecan2):
#     print(f"  ")
#     print(f"Gemini Decan 2 interpretation")
#     print(f"  ")


#     #3rd decan
# elif (date in geminiDecan3): 
#     print(f"  ")
#     print(f"Gemini Decan 3 interpretation")
#     print(f"  ")

#####################################################################################

# if (date in cancerSeason):
#     print(f"  ")
#     print(f"Cancer Sun interpretation")    
    
# #1st decan
# if(date in cancerDecan1):
#     print(f"  ")
#     print(f"Cancer Decan 1 interpretation")
#     print(f"  ")

#     #2nd decan
# elif(date in cancerDecan2):
#     print(f"  ")
#     print(f"Cancer Decan 2 interpretation")
#     print(f"  ")


#     #3rd decan
# elif (date in cancerDecan3): 
#     print(f"  ")
#     print(f"Cancer Decan 3 interpretation")
#     print(f"  ")

#####################################################################################

#2007 COnnjcutions (Sun/moon Conjunction in aries on april 17)
# (Sun/mercury conjunction on may 3-4-5 in taurus)(sun/moon conjunctions on may 17 in taurus)
# (sun/moon conjunction in gemini on june 15)(Sun/mercury conjunction in cancer june 29-29)

        #CONJUNCTIONS

moonConj_ARI = ["4.17.07"]
mercConj_TAU = ["5.3.07", "5.4.07", "5.5.07"]
moonConj_TAU =["5.17.07"]

if(date in moonConj_ARI):
    print(f"  ")
    print(f"Sun/Moon Conjunction in Aries interpretation.")
    print(f"  ")


if(date in mercConj_TAU):
    print(f"  ")
    print(f"Sun/Mercury Conjunction in Taurus interpretation.")
    print(f"  ")


if(date in moonConj_TAU):
    print(f"  ")
    print(f"Sun/Moon Conjunction in Taurus interpretation.")
    print(f"  ")
