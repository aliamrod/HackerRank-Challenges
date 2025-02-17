/*
Query the Western Longitude (LONG_W) for the largest Northen Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.
*/

select round(long_w, 4)
from station 
where lat_n < 137.2345

order by lat_n desc
limit 1; 
