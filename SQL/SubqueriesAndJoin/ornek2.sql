-- film uzunluğu en fazla olan filmlerin isimlerini, uzunluğunu actor isim ve soyisimleri
-- ile birlikte yazalım.

SELECT actor.first_name, actor.last_name, film.title, film.length
FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film.length = 
(
	SELECT MAX(length) FROM film
);
