Patika SQL Ödev 7
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>film</b> tablosunda bulunan filmleri <b>rating</b> değerlerine göre gruplayınız.</li><br/>
    
```
  SELECT rating, title FROM film GROUP BY rating, title;
```
  <li><b>film</b> tablosunda bulunan filmleri <b>replacement_cost</b> sütununa göre grupladığımızda film sayısı 50 den fazla olan replacement_cost değerini ve karşılık gelen film sayısını sıralayınız.</li><br/>
  
```
  SELECT replacement_cost, COUNT(title) FROM film GROUP BY replacement_cost HAVING COUNT(title) > 50; 
```
  
  <li><b>customer</b> tablosunda bulunan store_id değerlerine karşılık gelen müşteri sayılarını nelerdir?</li><br/>
  
```
  SELECT store_id, COUNT(customer_id) FROM customer GROUP BY store_id;
```
  <li><b>city</b> tablosunda bulunan şehir verilerini <b>country_id</b> sütununa göre gruplandırdıktan sonra en fazla şehir sayısı barındıran country_id bilgisini ve şehir sayısını paylaşınız.</li>

```
  SELECT country_id, COUNT(city) FROM city GROUP BY country_id ORDER BY COUNT(city) DESC LIMIT 1;
```
</ol>
