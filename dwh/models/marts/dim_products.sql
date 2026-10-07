WITH raw_products AS (
    SELECT * FROM {{ source('raw', 'products')}}
),
category_translation AS (
    SELECT * FROM {{ source('raw', 'product_category_name_translation')}}
),
joined AS (
    SELECT 
        p.product_id,
        p.product_category_name AS category_name_pt,
        COALESCE(t.product_category_name_english, 'Unknown') AS category_name_en,
        p.product_weight_g, p.product_length_cm, p.product_height_cm, p.product_width_cm
    FROM raw_products p LEFT JOIN category_translation t ON p.product_category_name = t.product_category_name
)

SELECT * FROM joined