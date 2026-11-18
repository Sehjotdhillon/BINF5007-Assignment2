import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    numbers = []
    count = 0

    try:
        with open(filepath, 'r') as infile:
            for line_number, line in enumerate(infile, start=1):
                count += 1
                values = line.split("/t")
                try:
                    value = values[column]
                except IndexError:
                    print("Exiting There is no valid 'list index') in column "
                          + str(column) + " in line " + str(line_number)
                          + " in file: " + filepath)
                    sys.exit()
                try:
                    number = float(value)

                    if not math.isnan(number) :
                        numbers.append(number)

                except ValueError:
                    continue
    except FileNotFoundError:
        print("Error: File not found: " + filepath)
        sys.exit()

    return numbers, count
            

def calculate_average(numbers:list)->float:
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_max_and_min(numbers:list)->tuple[float, float]:
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

def calculate_variance(numbers:list)->float:
    if len(numbers) == 1:
        return 0.0
      
    average = calculate_average(numbers)
    total = 0

    for number in numbers:
        total += (number - average) ** 2
    variance = total / (len(numbers) -1)
    return variance

def calculate_std_dev(numbers:list)->float:
    variance = calculate_variance(numbers)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

def calculate_median(number:list)->float:
    number.sort()
    middle = len(number) // 2

    if len(number) % 2 == 0:
        median = (number[middle - 1] + number[middle]) / 2
    else:
        median = float(number[middle])
    return median