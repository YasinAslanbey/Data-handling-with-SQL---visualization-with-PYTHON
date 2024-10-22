SET SQL_SAFE_UPDATES = 0;

UPDATE test2.transporation2
SET VIP = 'False'
WHERE VIP IS NULL;


UPDATE test2.transporation2
SET Transported = 'False'
WHERE Transported IS NULL;


UPDATE test2.transporation2
SET HomePlanet = 'Other'
WHERE HomePlanet IS NULL;


SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
SELECT 
    Destination, 
    COUNT(*) AS TotalPassengers, 
    SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) AS TransportedCount,
    (SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS Transported_Percentage_destination
FROM test2.transporation2
GROUP BY Destination
ORDER BY Transported_Percentage_destination;


SELECT
    VIP,
    COUNT(*) AS TotalVIP,
    SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) AS TRANSPORTED_VIP,
    (SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS Transported_Percentage_VIP
FROM test2.transporation2
GROUP BY VIP
ORDER BY Transported_Percentage_VIP;

SELECT
    Age,
    COUNT(*) AS person_count,
    SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) AS Transported_a,
    (SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS Transported_Percentage_per_age
FROM test2.transporation2 
GROUP BY Age
ORDER BY Transported_Percentage_per_age DESC;


SELECT
    HomePlanet,
    COUNT(*) AS People_count,
    SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) AS Transported_person,
    (SUM(CASE WHEN Transported = 'True' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS Transported_Percentage_homeplanet
FROM test2.transporation2
GROUP BY HomePlanet
ORDER BY Transported_Percentage_homeplanet;


SET SQL_SAFE_UPDATES = 1;

SELECT COUNT(*) FROM test2.transporation2 WHERE Transported = 'True';




