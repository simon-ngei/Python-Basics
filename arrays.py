# store lots of data
people = ["jack", "jane", "ahmed", "hussein", "Mariam"]
scores = [87, 45, 67, 91, 29, 66, 71, 81]
print(people[0])
print(scores[0])
print(people[-1])
people.append("willis")
print(people)
scores.append(44)
print(scores)
people.sort()
scores.sort(reverse=True)
print(people)
print(scores)
print(scores[0], scores[-1])
print(sum(scores) // len(scores))
scores.count(66)
print(scores.count(66))
print(scores)
print(scores[-3:])
print(scores[0:3])
print(scores[3:5])

# set
numbers = {87, 89, 87, 67, 54}
print(numbers)

# Tuple
days =("Mon", "Tue", "Fri")

#dictionary
person = {"name": "zillow", "city": "marsabit", "age": 19}
print(person["name"])
print(sum(numbers))
watu = [{"name": "sila", "age": 22},
        {"name": "hin", "age": 59}, 
        {"name": "cril", "age": 16}]
print(watu[1]["name"])
print(watu[2]["name"])
