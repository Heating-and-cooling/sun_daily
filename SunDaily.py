# -*- coding: utf-8 -*-
# SunDaily
# Version 2021_11_01_S.py
# Calculation of sun position and solar radiation on horizontal and vertical surfaces for a given day and hour
# By Sirri AYDINLI, Engin BAGDA, Erkam Talha ÖZTÜRK

# Based on Global Horizontal Irradiance Clear Sky Models: Implementation and Analysis
# Mathew J. Reno, Clifford W. Hansen, Joshua S.Stein, SAND 2012-2389, March 2012
# DIN 5034-2:2019-12 Daylight in interiors - Part 2: Principles

import math

GUSEV = {
           0: {0: 176, 1: 170, 2: 135, 3: 101, 4: 74, 5: 53, 6: 38},
           1: {0: 171, 1: 166, 2: 132, 3: 99,  4: 73, 5: 53, 6: 38},
           2: {0: 158, 1: 153, 2: 122, 3: 92,  4: 69, 5: 51, 6: 38},
           3: {0: 138, 1: 132, 2: 106, 3: 82,  4: 63, 5: 49, 6: 38},
           4: {0: 114, 1: 108, 2: 88,  3: 70,  4: 56, 5: 46, 6: 38},
           5: {0: 89,  1: 82,  2: 68,  3: 57,  4: 49, 5: 43, 6: 38},
           6: {0: 68,  1: 60,  2: 52,  3: 46,  4: 42, 5: 40, 6: 38},
           7: {0: 55,  1: 47,  2: 41,  3: 38,  4: 37, 5: 37, 6: 38},
           8: {0: 49,  1: 40,  2: 35,  3: 33,  4: 33, 5: 35, 6: 38},
           9: {0: 47,  1: 37,  2: 32,  3: 30,  4: 30, 5: 33, 6: 38},
          10: {0: 46,  1: 36,  2: 31,  3: 28,  4: 29, 5: 32, 6: 38},
          11: {0: 46,  1: 36,  2: 30,  3: 28,  4: 28, 5: 31, 6: 38},
          12: {0: 46,  1: 36,  2: 30,  3: 27,  4: 28, 5: 31, 6: 38}
}

day = int(input("Number of day (from 1 to 365): "))
if day > 365:
    print ("Day number > 365 in a  year is not possible")
    exit()

print("To calculate the local time. Time zone for Germany at wintertime: 1 and for summertime: 2")
Time_zone = int(input("Time zone: "))
if Time_zone > abs(12):
    print ("Time zone number > 12 is  not possible.")
    exit()

Surface_Azimuth_deg = float(input("Surface azimuth in degrees (east 90°, south 180°, west 270°, North 360°): "))
Surface_Azimuth_rad = math.radians(Surface_Azimuth_deg)
if Surface_Azimuth_deg > 360:
    print ("Surface azimuth > 360 is  not possible.")
    exit()

Surface_Tilt_rad = math.pi/2 # Vertical surface: pi/2, Horizontal surface: zero

Latitude_deg = float(input("Latitude in degrees: "))
Latitude_rad = math.radians(Latitude_deg)
if Latitude_deg > 90:
    print ("Code for Latitude > 90° is not appropriate.")
    exit()

Longitude_deg = float(input("Longitude in degrees: "))
Longitude_rad = math.radians(Longitude_deg)
if Longitude_deg > 180:
    print ("Code for Longitude > 180° is not appropriate.")
    exit()

Height = int(input("Height from sea level in m: "))
if Height  > 8000:
    print("Code for height > 8000 m is not appropriate.")
    exit()

# mn = 0 # always set hour:00:00

Horizontal_global_sum = Surface_total_sum = 0

if day <=31: TF = 3.7 # January
if day >31 and day <= 59 : TF = 4.1 # February
if day >59 and day <= 90 : TF = 4.6 # March
if day >90 and day <= 120 : TF = 5.1 # April
if day >120 and day <= 151 : TF = 5.3 # May
if day >151 and day <= 181 : TF = 6.1 # June
if day >181 and day <= 212 : TF = 6.1 # July
if day >212 and day <= 243 : TF = 5.9 # August
if day >243 and day <= 273 : TF = 5.4 # September23
if day >273 and day <= 304 : TF = 4.2 # October
if day >304 and day <= 334 : TF = 3.6 # November
if day >334 and day <= 365 : TF = 3.5 # December

