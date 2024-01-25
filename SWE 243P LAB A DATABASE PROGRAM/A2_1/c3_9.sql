SELECT CONCAT(vendor_contact_last_name, ', ', vendor_contact_first_name) AS full_name
FROM Vendors
WHERE vendor_contact_last_name LIKE 'A%' 
   OR vendor_contact_last_name LIKE 'B%' 
   OR vendor_contact_last_name LIKE 'C%' 
   OR vendor_contact_last_name LIKE 'E%'
ORDER BY vendor_contact_last_name ASC, vendor_contact_first_name ASC;