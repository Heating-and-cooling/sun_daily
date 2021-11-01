# Calculation of solar radiation on horizontal and vertical surfaces under clear sky conditions
 
Sırrı Aydınlı, Engin Bagda, Erkam Talha Öztürk

For the impact of solar radiation on surfaces and the indoor climate of buildings, the knowledge of hourly solar
irradiance under clear sky conditions is of crucial importance. The hourly solar irradiance is also important for the
calculation of the power output of photovoltaic systems over the day. With the code SunDaily.py it is possible for a
given place, located by its longitude and latitude, to calculate for every day in the year the hourly direct and diffuse
solar irradiance on horizontal and vertical surfaces under clear sky conditions. The code is based to the paper
“Global Horizontal Irradiance Clear Sky Models: Implementation and Analysis”, by Matthew J. Reno, Clifford W. Hansen and
Joshua S. Stein

https://www.researchgate.net/publication/254994320_Global_horizontal_irradiance_clear_sky_models_implementation_and_analysisas

well as on DIN 5034-2 "Daylight in interiors-Part 2: Principles ".
For the calculation of diffuse irradiance, the R-values of Gusev, published in "CIE S 011/E: 2003/ISO15469:2004: Spatial
Distribution of Daylight- CIE Standard General Sky, Vienna" were used. R-value is the ratio of the irradiance on a
tilted surface to the horizontal irradiance by clear sky only.
The code uses the turbidity factors according to Linke suggested in DIN 5034-2 for clear sky conditions, but it is also
possible to calculate with other turbidity factors, depending on the requirements of the local atmospheric conditions at
the time.
