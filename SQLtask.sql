SELECT u.email, COUNT(u.id) as total_urls
FROM users_user u
JOIN urls_url r ON u.id = r.user_id
GROUP BY u.id, u.email
ORDER BY total_urls DESC, u.date_joined
LIMIT 10;