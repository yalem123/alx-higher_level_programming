-- prints script that displays the average temperature (Fahrenheit)
-- query of script that displays the average temperature (Fahrenheit)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
