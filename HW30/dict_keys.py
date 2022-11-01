class CustomClass:
    def __init__(self, a):
        self.a = a


obj_instance_1 = CustomClass(1)
obj_instance_2 = CustomClass(1)

test_dict = {
    obj_instance_1: "one",
    obj_instance_2: "two",
}

for key in test_dict:
    if key in [obj_instance_1, obj_instance_2]:
        print("match")
    else:
        print("no match")

print(test_dict[obj_instance_1])
print(test_dict[obj_instance_2])
