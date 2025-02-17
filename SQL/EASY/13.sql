/*
Query the list of CITY names from STATION which have vowels (a,e,i,o,u) from as both their first and last characters. Your result cannot contain duplicates. 

Input Format:
The STATION table is described as follows:

      STATION
+-------------+--------------+
| Field       | Type         |
+-------------+--------------+
| ID          | NUMBER       |
| CITY        | VARCHAR2(21) |
| STATE       | VARCHAR2(2)  |
| LAT_N       | NUMBER       |
| LONG_W      | NUMBER       |
+-------------+--------------+

*/


SELECT DISTINCT CITY
FROM STATION 
WHERE LOWER(SUBSTR(CITY(1,1)) IN ('a', 'e', 'i', 'o', 'u') AND LOWER(SUBSTR(CITY,-1,1)) IN ('a', 'e', 'i', 'o', 'u'); 


/* 
Case 2
*/

SELECT DISTINCT CITY FROM STATION
      WHERE SUBSTR(CITY(1,1) REGEXP '[aeiouAEIOU]' AND CITY REGEX '[aeiou]$';
