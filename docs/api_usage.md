# API Usage

## GET list of the products

Endpoint: GET `/api/products`

**Note**: you can set `page_size` for different pagination. As an example: GET `/api/products?page_size=100`.

## Create a product

Endpoint: POST `/api/products/` 

data_keys: ['title']

## Edit a product

Endpoint: PATCH `/api/products/<product_id>/` 

data_keys: ['title']

## delete a product

Endpoint: DELETE `/api/products/<product_id>/` 

---------------

## Get list of rating of  the product

Endpoint: GET `/api/products/<product_id>/ratings/`,


## Create or update a rating for a product

Endpoint: POST `/api/products/<product_id>/ratings/`,

data_keys: [`rating`]

