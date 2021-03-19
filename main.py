birth_doc = open("US_births_2000-2014.csv","r",encoding= "utf-8")

f = birth_doc.read()

birth_split = f.split("\n")

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

us_birth_list = read_csv("US_births_2000-2014.csv")


#Calculer le nombre de naissances par mois
def month_birth(list):
  births_per_month = {}

  for li in list:
    month = li[1]
    births = li[4]
    if month in births_per_month:
      births_per_month[month] += births
    else:
      births_per_month[month] = births
  
  return(births_per_month)




us_month_births = month_birth(us_birth_list)

print(us_month_births)


