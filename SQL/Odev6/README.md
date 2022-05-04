Patika SQL Ödev 6
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>film</b> tablosunda bulunan rental_rate sütunundaki değerlerin ortalaması nedir?</li><br/>
  
```
SELECT AVG(rental_rate) FROM film;
```
  <li><b>film</b> tablosunda bulunan filmlerden kaç tanesi 'C' karakteri ile başlar?</li><br/>
  
```
SELECT COUNT(title) FROM film WHERE title LIKE('C%');
```
  
  <li><b>film</b> tablosunda bulunan filmlerden rental_rate değeri 0.99 a eşit olan en uzun (length) film kaç dakikadır?</li><br/>
  
```
SELECT MAX(length) FROM film WHERE rental_rate = 0.99;
```
  
  <li><b>film</b> tablosunda bulunan filmlerin uzunluğu 150 dakikadan büyük olanlarına ait kaç farklı replacement_cost değeri vardır?</li><br/>

```
SELECT COUNT(DISTINCT(replacement_cost)) FROM film WHERE length > 150;
```  
</ol>
