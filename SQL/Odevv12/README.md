Patika SQL Ödev 12
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>film</b> tablosunda film uzunluğu <b>length</b> sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?</li><br/>
  
```
SELECT COUNT(title) FROM film WHERE length > (SELECT AVG(length) FROM film);
```
  <li><b>film</b> tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?</li><br/>
  
```
SELECT COUNT(film) FROM film WHERE rental_rate = (SELECT MAX(rental_rate) FROM film);
```
  
  <li><b>film</b> tablosunda en düşük rental_rate ve en düşün replacement_cost değerlerine sahip filmleri sıralayınız.</li><br/>
  
```
SELECT title, rental_rate, replacement_cost 
FROM film 
WHERE rental_rate = (SELECT MIN(rental_rate) FROM film) AND replacement_cost = (SELECT MIN(replacement_cost) FROM film);

```
  
  <li><b>payment</b> tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.</li><br/>

```
SELECT payment.customer_id, customer.first_name, customer.last_name FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
WHERE payment.amount = (SELECT MAX(amount) FROM payment)
ORDER BY payment;
```  
</ol>

