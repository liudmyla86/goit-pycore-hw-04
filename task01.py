
file = """ Alex Korp,3000 
Nikita Borisenko,2000
Sitarama Raju,1000"""

with open('salary_file.txt', 'w', encoding='utf-8') as f:
    f.write(file)


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1



            if count > 0:
                return total, total / count
            else: 
                return 0, 0
    except FileNotFoundError:
       print (f"File {path} not found")
       return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None

total, average = total_salary("salary_file.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
