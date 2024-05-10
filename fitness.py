# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F):")
    birth_str = input("Enter your birthdate(YYYY-MM-DD): ")
    weight = float(input("Enter your weight in U.S. pounds: "))
    height = float(input("Enter your height in U.S. inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    years = compute_age(birth_str)
    m_kg = kg_from_lb(weight)
    length = cm_from_in(height)
    b_mi = body_mass_index(m_kg, length)
    b_mr =  basal_metabolic_rate(gender, m_kg, length, years)


    # Print the results for the user to see.
    pass
    print(f"Age (years): {years:.0f}")
    print(f"Weight (kg): {m_kg:.2f}")
    print(f"Height (cm): {length:.1f}")
    print(f"Body mass index: {b_mi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {b_mr:.0f}")



def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(weight):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    m_kg = weight/0.45359237

    return m_kg


def cm_from_in(height):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    length = height * 2.54
    return length


def body_mass_index(m_kg, length):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    b_mi = m_kg / (length**2 ) * 10000
    return b_mi


def basal_metabolic_rate(gender, m_kg, length, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """

    if (gender == 'f' or gender == 'F'):
        b_mr = 447.593 + 9.247 * m_kg + 3.098 * length - 4.330 * years
    else:
        b_mr = 88.362 + 13.397 * m_kg + 4.799 * length - 5.677 * years
    
    return b_mr


# Call the main function so that
# this program will start executing.

main()
