birth_doc = open("US_births_2000-2014.csv","r",encoding= "utf-8")

f = birth_doc.read()

birth_split = f.split("\n")

print(birth_split[0:10])

def read_csv(file):
  f = open(file,"r")
  string_list = f.read()
  string_list = string_list.split("\n")
  string_list = string_list[1:]

  final_list = []
  
  for rows in string_list :
    int_fields = []
    string_fields = rows.split(",")
    for rows in string_fields:
      int_fields.append(int(rows))
    
    final_list.append(int_fields)

  return final_list


birth_list = read_csv("US_births_2000-2014.csv")

print(birth_list[0:10])