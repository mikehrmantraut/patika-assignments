Patika SQL Ödev 4
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>film</b> tablosunda bulunan <b>replacement_cost</b> sütununda bulunan birbirinden farklı değerleri sıralayınız</li><br/>
  
```
SELECT DISTINCT replacement_cost FROM film;
```
  <li><b>film</b> tablosunda bulunan <b>replacement_cost</b> sütununda birbirinden farklı kaç tane veri vardır?</li><br/>
  
```
SELECT COUNT(DISTINCT replacement_cost) FROM film;
```
  
  <li><b>film</b> tablosunda bulunan <b>film</b> isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?</li><br/>
  
```
SELECT COUNT(title) FROM film WHERE title LIKE('T%') AND rating='G';
```
  
  <li><b>country</b> tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?</li><br/>

```
SELECT COUNT(country) FROM countryWHERE LENGTH(country) = 5;
```
  <li><b>city</b> tablosundaki şehir isimlerinin kaç tanesi 'R' veya r karakteri ile biter?</li><br/>

```
SELECT COUNT(city) FROM city WHERE city ILIKE('%R');
```  
</ol>