print("Proposed turbidity factor acc. to Linke: %3.1f"% (TF))
TF = float(input("Turbidity factor acc. to Linke: "))

# Solar constant in W/m2 Median 1367.7 W/m2, according to Reno, Hansen, Stein equation 11
SC = 1367.7 * (1 + 0.033 * math.cos(math.pi * 2 * day / 365))

print ("Solar constant : %4.0f"% (SC))
print ("Surface tilt angle : %2.0f"% (math.degrees(Surface_Tilt_rad)))
print()
print("                               Degrees                       Irradiation in W/m2                      ")
print("   Local time  True time   Zenith   Azimuth    Normal   Horizontal  Horizontal  Horizontal   Surface     R_Sky")
print("                                               Direct    Direct       Sky         Global      Total    ")

for hour in range (3, 23, 1): # in local true time respective solar time

# according to Reno, Hansen, Stein equation 6 to slice the year in radians/day, calculation start at 00:00
    fy_rad = (2 * math.pi / 365) * (day - 1)

# Declination according to Spancer, Reno, Hansen, Stein  equation 5 in Radiant
    Declination_rad = 0.006918 - 0.399912 * math.cos(fy_rad) + 0.070257 * math.sin(fy_rad) - 0.006758 * math.cos(
        2 * fy_rad) + 0.000907 * math.sin(2 * fy_rad) - 0.002697 * math.cos(3 * fy_rad) + 0.00148 * math.sin(3 * fy_rad)

# Hour_angle, according to Reno, Hansen, Stein equation 9
# earth rotation 15 degrees per hour

    Hour_Angle_deg = (hour - 12) * 15
    Hour_Angle_rad = math.radians(Hour_Angle_deg)

# Zenith Angle of sun, at zenith ZA=0, at horizon ZA = 90°, according to Reno, Hansen, Stein equation 10

    Cos_Zenith_rad = math.sin(Latitude_rad) * math.sin(Declination_rad) + math.cos(Latitude_rad) * math.cos(Declination_rad) * math.cos(Hour_Angle_rad)

    Zenith_rad = math.acos(Cos_Zenith_rad)

    Elevation_deg = 90 - math.degrees(Zenith_rad)

# Azimut angle of sun according to DIN 5034-2:1985 equation 10, 11 and 12

    Cos_Azimuth_rad = ((math.cos(Zenith_rad)*math.sin(Latitude_rad))
                         - math.sin(Declination_rad)) / (math.cos(Latitude_rad)*math.sin(Zenith_rad))

    if Hour_Angle_rad == 0:
        Azimuth_deg = 180

    if Hour_Angle_rad > 0:
        Azimuth_deg = 180 + math.degrees(math.acos(Cos_Azimuth_rad))

    if Hour_Angle_rad < 0:

        Azimuth_deg = 180 - math.degrees(math.acos(Cos_Azimuth_rad))

    Azimuth_rad = math.radians(Azimuth_deg)

# Air mass

    Air_mass = 1/(0.9 + 9.4 * math.sin(math.radians(Elevation_deg)))

# Absorption by transmission trough atmosphere

    if math.degrees(Zenith_rad) < 90: # after Zenith angle=90 is sun set
        TaM = 1.294 + 2.4417 * 10 ** -2 * Elevation_deg - 3.973 * 10 ** -4 * Elevation_deg ** 2
        TaM = TaM + 3.8034 * 10 ** -6 * Elevation_deg ** 3 - 2.2145 * 10 ** -8 * Elevation_deg ** 4
        TaM = (TaM + 5.8832 * 10 ** -11 * Elevation_deg ** 5) * (0.506 - 1.0788 * 10 ** -2 * TF)

# Direct normal irradiance (Bestrahlungsstaerke auf Flächennormale, gerichtet zur Sonne)

        Normal_direct = SC * math.exp(-TF * Air_mass * math.exp(-Height/8000))

# Direct horizontal irradiance (Horizontale Bestrahlungsstärke durch Sonne)

        Horizontal_direct = Normal_direct * math.cos(Zenith_rad)

 # Horizontal irradiance from sky (Horizontale Bestrahlungsstaerke durch den klaren Himmel)

        Horizontal_sky = 0.5 * SC * (math.sin(math.radians(Elevation_deg)))  * (TaM - math.exp(-TF * Air_mass *  math.exp(-Height/8000)))

