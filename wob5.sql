ALTER TABLE public.order_items
ADD CONSTRAINT fk_product_listings_id
FOREIGN KEY (product_listing_id) REFERENCES product_listings(product_listing_id) ON DELETE CASCADE; 