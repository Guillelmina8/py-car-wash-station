class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 average_rating: int, clean_power: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.average_rating = average_rating
        self.clean_power = clean_power
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            def calculate_washing_price() -> float:
                cost = (car.comfort_class
                        * (self.clean_power - car.clean_mark)
                        * self.average_rating
                        / self.distance_from_city_center)
                income: float = round(cost, 1)
                return income

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        self.average_rating = ((self.average_rating
                               * self.count_of_ratings + new_rate)
                               / (self.count_of_ratings + 1))
        self.count_of_ratings += 1
