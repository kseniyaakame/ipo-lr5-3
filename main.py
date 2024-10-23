with open("text.txt", "r") as file: 
  s = file.read().split() 
print(f"Количество слов в файле: {len(s)}")