# Fees and profit

--- 

## Fees

--- 

When you swap your assets on Far Away, whether in an order book or 
in a liquidity pool, we take some swap fees.

<b>Currently the maximum swap fee does not exceed ```0.3%``` of swap volume</b>


There are different type of fees:
- transaction fee (almost negligible)
- Far Away Swap
  - provider fee
  - protocol fee

Here are the explanations of fees for each type of swap you can execute on Far Away.

###  Liquidity Pool Swap Fees
Far Away takes two types of fees in the liquidity pool: 

- ```0.3%``` <u>provider fee</u> that makes 
liquidity providers lock their assets in pool.
In the future we are going to implement different provider fee levels
but **right now all liquidity pools have 0.3% fee**


The total fee is: 

```fees = Provider Fee + Transaction Fee``` 

It currently gives us 
0.3% + negligible transaction fee for each pool swap.


### Order Book Fees
Order book has only one fee - Far Away Protocol Fee. So currently
each order have a ```0.1%``` fee on the transaction volume.


### Combined Swap Fees
In combined swap fee rate for a volume is always different.
It depends on [pool rate](/far-away-docs#pool-rate). 
However, it is not hard to calculate it.
For example, if pool ratio = 20%, pool fee level = 0.3%,
order book fee level = 0.1%, then your fee is

``` fee =  80% * SwapVolume * 0.1% + 20% * SwapVolume * 0.3% ```


---

## Liquidity providers profit
All liquidity providers get profit, proportional to the 
liquidity put in a pool.

For example, if you add 50 $NEAR and 250 $USN in a liquidity pool,
and after that, there are 500 $NEAR and 2500 $USN in total, then 
you owe 10% of pool's liquidity. Every time users swap their 
tokens in this pool (with 0.3% liquidity provider fee),
as a liquidity provider, you get 

``` profit = SwapVolume * 0.3% * 10% ```

However, this profit is put back to pool.
You can pick it back on your wallet at every time.

If you want to become a liquidity provider, know that there are nevertheless
some risks. One significant risk is impermanent loss,
this is a great
[explanation](https://academy.binance.com/en/articles/impermanent-loss-explained)
of this concept by Binance Academy. 
Make sure to understand what impermanent loss is before provide your 
liquidity to pools.

