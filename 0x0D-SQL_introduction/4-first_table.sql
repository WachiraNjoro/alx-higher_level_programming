-- creates a table called first_table in the current database in my MySQL server
-- Does not fail if table exists
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
