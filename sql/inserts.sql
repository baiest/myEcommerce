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
