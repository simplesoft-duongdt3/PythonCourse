
-- select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City from employees AS e

 -- select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City , e.address
 -- from employees AS e
 -- ORDER BY e.Address DESC
 
-- select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City , e.address
-- from employees AS e
-- WHERE E.EmployeeId=5
 
--select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City , e.address
--from employees AS e
--WHERE e.LastName LIKE '%a%'

--select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City , e.address
--from employees AS e
--WHERE e.LastName LIKE '%e%' OR e.LastName LIKE '%A%'

--select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City , e.address
--from employees AS e
--WHERE e.LastName LIKE '%e%' AND e.LastName LIKE '%A%'

select e.EmployeeId,e.LastName,e.FirstName,e.Title ,e.City , e.address
from employees AS e
WHERE e.EmployeeId >5
