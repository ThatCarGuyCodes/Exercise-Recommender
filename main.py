import pandas as pd

df=pd.read_html("https://en.wikipedia.org/wiki/List_of_weight_training_exercises")

part = input("Which body part do you wish to exercise (copy paste from the description)? ")
df0 = df[0]
df0.to_csv("exercises.csv")

def recommend(part):
  exercises = []
  indices0 = df0[df0[part] == "Yes"].index.tolist()
  indices1 = df0[df0[part] == "Some"].index.tolist()
  for item in indices0:
    loc = df0.iloc[item, 0]
    exercises.append(loc)
  for item in indices1:
    loc = df0.iloc[item, 0]
    exercises.append(loc)
  print(exercises)
recommend(part)
