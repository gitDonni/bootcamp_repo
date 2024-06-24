#1

class Factory:
    def engine(self):
        return 'Двигатель создан'

    def bridge(self):
        return 'Ходовая часть создана'

my_factory = Factory()
# engine_result = my_factory.engine()
# bridge_result = my_factory.bridge()
#
#
# print(engine_result)
# print(bridge_result)


#2

class Toyota(Factory):
  def wheels(self):
      return 'Колеса готовы'

  def windows(self):
      return 'Стекла готовы'


new_toyota = Toyota()

my_list = []
my_list.append(new_toyota.engine())
my_list.append(new_toyota.bridge())
my_list.append(new_toyota.wheels())
my_list.append(new_toyota.windows())

print(my_list)

#3


class Zoo:
    def __init__(self):
        self.animal_1 = 'Тигр'
        self.animal_2 = 'Бегемот'
        self.animal_3 = 'Жираф'


my_zoo = Zoo()

my_zoo.animal_1 = 'Лев'

my_zoo.animal_4 = [my_zoo.animal_2, my_zoo.animal_3]

my_zoo.animal_3 = 'Змея'

print(my_zoo.animal_1)
print(my_zoo.animal_2)
print(my_zoo.animal_3)
print(my_zoo.animal_4)