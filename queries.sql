USE db

CREATE PROCEDURE sp_fire_incidents @district nvarchar(200) = NULL, @batallion nvarchar(200) = NULL, @incident_date1 nvarchar(100) = NULL,
@incident_date2 nvarchar(100) = NULL
AS

BEGIN

SELECT *
FROM fire_incidents
WHERE neighborhood_district = ISNULL(@district,neighborhood_district);

SELECT *
FROM fire_incidents
WHERE batallion = ISNULL(@batallion,batallion);

SELECT *
FROM fire_incidents
AND incident_date >= ISNULL(@incident_date, incident_date) AND < (@incident_date2, incident_date);

END

------------

EXEC sp_fire_incidents @district = '' 
GO

EXEC sp_fire_incidents @batallion = '' 
GO

EXEC dbo.uspGetAddress @incident_date1 = '', @incident_date2 = '' 
GO


