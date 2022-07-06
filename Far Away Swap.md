
# Far Away Docs 🐉
--- 

## What is Far Away Swap
Far Away Swap is a decentralized exchange platform
built on NEAR blockchain. We use liquidity pools 
and order-books for these exchanges. 
That means, the application allows to
change any presented pair of crypto assets with no
intermediaries. Far Away Swap implements a new 
**combined swap** algorithm

--- 

## Main features
- **Order book** swap / limit order
- **Liquidity pool** swap / provide
- **Combined swap**

 ---
## Combined Swap Algorithm

### How it works?
When swapping, **one part of assets is being
swapped in
the order book and another part in the liquidity pool**

![](/images/combined_swap.png)

#### Pool rate
Which part of tokens is swapped in pool? It is always different.
In next paragraphs we will call it
"pool rate".

```pool_rateo = tokens_we_swap_in_pool / total_volume_of_swap```

![](/images/pool_rate.png)

It depends on the total number of
assets presented for the pair in both liquidity pool and
order book. In order to choose the best pool
rate, we use a predictive model based on our [researches](Researches.md).

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

These problems could be solved by
implementing both models at the same time
(Combined Swap Algorithm)
as their advantages perfectly complete 
their disadvantages ([check researches](Researches.md)).
