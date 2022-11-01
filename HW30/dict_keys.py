class CustomClass:
    def __init__(self, a):
        self.a = a


obj_instance_1 = CustomClass(1)
obj_instance_2 = CustomClass(2)

test_dict = {
    obj_instance_1: "one",
    obj_instance_2: "two",
}

for key in test_dict:
    if key in [obj_instance_1, obj_instance_2]:
        print("match")

print(test_dict[obj_instance_1])
print(test_dict[obj_instance_2])


# print(test_dict[CustomClass(2)])  # Так буде помилка


class CustomClass_2:
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return self.a is other.a

    def __hash__(self):
        return hash(self.a)


obj_instance = CustomClass_2(1)

test_dict = {
    CustomClass_2(1): "one",
    CustomClass_2(2): "two",

}

for key in test_dict:
    if key == obj_instance:
        print("match")

print(test_dict[obj_instance])
print(test_dict[CustomClass_2(2)])
