file = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""

with open ('cats_file.txt', 'w', encoding='utf-8') as f:
 f.write(file)

def get_cats_info(path):
    cats_info = []
    try:
       with open(path, 'r', encoding='utf-8') as file:
          for line in file:
             cat_id, name, age = line.strip().split(',')
             cat_dict = {
                "id": cat_id,
                "name": name,
                "age": int(age)
             }
             cats_info.append(cat_dict)
    except FileNotFoundError:
          print(f"File {path} not found")
          return None
    except Exception as e:
          print(f"An error occured: {e}")
          return None
    return cats_info
cats_data = get_cats_info('cats_file.txt') 
if cats_data is not None:
    for cat in cats_data:
     print(cat)

