INSERT INTO users(
	user_id
	,user_email
	,user_name
	,user_lastname
	,user_password
	,created
	,updated
) VALUES (
	'1005944768'
	,'juanba@gmail.com'
	,'Juan'
	,'Ballesteros'
	,'hola'
	,NOW()
	,NOW()
)
,(
	'1005944763'
	,'camilo@gmail.com'
	,'Camilo'
	,'Ballesteros'
	,'hola'
	,NOW()
	,NOW()
);

INSERT INTO clients(
	client_id
) VALUES (
	'1005944768'
)
, (
	'1005944763'
);
INSERT INTO Categories(
	category_name
	,created
	,updated
) VALUES (
	'Ropa'
	,NOW()
	,NOW()
),
(
	'Zapatos'
	,NOW()
	,NOW()
),
(
	'Jolleria'
	,NOW()
	,NOW()
),
(
	'Perfumes'
	,NOW()
	,NOW()
);
/*
INSERT INTO Products(
	product_id
	,product_name
	,product_quantity
	,product_price
	,created
	,updated
) VALUES (
	'PRODUCTO_1'
	,'camiseta roja'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_2'
	,'camiseta amarilla'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_3'
	,'camiseta azul'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_4'
	,'camiseta verde'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_5'
	,'camiseta roja'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_6'
	,'camiseta amarilla'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_7'
	,'camiseta azul'
	,1
	,32.32
	,NOW()
	,NOW()
),
(
	'PRODUCTO_8'
	,'camiseta verde con correa roja en un lado del pantalon'
	,1
	,32.32
	,NOW()
	,NOW()
);


INSERT INTO product_has_category 
VALUES (
	'PRODUCTO_1'
	,1
),
(
	'PRODUCTO_2'
	,2
),
(
	'PRODUCTO_3'
	,1
),
(
	'PRODUCTO_4'
	,2
),
(
	'PRODUCTO_5'
	,1
),
(
	'PRODUCTO_6'
	,2
),
(
	'PRODUCTO_7'
	,1
),
(
	'PRODUCTO_8'
	,1
);

INSERT INTO product_image VALUES 
('PRODUCTO_1', '1.jpg')
,('PRODUCTO_1', '2.jpg')
,('PRODUCTO_1', '4.webp')
,('PRODUCTO_1', 'nevera.jpg')
,('PRODUCTO_2', '1.jpg')
,('PRODUCTO_3', '1.jpg')
,('PRODUCTO_4', '1.jpg')
,('PRODUCTO_4', 'zapato2.jpg')
*/
--SELECT * FROM product_has_category GROUP BY category_id
 --SELECT * FROM products WHERE product_id = 'PRODUCTO_1'

-- SELECT p.product_id, product_name, product_quantity, product_price, array_agg(p_i.product_image) AS images FROM products AS p 
-- INNER JOIN product_image AS p_i ON p.product_id = p_i.product_id 
-- WHERE p.product_id = 'PRODUCTO_1' 
-- GROUP BY p.product_id 
--  SELECT p.product_id,product_name,product_quantity,product_price,array_agg(p_i.product_image) FROM products AS p 
--         INNER JOIN product_image AS p_i ON p.product_id = p_i.product_id
--         WHERE p.product_id = 'PRODUCTO_1'