# Dictionary  is a kind of data structure in python it is used to map the value pairs
# Dictionary is nothing but a key value pair
#
# d1 = {} this is a empty Dictionary
#
# d1 = [] this is a empty list
#
# d1 = () this is a empty  tuple


# print(type(d1))

d2 = {"harry": "burger",
      "rohan": "fish",
      "Mukul": "Roti",
      "shubham": {      # nested Dictionary
          "morning": "breakfast",
          "afternoon": "launch",
          "evening": "snax",
          "night": "Dinner"
          },

      }


# print(d2["harry"])
# print(d2["Mukul"])

# print(d2["shubham"]["evening"])  #This is how you can the nested dictionary


# d2["Ankit"] = "junk food"    this how u can add externally into a dictionary

# del d2["Mukul"] using del you can delete elements from dictionary


# print(d2)

# d3 = d2 # this is basically a creating a referance so if you delete in element in d3 it outomatically gets deleted from d2
# to avoid this we can use a copy function

# d3 = d2.copy()
# del d3["rohan"]
# print(d2)
# print(d3)

# d2.update({"leena": "toffie"})   # update function adds the at last of the dictionary eleemnt


# print(d2.keys())  # this can only print the keys

# print(d2.items()) it print the key value pairs

print(d2)
