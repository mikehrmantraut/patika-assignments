Patika SQL Ödev 2
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
<li>film tablosunda bulunan tüm sütunlardaki verileri replacement cost değeri 12.99 dan büyük eşit ve 16.99 küçük olma koşuluyla sıralayınız ( BETWEEN - AND yapısını kullanınız.)</li><br/>
  
  
```
SELECT * FROM film WHERE replacement_cost BETWEEN 12.99 AND 16.99;
```
  <li><b>actor</b> tablosunda bulunan first_name ve last_name sütunlardaki verileri first_name 'Penelope' veya 'Nick' veya 'Ed' değerleri olması koşuluyla sıralayınız. ( IN operatörünü kullanınız.)</li><br/>
  
```
SELECT * FROM actor WHERE first_name IN('Penelope', 'Nick', 'Ed');
```
  
  <li><b>film</b> tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99, 2.99, 4.99 <b>VE</b> replacement_cost 12.99, 15.99, 28.99 olma koşullarıyla sıralayınız. ( IN operatörünü kullanınız.)</li><br/>
  
```
SELECT * FROM film WHERE rental_rate IN(0.99, 2.99, 4.99) AND replacement_cost IN(12.99, 15.99, 28.99);
```
</ol>
