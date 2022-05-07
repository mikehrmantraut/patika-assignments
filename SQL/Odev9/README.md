Patika SQL Ödev 9
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>city</b> tablosu ile <b>country</b> tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.</li><br/>
  
```
SELECT city, country FROM country
INNER JOIN city ON city.country_id = country.country_id;
```
  <li><b>customer</b> tablosu ile <b>payment</b> tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.</li><br/>
  
```
SELECT payment_id, first_name, last_name FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id;
```
  
  <li><b>customer</b> tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.</li><br/>
  
```
SELECT rental_id, first_name, last_name FROM customer
INNER JOIN rental ON customer.customer_id = rental.customer_id;
```

</ol>
