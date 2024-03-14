// THis file is supposed to generate the endpoints for the frontend.

DOMAIN = '<This Domain!>'

endpoints = {
    products: fetch(`${DOMAIN}/products/`),
    product: 'products/<int:id>/0/',
}