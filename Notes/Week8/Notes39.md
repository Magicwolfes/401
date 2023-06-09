# SQLi with Burp Suite, WebGoat

## What is SQL injection?
SQL injection is a type of web application vulnerability that occurs when an attacker can manipulate the SQL queries executed by a web application's backend database. It allows the attacker to insert malicious SQL code into the application's input fields, which is then executed by the database server, potentially leading to unauthorized access, data manipulation, or data leakage.

## Can you give an example of how a hacker could use SQL injection to gain unauthorized access?
An attacker can exploit a SQL injection vulnerability by manipulating the input fields to inject malicious SQL code. As a result of successful SQL injection, the attacker bypasses the authentication mechanism and gains unauthorized access to the application. The application responds to the modified query by returning data for all users since the condition '1'='1' is true for every row.

## What are some ways to prevent SQL injection attacks on a web server?
Implement strict input validation to ensure that user-supplied data matches the expected format and meets specific criteria.
Sanitize user input by removing or encoding special characters that could be interpreted as SQL code.
Utilize server-side input validation, as client-side validation alone can be bypassed.