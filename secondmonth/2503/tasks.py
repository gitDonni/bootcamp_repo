#2
# class Hotels:
#     def __init__(self, data):
#         self.markers = data.get('MARKERS', [])
#
#     def get_names(self):
#         return [marker.get('NAME') for marker in self.markers]
#
#     def get_name_location(self):
#         names = tuple(marker.get('NAME') for marker in self.markers)
#         locations = tuple(marker.get('LOCATION') for marker in self.markers)
#         return {'names': names, 'locations': locations}
#
#     def add_status(self):
#         for marker in self.markers:
#             marker['status_id'] = 1
#
#
# data = {
#     "MARKERS": [
#         {
#             "NAME": "RIXOS THE PALM DUBAI", "LOCATION": [25.1212, 55.1535]
#         },
#         {
#             "NAME": "SHANGRI-LA HOTEL", "LOCATION": [25.2084, 55.2719]
#         },
#         {
#             "NAME": "GRAND HYATT", "LOCATION": [25.2285, 55.3273]
#         }]
# }
#
#
# hotels = Hotels(data)
#
# print('Hotel NAME:', hotels.get_names())
# print('Name and Location: ', hotels.get_name_location())
#
# hotels.add_status()
# print('new data: ', data)




#2


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
