-- List all brands with glam rock as the main style
SELECT band_name,
    SUM(COALESCE(split, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
GROUP BY band_name
ORDER BY lifespan DESC;
