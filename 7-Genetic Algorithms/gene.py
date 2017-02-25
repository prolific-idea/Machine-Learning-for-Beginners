class Gene:
    def __init__(self, drone_ID, action, action_parameter=None):
        self.drone_ID = drone_ID
        self.action = action
        self.action_parameter = action_parameter
