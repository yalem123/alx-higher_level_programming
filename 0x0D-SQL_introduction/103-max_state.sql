-- print import in hbtn_0c_0 database
-- query of Import in hbtn_0c_0 database
SELECT state, MAX(value) as max_temp FROM temperatures
           GROUP BY state
	   ORDER BY state
	   limit 3;
