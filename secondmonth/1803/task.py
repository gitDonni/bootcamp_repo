class Laptop:
    def __init__(self, model):
        self.model = model
        self.specs = {}

    def add_processor(self, processor):
        self.specs["Процессор"] = processor

    def add_ram(self, ram):
        self.specs["Оперативная Память"] = ram

    def add_graphics_card(self, graphics_card):
        self.specs["Видео карта"] = graphics_card

    def add_hard_drive(self, hard_drive):
        self.specs["Жёсткий Диск"] = hard_drive

    def add_motherboard(self, motherboard):
        self.specs["Материнская плата"] = motherboard

    def add_screen_size(self, screen_size):
        self.specs["Размер экрана"] = screen_size

    def get_specs(self):
        return {"Модель Ноутбука": self.model, "Характеристики": self.specs}


my_laptop = Laptop(model='Lenovo')
my_laptop.add_processor('AMD Ryzen 5')
my_laptop.add_ram('16 GB')
my_laptop.add_graphics_card('Ryzen Vega')
my_laptop.add_hard_drive('256 gb ssd')
my_laptop.add_motherboard('Какая-то плата')
my_laptop.add_screen_size('14"')

laptop_specs = my_laptop.get_specs()
print(laptop_specs)
