SELECT 
    invoice_number,
    invoice_date,
    invoice_total - (payment_total + credit_total) AS balance_due,
    payment_date
FROM Invoices
WHERE payment_date IS NULL;