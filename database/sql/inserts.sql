INSERT INTO users(
	user_id
	,user_email
	,user_name
	,user_lastname
	,created
	,updated
) VALUES (
	'1005944768'
	,'juanba@gmail.com'
	,'Juan'
	,'Ballesteros'
	,NOW()
	,NOW()
)
,(
	'1005944763'
	,'camilo@gmail.com'
	,'Camilo'
	,'Ballesteros'
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

--SELECT * FROM product_has_category GROUP BY category_id
 SELECT * FROM products WHERE product_id = 'PRODUCTO_1'