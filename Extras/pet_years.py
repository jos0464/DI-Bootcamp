def calculate_pet_years(human_years):
    # Calculate cat years
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Example usage:
human_years = 10
result = calculate_pet_years(human_years)
print(result)  # Output: [5, 37, 44]
human_years = 1
result = calculate_pet_years(human_years)
print(result)
human_years = 2
result = calculate_pet_years(human_years)
print(result)
