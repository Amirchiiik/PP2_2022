CREATE OR REPLACE PROCEDURE new_user(
	num varchar,
	fname text,
    lname text
) 
AS $$

BEGIN

	UPDATE Phone_number_book
	SET phone_number = num
	WHERE firstname = fname and lastname = lname;

	IF NOT FOUND THEN
	INSERT INTO Phone_number_book(phone_number, firstname, lastname)
	VALUES(num, fname, lname);
	END IF;
	
END; $$
LANGUAGE plpgsql;