class Gene:
    def __init__(self, drone_ID, action, action_parameter = 0):
        self.drone_ID = drone_ID
        self.action = action
        self.action_parameter = action_parameter