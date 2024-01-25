-- SELECT vendor_name, vendor_city, vendor_state
-- FROM vendors
-- WHERE CONCAT(vendor_state, vendor_city) NOT IN 
--     (SELECT CONCAT(vendor_state, vendor_city) as vendor_city_state
--      FROM vendors
--      GROUP BY vendor_city_state
--      HAVING COUNT(*) > 1)
-- ORDER BY vendor_state, vendor_city
SELECT v1.vendor_name, v1.vendor_city, v1.vendor_state
FROM vendors v1
LEFT JOIN (
    SELECT CONCAT(vendor_state, vendor_city) as vendor_city_state
    FROM vendors
    GROUP BY vendor_city_state
    HAVING COUNT(*) > 1
) v2 ON CONCAT(v1.vendor_state, v1.vendor_city) = v2.vendor_city_state
WHERE v2.vendor_city_state IS NULL
ORDER BY v1.vendor_state, v1.vendor_city;