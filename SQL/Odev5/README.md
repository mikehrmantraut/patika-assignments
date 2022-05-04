Patika SQL Ödev 5
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>film</b> tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en uzun (length) 5 filmi sıralayınız.</li><br/>
  
```
SELECT title, length FROM film WHERE title LIKE('%n') ORDER BY length DESC LIMIT 5;
```
  <li><b>film</b> tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en kısa (length) ikinci(6,7,8,9,10) 5 filmi(6,7,8,9,10) sıralayınız.</li><br/>
  
```
SELECT title, length FROM film  WHERE title LIKE('%n')  ORDER BY length OFFSET 5 LIMIT 5;

```
  
  <li><b>customer</b> tablosunda bulunan last_name sütununa göre azalan yapılan sıralamada store_id 1 olmak koşuluyla ilk 4 veriyi sıralayınız.</li><br/>
  
```
SELECT *  FROM customer WHERE store_id = 1 ORDER BY last_name DESC LIMIT 4;
```

</ol>
