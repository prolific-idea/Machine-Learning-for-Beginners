from domain.delivery import Delivery

class SimulationMap:
    def __init__(self, simulation_map, warehouse_items, delivery_items):
        self.simulation_map = simulation_map
        self.warehouse_items = warehouse_items
        self.delivery_items = delivery_items

    def get_number_of_orders(self):
        number_of_orders = 0
        for row in self.simulation_map:
            for element in row:
                if isinstance(element, Delivery):
                    number_of_orders += sum(element.orders.values())
        return number_of_orders
