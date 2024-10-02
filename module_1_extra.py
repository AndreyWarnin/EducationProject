grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_ = list(students)
list_.sort()

med_list = []
da = grades[::]
print(da)

dictionary = {}
dictionary[list_[0]] = sum(grades[0])/len(grades[0])
dictionary[list_[1]] = sum(grades[1])/len(grades[1])
dictionary[list_[2]] = sum(grades[2])/len(grades[2])
dictionary[list_[3]] = sum(grades[3])/len(grades[3])
dictionary[list_[4]] = sum(grades[4])/len(grades[4])
print(dictionary)