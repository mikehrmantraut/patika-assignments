Patika SQL Ödev 8
--

<ol>
  <li><b>test</b> veritabanınızda <b>employee</b> isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım </li><br/>

    
```
 CREATE TABLE employee(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	birthday DATE,
	email VARCHAR(100)
) 
```
  <li>Oluşturduğumuz <b>employee</b> tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.</li><br/>
  
![Adsız](https://user-images.githubusercontent.com/76072666/167127346-d8459df9-6d16-4ee9-99d0-07480b1cc24d.png)

  
  <li>Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.</li><br/>
  
```
 UPDATE employee
 SET name = 'Ahmet',
	   birthday = '1994-05-23',
	   email = 'ahmet@xd.com'
 WHERE id <=5
 RETURNING *;
```
  <li>Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.</li>

```
  DELETE FROM employee
  WHERE id>10 AND id<=15;
```
</ol>
