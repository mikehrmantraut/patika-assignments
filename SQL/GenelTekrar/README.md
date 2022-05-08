Patika.dev SQL eğitiminde "Genel Tekrar Dersi"'ndeki SQL örnekleri:
--
<li>İsminde en az 4 tane e veya E bulunan kaç film vardır?</li>

```
SELECT COUNT(*) FROM film
WHERE title ILIKE('%e%e%e%e%');
```

<li>Kategori isimlerini ve kategori başına düşen film sayısını yazınız.</li>

```
SELECT category.name, COUNT(*) 
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film.film_id = film_category.film_id
GROUP BY category.name
ORDER BY category.name;
```

<li>En çok film bulunan rating kategorisi hangisidir?</li>

```
SELECT COUNT(title), rating FROM film
GROUP BY rating
ORDER BY COUNT(title) DESC
LIMIT 1;
```

<li>Film tablosunda 'K' karakteri ile başlayan en uzun ve replacement_cost en az olan 3 filmi sıralayınız.</li>

```
SELECT title FROM film
WHERE title LIKE('K%')
ORDER BY length DESC, replacement_cost ASC
LIMIT 3;
```

<li> En çok alışveriş yapan müşterinin adı nedir?</li>

```
SELECT SUM(amount), customer.first_name, customer.last_name
FROM payment
JOIN customer ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id, customer.first_name, customer.last_name
ORDER BY SUM(amount) DESC
LIMIT 1;
```
