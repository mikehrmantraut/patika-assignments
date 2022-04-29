Patika SQL Ödev 3
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>country</b> tablosunda bulunan <b>country</b> sütunundaki ülke isimlerinden 'A' karakteri ile başlayıp 'a' karakteri ile sonlananları sıralayınız.</li><br/>
  
```
SELECT * FROM country WHERE country LIKE('A%a');
```
  <li><b>country</b> tablosunda bulunan <b>country</b> sütunundaki ülke isimlerinden en az 6 karakterden oluşan ve sonu 'n' karakteri ile sonlananları sıralayınız.</li><br/>
  
```
SELECT * FROM country WHERE country LIKE('%n') AND length(country) >= 6;
```
  
  <li><b>film</b> tablosunda bulunan title sütunundaki <b>film</b> isimlerinden en az 4 adet büyük ya da küçük harf farketmesizin 'T' karakteri içeren film isimlerini sıralayınız.</li><br/>
  
```
SELECT title FROM film WHERE title ILIKE('%t%t%t%t');
```
  
  <li><b>film</b> tablosunda bulunan tüm sütunlardaki verilerden <b>title</b> 'C' karakteri ile başlayan ve uzunluğu (length) 90 dan büyük olan ve rental_rate 2.99 olan verileri sıralayınız.</li><br/>

```
SELECT * FROM film WHERE title LIKE('C%') AND length > 90 AND rental_rate = 2.99;
```
</ol>
