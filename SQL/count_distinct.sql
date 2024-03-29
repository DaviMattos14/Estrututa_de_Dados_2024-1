SELECT
  warehouse.state AS state,
  COUNT ( DISTINCT order_id) as num_order
FROM
  `warehouse_orders.Orders` AS orders
JOIN
  `warehouse_orders.Warehouse` AS warehouse 
  ON
  orders.warehouse_id = warehouse.warehouse_id
GROUP BY
  warehouse.state