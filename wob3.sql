ALTER TABLE public.product_listings
ADD CONSTRAINT fk_seller_id
FOREIGN KEY (seller_id)
REFERENCES businesses(business_id);