-- models/top_10_customers_email_list.sql

-- Get the top 10 most valued customers

{{ config(materialized='view') }}

with ranked_customers as (
    select
        customer_id,
        customer_name,
        total_amount_spent,
        rank() over (order by total_amount_spent desc) as customer_rank
    from
        {{ ref('calc_most_valued_customer') }}
)

-- Filter the top 10 customers and retrieve their email addresses
select
    c.email,
    rc.customer_name
from
    customer c
join
    ranked_customers rc on c.customer_id = rc.customer_id
where
    rc.customer_rank <= 10
