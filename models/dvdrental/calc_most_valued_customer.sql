-- models/most_valuable_customer.sql

-- Calculate the total amount spent by each customer on rented DVDs

{{ config(materialized='table') }}

with customer_rental_totals as (
    select
        c.customer_id,
        c.first_name || ' ' || c.last_name as customer_name,
        sum(p.amount) as total_amount_spent
    from
        customer c
    left join
        payment p on c.customer_id = p.customer_id
    group by
        c.customer_id, customer_name
)

-- Rank customers based on the total amount spent
select
    customer_id,
    customer_name,
    total_amount_spent,
    rank() over (order by total_amount_spent desc) as customer_rank
from
    customer_rental_totals
