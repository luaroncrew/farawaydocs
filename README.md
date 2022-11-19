# Overview

## What is farswap?
farswap is a decentralized exchange platform with integrated liquidity aggregator
built on NEAR blockchain.

### Just another DEX? Not we're better:
There is a key thing to know about farswap:

farswap implements the new [combined swap](#Combined-Swap) market making model
that makes markets more liquid and consequently gives you more profit when you execute the swaps.
efficiency and consequently provides you:
- lower prices
- lower fees
- fast trading experience
---

## Combined Swap
Combined swap can be imagined as order-books working on top of liquidity pools

### Why it works?
farswap order books, built on top of pools, make illiquid pairs liquid by concentrating way more liquidity around the
market price. Consequently, trades become more profitable as order books reduce
the slippage and the fees. Combined swap is very fast,
since we use mathematical models instead of computing values on the blockchain.

Combined swap is better than just a liquidity-pool-based exchange,
as we have an additional liquidity in farswap order books,
well concentrated around the market price.
Also, Combined swap is better than just an order book,
since we can use the liquidity of the existing pools along
with the liquidity in farswap order books to provide better prices.

example:

![](/images/pool_plus_order_book.png)

### Implementation
When swapping, one part of assets is being
swapped in the order book and another is in liquidity pool.

![](/images/combined_swap.png)


#### Pool rate
Which part of tokens is swapped in pool? It is always different.
In next paragraphs we will call it
"pool rate".

```pool_rate = volume_to_swap_in_pool / total_volume_of_swap```

![](/images/pool_rate.png)

It depends on the total number of
assets presented for the pair in both liquidity pool and
order book. In order to choose the best pool
rate, we will use a predictive models based on our [researches](researches.md).

---

### Why do we need it?
Most DEX platforms use two models of 
exchange:  automated market maker (AMM) 
and order book. Both models have some disadvantages
- Illiquid market 
makes traders have difficulty 
in finding matching orders
due to large bid-ask spread and low trading volumes.
If you want to have successful orders,
you have to make sure that your highest 
bid is lower than the lowest ask.
- AMM causes high slippage for large orders:
Slippage relies on the liquidity pool’s size of a 
certain trading pair. The liquidity pool 
needs to be 100x greater than the size 
of the order to keep the slippage rate under 1\%

These problems cause a liquidity lack on the market. At farswap we believe that with the combined swap, even 
shitcoins will be liquid.