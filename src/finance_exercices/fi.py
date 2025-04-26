import numpy as np

def financial_independence(annual_expenses, withdrawal_rate):
    """
    Calculate the amount needed for financial independence.

    Parameters:
    annual_expenses (float): The annual expenses.
    withdrawal_rate (float): The withdrawal rate as a decimal.

    Returns:
    float: The amount needed for financial independence.
    """
    return annual_expenses / withdrawal_rate

def years_to_fi(current_savings, annual_expenses, withdrawal_rate, annual_investment, annual_return_rate, inflation_rate):
    """
    Calculate the number of years to financial independence, accounting for inflation.

    Parameters:
    current_savings (float): The current savings.
    annual_expenses (float): The annual expenses.
    withdrawal_rate (float): The withdrawal rate as a decimal.
    annual_investment (float): The annual investment.
    annual_return_rate (float): The expected annual return on investments as a decimal.
    inflation_rate (float): The expected annual inflation rate as a decimal.

    Returns:
    float: The number of years to financial independence.
    """
    real_return_rate = (1 + annual_return_rate) / (1 + inflation_rate) - 1
    target_amount = financial_independence(annual_expenses, withdrawal_rate)
    years = 0
    while current_savings < target_amount:
        current_savings += annual_investment
        current_savings *= (1 + real_return_rate)
        annual_expenses *= (1 + inflation_rate)  # Adjust expenses for inflation
        target_amount = financial_independence(annual_expenses, withdrawal_rate)  # Recalculate target amount
        years += 1
    return years

def years_to_fi_with_confidence(current_savings, annual_expenses, withdrawal_rate, annual_investment, annual_return_rate, inflation_rate, return_std_dev, inflation_std_dev, num_simulations=1000, confidence_level=0.95):
    """
    Calculate the number of years to financial independence with confidence intervals.

    Parameters:
    current_savings (float): The current savings.
    annual_expenses (float): The annual expenses.
    withdrawal_rate (float): The withdrawal rate as a decimal.
    annual_investment (float): The annual investment.
    annual_return_rate (float): The expected annual return on investments as a decimal.
    inflation_rate (float): The expected annual inflation rate as a decimal.
    return_std_dev (float): The standard deviation of the annual return rate.
    inflation_std_dev (float): The standard deviation of the annual inflation rate.
    num_simulations (int): The number of simulations to run.
    confidence_level (float): The confidence level for the interval (e.g., 0.95 for 95%).

    Returns:
    tuple: The mean, lower bound, and upper bound of the confidence interval for years to financial independence.
    """
    results = []

    for _ in range(num_simulations):
        simulated_return_rate = np.random.normal(annual_return_rate, return_std_dev)
        simulated_inflation_rate = np.random.normal(inflation_rate, inflation_std_dev)
        real_return_rate = (1 + simulated_return_rate) / (1 + simulated_inflation_rate) - 1

        years = 0
        savings = current_savings
        expenses = annual_expenses
        target_amount = financial_independence(expenses, withdrawal_rate)

        while savings < target_amount and years < 100:  # Limit to 100 years to avoid infinite loop
            savings += annual_investment
            savings *= (1 + real_return_rate)
            expenses *= (1 + simulated_inflation_rate)
            target_amount = financial_independence(expenses, withdrawal_rate)
            years += 1

        results.append(years)

    mean_years = np.mean(results)
    lower_bound = np.percentile(results, (1 - confidence_level) / 2 * 100)
    upper_bound = np.percentile(results, (1 + confidence_level) / 2 * 100)

    return mean_years, lower_bound, upper_bound

