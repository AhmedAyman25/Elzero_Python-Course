my_list = [1,2,3,4,5]
my_dic = {"name":"Ahmed", "age":24, "countr":"Egypt"}

for item in my_list:
    print(item)

for key, value in my_dic.items():
    print(f"{key} => {value}")

def say_hello():
    print("hello")

say_hello()