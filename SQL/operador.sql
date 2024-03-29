SELECT
  Date,
  region,
  Small_Bags,
  Total_Bags,
  (Small_Bags / Total_Bags)*100 AS small_bags_percent
FROM
 `avocado_prices.avocado_data`
WHERE
  Small_Bags <> 0 