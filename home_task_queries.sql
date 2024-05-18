/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
SELECT count(f.film_id) as films_count,
       c.name as category_name
FROM film_category f
JOIN category c ON  f.category_id=c.category_id
GROUP BY c.name
ORDER BY 1 DESC;



/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
SELECT count(r.inventory_id), a.first_name || ' ' || a.last_name as full_actor_name
FROM rental r
JOIN inventory i on r.inventory_id=i.inventory_id
JOIN film_actor fa on i.film_id=fa.film_id
JOIN actor a on fa.actor_id=a.actor_id
GROUP BY 2
ORDER BY 1 DESC
LIMIT 10;



/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
SELECT sum(p.amount) as payment_sum, c.name as category_name
FROM payment p
JOIN rental r on p.rental_id=p.rental_id
JOIN inventory i on r.inventory_id=i.inventory_id
JOIN film_category fc on fc.film_id=i.film_id
JOIN category c on fc.category_id=c.category_id
GROUP BY 2
ORDER BY 1 DESC;




/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
SELECT f.title
FROM film f
LEFT JOIN inventory i ON i.film_id = f.film_id
WHERE i.film_id is NULL;


/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
SELECT count(fa.actor_id), a.first_name || ' ' || a.last_name as actor_full_name
FROM film_actor fa
JOIN film_category fc ON fa.film_id=fc.film_id
JOIN category c ON fc.category_id=c.category_id
JOIN actor a ON fa.actor_id=a.actor_id
WHERE c.name = 'Children'
GROUP by 2
ORDER BY 1 DESC
LIMIT 3