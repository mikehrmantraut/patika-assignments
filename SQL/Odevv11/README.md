Patika SQL Ödev 11
--
Aşağıdaki sorgu senaryolarını <b>dvdrental</b> örnek veri tabanı üzerinden gerçekleştiriniz.
<ol>
  <li><b>actor</b> ve <b>customer</b> tablolarında bulunan <b>first_name</b> sütunları için tüm verileri sıralayalım.</li><br/>
  
```
(SELECT first_name FROM actor)
UNION
(SELECT first_name FROM customer);
```
  <li><b>actor</b> ve <b>customer</b> tablolarında bulunan <b>first_name</b> sütunları için kesişen verileri sıralayalım.</li><br/>
  
```
(SELECT first_name FROM actor)
INTERSECT
(SELECT first_name FROM customer);
```
  
  <li><b>actor</b> ve <b>customer</b> tablolarında bulunan <b>first_name</b> sütunları için ilk tabloda bulunan ancak ikinci tabloda bulunmayan verileri sıralayalım.</li><br/>
  
```
(SELECT first_name FROM actor)
EXCEPT
(SELECT first_name FROM customer);
```
  
  <li>İlk 3 sorguyu tekrar eden veriler için de yapalım.</li><br/>

```
(SELECT first_name FROM actor) UNION ALL (SELECT first_name FROM customer);  
(SELECT first_name FROM actor) INTERSECT ALL (SELECT first_name FROM customer);
(SELECT first_name FROM actor) EXCEPT ALL (SELECT first_name FROM customer);
```  
</ol>

