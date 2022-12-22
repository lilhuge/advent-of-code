with open("input.txt", "r") as f:
    foodItems = [contents.replace("\n", "") for contents in f.readlines()]
    elfCalorieCount = 0
    elvesCalorieList = []
    for i, foodItem in enumerate(foodItems):
        if foodItem == "" or i+1 == len(foodItems):
            elvesCalorieList.append(elfCalorieCount)
            elfCalorieCount = 0
        else:
            elfCalorieCount += int(foodItem)

        
print(max(elvesCalorieList))
