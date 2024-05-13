# Use cases

This document contains use-cases of this task. As this is just a Interview task I do not define any django group, only Non-loged-in users (Anonymous Users), SuperUsers (I call them as Admin), and Non-super-users (I call them as Normal Users).

| use case | description | Access |
| -------- | ----------- | ------- |
| register | register a new user | Anonymous Users |
| login | login a user | Anonymous Users |
| Add Product | Add product by admin | Admins |
| Product List | List of Products and overal rating of the products | Anyone |
| Set and Update rating of Product | Both Set and Update Rating 0 - 5 to Products | Non-Anonymous Users |

## Models 

In this section I decided on models required for this task and fields of each

### Product 

| field name | type | description |
| ---------- | ---- | ----------- |
| id | integer - auto-increment | Unique |
| title | varchar(128) | ----- |

### ProductRating 

| field name | type | description |
| ---------- | ---- | ----------- |
| id | integer - auto-increment | --- |
| user_id | Foreign Key | uniqute_togeter(user_id, product_pk, rating) |
| product_id | Foreign Key | uniqute_togeter(user_id, product_pk, rating) |
| rating | SmallIntegerField | uniqute_togeter(user_id, product_pk, rating) |

