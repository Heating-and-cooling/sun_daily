# Dynamic temperature calculation on surfaces in solar radiance and radiation exchange with environment 

Engin Bagda, Manfred Hermann, Erkam Talha Öztürk
Heat flow through walls depends on the surface temperature between the inside and the outside. If the surface
temperatures change the heat flow gets dynamic. In this work is a calculation method explained and a code
“Surface_temp.py” given to determine the surface temperature of materials at changing solar radiation and air
temperature. It is shown how the surface temperature depends beside the intensity of the solar radiation and the air
temperature to the solar absorptions coefficient of the surface, thermal conductivity of the material and the emission
coefficients of surface and environment.

The code “Surface_temp_2021_03_11.py” calculate in a good approximation the surface temperature of a material in
dependence on the sun radiation and air temperature. This is shown by using the measurements in the excel sheet
“Garden_2021_03_08.xlsx”.

The code Surface_temp.py use for the calculation of the dynamic heat flow through walls the numerical Crank-Nicolson
method as explained in erkam-o/DynamicHeatFlow .