# Global horizontal irradiance (Horizontale Globalbestrahlungsstaerke)

        Horizontal_global = Horizontal_direct + Horizontal_sky

        Horizontal_global_sum = Horizontal_global_sum + Horizontal_global

# Incidence Angle IA , angle between direction of sun radiation and surface normal in Radiant

        IA_rad = math.cos(Zenith_rad) * math.cos(Surface_Tilt_rad)
        IA_rad = IA_rad + math.sin(Surface_Tilt_rad) * math.sin(Zenith_rad) * math.cos(
                abs(Azimuth_rad - Surface_Azimuth_rad))

        if IA_rad > 1: IA_rad = 1
        if IA_rad < 0: IA_rad = 0

        IA_rad = math.acos(IA_rad)  # because IA is cos(IA) = cos(zenith)*cos (Surf TA) + ....

# Direct irradiance on surface
        Surface_direct = Normal_direct * math.cos(IA_rad)

# Calculation the R-Value according to GUSEV for a vertical surface for  diffuse irradiation from clear sky

        I1 = math.floor((Elevation_deg) / 15)
        I2 = I1 + 1
        if I2 > 6: I1 = I2 = 6
        Elev_diff = Elevation_deg - I1 * 15

        J1 = math.floor(abs((math.degrees((Azimuth_rad - Surface_Azimuth_rad)) / 15)))
        J2 = J1 + 1
        if J2 > 12: J1 = J2 = 12
        Alf_diff = abs(math.degrees(Azimuth_rad - Surface_Azimuth_rad)) - J1 * 15

        Alf_diff = abs(math.degrees(Azimuth_rad - Surface_Azimuth_rad)) - J1 * 15

        R11 = GUSEV[J1][I1]  # [AziDiff1] [Elev1]
        R12 = GUSEV[J1][I2]  # [AziDiff1] [Elev2]
        R21 = GUSEV[J2][I1]  # [AziDiff2] [Elev1]
        R22 = GUSEV[J2][I2]  # [AziDiff2] [Elev2]

        R110 = (R11 - R12) / 15  # [AziDiff1] [Elev1] - [AziDiff1] [Elev2]
        R220 = (R21 - R22) / 15  # # [AziDiff2] [Elev1] - [AziDiff1] [Elev2]

        R01 = R11 - R110 * Elev_diff
        R02 = R21 - R220 * Elev_diff

        R0012 = (R02 - R01) / 15

        R_sky = (R01 + R0012 * Alf_diff) / 100  # irradiance on a vertical surface related to horizontal irradiance by clear sky only

# Sky irradiance
        Surface_sky = Horizontal_sky * R_sky

# Reflection from ground
        Reflection_ground = 0.2
        Surface_reflec = Horizontal_global * 0.5 * Reflection_ground * (1 - math.cos(Surface_Tilt_rad))

# Diffuse irradiance
        Surface_diffuse = Surface_reflec + Surface_sky

# Total irradiance on surface
        Surface_total = Surface_direct + Surface_diffuse

        Surface_total_sum += Surface_total

# Calculation Local time
# Equation of Time (EoT) # According to Reno, Hansen, Stein equation 8

        x = (2 * math.pi / 365) * ((day - 81))
        EoT = 9.87 * math.sin(2 * x) - 7.53 * math.cos(x) - 1.5 * math.sin(x)

        Time_offset = ((Time_zone * 15 - Longitude_deg) / 15) * 60 + EoT # in Minutes

        Local_time = (hour * 60 + Time_offset) / 60

        Local_Hour = int(Local_time)
        Local_Minute = (Local_time - Local_Hour) * 60

        if Local_Minute > 59.5:
            Local_Hour = hour + 1

            Local_Minute = 00

        if hour == 12: print()
        print("%6.0f %2.0f %8.0f  %10.0f  %8.0f    %8.0f  %8.0f   %8.0f   %10.0f   %8.0f     %8.2f" % (Local_Hour, Local_Minute, hour, math.degrees(Zenith_rad), math.degrees(Azimuth_rad), Normal_direct, Horizontal_direct, Horizontal_sky, Horizontal_global,  Surface_total, R_sky))
        if hour == 12: print()

print()
print("Global horizontal irradiance = %8.2f" % (Horizontal_global_sum/1000), "kWh/m2/day")
print("Total irradiance to surface  = %8.2f" % (Surface_total_sum/1000), "kWh/m2/day")
