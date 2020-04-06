#!/usr/bin/python3

# This program models the growth of infected people by producing a stdout
# that can be ploted in gnuplot. 

# This program is based on the work of Ross Beckley, Cametria Weatherspoon,
# Michael Alexander, Marissa Chandler, Anthony Johnson, and Ghan S Bhatt in 
# their paper "Modeling epidemics with differential equations". 
# http://www.tnstate.edu/mathematics/mathreu/filesreu/GroupProjectSIR.pdf

# Metrics from these pages
# Growth factor of 7% per day from 
# https://www.worldometers.info/coronavirus/coronavirus-cases/
# beta (recovery rate) extrapolated by ratio of recoveries vs. new cases
alpha = 0.0000000007 # per person per person per day
beta = 0.02 # per person per day


# US Population on 4/4/20 was 329,472,392 from https://www.census.gov/popclock/


# Initial conditions on 4/4/20
# Infected people
I = 336673.0
# Recovered people
R = 17977.0
# Susceptible people 
S = 329472392.0 - I - R

# Time scale shall be days
dT = 1.0
T = 0

print("# T S I R")
print("" + str(T) + " " + str(S) + " " + str(I) + " " + str(R))
while I > 1000:
    
    dS = -1*alpha*S*I*dT
    dI = (alpha*S*I - beta*I)*dT
    dR = beta*I*dT

    S += dS
    I += dI
    R += dR

    T += 1
    print("" + str(T) + " " + str(S) + " " + str(I) + " " + str(R))

