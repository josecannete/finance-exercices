from src.finance_exercices.fi import financial_independence, years_to_fi, years_to_fi_with_confidence


def main():
    # Example inputs
    current_savings = 10_000_000
    annual_expenses = 24_000_000
    withdrawal_rate = 0.04
    annual_investment = 3_000_000
    annual_return_rate = 0.08
    inflation_rate = 0.03

    # Calculate financial independence target
    target = financial_independence(annual_expenses, withdrawal_rate)
    print(f"Target for financial independence: CLP {target:,.0f}")

    # Calculate years to financial independence
    years = years_to_fi(
        current_savings,
        annual_expenses,
        withdrawal_rate,
        annual_investment,
        annual_return_rate,
        inflation_rate,
    )
    print(f"Years to financial independence: {years}")

    # Calculate years to financial independence with confidence intervals
    return_std_dev = 0.02  # Example standard deviation for return rate
    inflation_std_dev = 0.01  # Example standard deviation for inflation rate
    num_simulations = 1000
    confidence_level = 0.95

    mean_years, lower_bound, upper_bound = years_to_fi_with_confidence(
        current_savings,
        annual_expenses,
        withdrawal_rate,
        annual_investment,
        annual_return_rate,
        inflation_rate,
        return_std_dev,
        inflation_std_dev,
        num_simulations,
        confidence_level
    )

    print(f"Mean years to financial independence: {mean_years:.2f}")
    print(f"{confidence_level * 100:.0f}% confidence interval: {lower_bound:.2f} - {upper_bound:.2f} years")


if __name__ == "__main__":
    main()
