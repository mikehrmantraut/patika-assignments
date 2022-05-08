-- Kitap sayfası sayısı ortalama kitap sayfası sayısından fazla
-- olan kitap isimlerini, yazar isim ve soyisimleri ile birlikte sıralayalım.
SELECT author.first_name, author.last_name, book.title, book.page_number
FROM author
INNER JOIN book
ON book.author_id = author.id
WHERE page_number > 
(
	SELECT AVG(page_number)
	FROM book
);
