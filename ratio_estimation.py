def get_optimal_ratio(
        amount_inA: float,
        orders: list,
        step=100,
        reserves_in=1254000,
        reserves_out=10000) -> list:
    """
    calculation of $A ratio sold in pool to get maximum of $B
    param orders: test order book data
    param step: the precision of algorithm depends on this param
    returns: [
        <ratio of $A sold in pool to get the max of $B>,
        <average $B price>
        ]
    """

    amounts_out = []
    steps = numpy.arange(step, amount_inA, step)

    for amount_in_pool in steps:
        test_orders = orders.copy()
        pool_amount_out = get_amount_out_pool(
            amount_in_pool, reserves_in, reserves_out
        )
        ob_amount_out = get_amount_out_ob(
            amount_inA - amount_in_pool, test_orders
        )
        amounts_out.append(pool_amount_out + ob_amount_out)

    max_amount_out = max(amounts_out)
    max_profit_a_pool = list(steps)[amounts_out.index(max_amount_out)]
    max_profit_a_pool_ratio = max_profit_a_pool/amount_inA
    token_b_price = amount_inA/max_amount_out

    return [max_profit_a_pool_ratio, token_b_price]