# -*- coding: utf-8 -*-


def monthly_afp_cost(afp_fee: float, salary: float) -> float:
    """
    Calculate the total costs of an AFP (Administradora de Fondos de Pensiones) for a given salary.
    """
    return afp_fee * salary


def afp_simulation(
    years: int,
    initial_investment: float,
    salary: float,
    afp_fee: float,
    return_rate: float,
    afp_contribution_rate: float,
) -> tuple[float, float]:
    acc_afp_cost = 0
    future_value = initial_investment

    for _ in range(years):
        monthly_cost = monthly_afp_cost(afp_fee, salary)
        annual_cost = monthly_cost * 12
        acc_afp_cost += annual_cost

        annual_invested_amount = salary * afp_contribution_rate * 12

        future_value = (future_value + annual_invested_amount) * (1 + return_rate)

    return future_value, acc_afp_cost


def afp_comparison(
    years: int,
    initial_investment: float,
    salary: float,
    first_afp_fee: float,
    second_afp_fee: float,
    first_afp_return_rate: float,
    second_afp_return_rate: float,
    afp_contribution_rate: float,
) -> None:
    """
    Compare the future value of two AFPs with different fees and return rates.

    Parameters:
    years (int): The number of years to invest.
    initial_investment (float): The initial investment amount.
    salary (float): The monthly salary used for contributions.
    first_afp_fee (float): The monthly fee for the first AFP as a decimal.
    second_afp_fee (float): The monthly fee for the second AFP as a decimal.
    first_afp_return_rate (float): The annual return rate for the first AFP as a decimal.
    second_afp_return_rate (float): The annual return rate for the second AFP as a decimal.
    afp_contribution_rate (float): The contribution rate as a decimal.

    """
    first_afp_future_value, first_afp_cost = afp_simulation(
        years,
        initial_investment,
        salary,
        first_afp_fee,
        first_afp_return_rate,
        afp_contribution_rate,
    )

    second_afp_future_value, second_afp_cost = afp_simulation(
        years,
        initial_investment,
        salary,
        second_afp_fee,
        second_afp_return_rate,
        afp_contribution_rate,
    )

    print(f"First AFP Future Value: CLP {first_afp_future_value:,.0f}")
    print(f"First AFP Total Cost: CLP {first_afp_cost:,.0f}")
    
    print(f"Second AFP Future Value: CLP {second_afp_future_value:,.0f}")
    print(f"Second AFP Total Cost: CLP {second_afp_cost:,.0f}")

    print(f"Difference in Future Value: CLP {first_afp_future_value - second_afp_future_value:,.0f}")
    print(f"Difference in Total Cost: CLP {first_afp_cost - second_afp_cost:,.0f}")

    print(f"Difference in Future Value - Difference in Total Cost: CLP {first_afp_future_value - second_afp_future_value - (first_afp_cost - second_afp_cost):,.0f}")
    


def main():
    print("AFPs exercise.")
    years = 30
    initial_investment = 2_000_000  # CLP
    salary = 700_000  # CLP
    afp_contribution_rate = 0.11  # 11% contribution rate

    # Habitat AFP parameters
    habitat_afp_fee = 1.27 / 100 # 1.27% monthly fee
    habitat_afp_return_rate =  5.38 / 100  # 5.38% annual return rate

    # Modelo AFP parameters
    modelo_afp_fee = 0.58 / 100  # 0.58% monthly fee
    modelo_afp_return_rate = 5.29 / 100  # 5% annual return rate

    afp_comparison(
        years,
        initial_investment,
        salary,
        habitat_afp_fee,
        modelo_afp_fee,
        habitat_afp_return_rate,
        modelo_afp_return_rate,
        afp_contribution_rate,
    )


if __name__ == "__main__":
    main()
