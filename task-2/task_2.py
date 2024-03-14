def get_cats_info(path):
    with open(path, "r",) as file_cats:
        content = file_cats.readlines()
    for cat in content:
        id_, name,age = cat.split(",")
            cats.append({"id": id_, "name": name, "age": age.strip()}) 
    return cats

file_path = r"F:\PythonCourse\Repositories\homework_m4-1\task-2\cats.txt"

    

