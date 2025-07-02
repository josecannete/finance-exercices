
WITHOLDING_TAXES = 0.15
UTM = 70_000

def compare_between_mutual_funds_and_etfs(
    years: int = 10,
    initial_investment: int = 10_000_000,
    annual_investment: int = 1_000_000,
    return_rate: float = 0.10,
    mutual_fund_fee: float = 0.0119,
    etf_fee: float = 0.001,
    dividend_yield: float = 0.03,
    chilean_tax: float = 0.23,
    sell_at_end: bool = True,
) -> None:
    """
    Compare the future value of an investment in a mutual fund versus a ETF with dividends reinvested.
    This comparison assumes costs and taxes applied when investing from Chile.

    Parameters:
    years (int): The number of years to invest.
    initial_investment (int): The initial investment amount.
    annual_investment (int): The annual investment amount.
    return_rate (float): The expected annual return rate as a decimal.
    mutual_fund_fee (float): The annual fee for the mutual fund as a decimal.
    dividend_yield (float): The annual dividend yield for the stock as a decimal.

    Returns:
    None
    """
    # Calculate the future value of the mutual fund
    mutual_fund_future_value = initial_investment
    fund_net_return_rate = return_rate - mutual_fund_fee
    mutual_fund_total_cost = 0
    mutual_fund_deposited = initial_investment
    print(
        f"Initial Investment: CLP {initial_investment:,.0f}, Annual Investment: CLP {annual_investment:,.0f}")
    
    for year in range(years):
        mutual_fund_total_cost += mutual_fund_future_value * mutual_fund_fee
        mutual_fund_future_value = (
            mutual_fund_future_value * (1 + fund_net_return_rate)
            + annual_investment
        )
        mutual_fund_deposited += annual_investment
        # print(
        #     f"Year {year + 1}: Mutual Fund Future Value: CLP {mutual_fund_future_value:,.0f}, Total Cost: CLP {mutual_fund_total_cost:,.0f}"
        # )



    # Calculate the future value of the ETF with dividends reinvested
    etf_net_return_rate = return_rate - etf_fee
    appreciation = etf_net_return_rate - dividend_yield

    etf_future_value = initial_investment
    etf_total_cost = 0
    etf_dividends_tax_cost = 0
    etf_deposited = initial_investment
    for year in range(years):
        etf_total_cost += etf_future_value * etf_fee
        etf_dividends_tax_cost += (
            etf_future_value * dividend_yield * (1 - (1 - WITHOLDING_TAXES) * (1 - (chilean_tax - WITHOLDING_TAXES)))
        )
        etf_future_value = (
            etf_future_value * (1 + appreciation)
            + etf_future_value * dividend_yield * (1 - WITHOLDING_TAXES) * (1 - (chilean_tax - WITHOLDING_TAXES))
            + annual_investment
        )
        etf_deposited += annual_investment + etf_future_value * dividend_yield * (1 - WITHOLDING_TAXES) * (1 - (chilean_tax - WITHOLDING_TAXES))

    print(f"Mutual Fund Future Value: CLP {mutual_fund_future_value:,.0f}")
    print(f"Mutual Fund Total Cost: CLP {mutual_fund_total_cost:,.0f}")
    print(f"ETF Future Value: CLP {etf_future_value:,.0f}")
    print(f"ETF Total Cost: CLP {etf_total_cost:,.0f}")
    print(f"ETF Dividends Tax Cost: CLP {etf_dividends_tax_cost:,.0f}")

    if sell_at_end:
        # Calculate the tax cost when selling the ETF at the end
        etf_tax_cost = (etf_future_value - etf_deposited) * chilean_tax
        etf_future_value -= etf_tax_cost
        print(f"ETF Tax Cost: CLP {etf_tax_cost:,.0f}")
        print(f"ETF Future Value after Tax: CLP {etf_future_value:,.0f}")

        mutual_fund_tax_cost = (mutual_fund_future_value - mutual_fund_deposited) * chilean_tax - 30 * UTM
        mutual_fund_future_value -= mutual_fund_tax_cost
        print(f"Mutual Fund Tax Cost: CLP {mutual_fund_tax_cost:,.0f}")
        print(f"Mutual Fund Future Value after Tax: CLP {mutual_fund_future_value:,.0f}")
    


if __name__ == "__main__":
    # Example usage
    years = 20
    initial_investment = 10_000_000
    annual_investment = 10_000_000
    return_rate = 0.10
    mutual_fund_fee = 0.0119
    etf_fee = 0.0006
    dividend_yield = 0.03
    chilean_tax = 0.23
    sell_at_end = True
    compare_between_mutual_funds_and_etfs(
        years,
        initial_investment,
        annual_investment,
        return_rate,
        mutual_fund_fee,
        etf_fee,
        dividend_yield,
        chilean_tax,
        sell_at_end,
    )