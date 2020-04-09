#!/usr/bin/gnuplot 
set terminal pngcairo 
set output 'corona.png'
set title "Infection Plot" 
set xlabel "Time (days)"
set ylabel "People"
plot 'corona.dat' using 1:2 title "uninfected" with lines,\
     'corona.dat' using 1:3 title "infected" with lines,\
     'corona.dat' using 1:4 title "recovered" with lines

