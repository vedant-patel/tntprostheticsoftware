from control import Control
from constants import *
import random

class MockModel:
    def __init__(self):
        self.states = [OPEN, INDEX, MIDDLE, RING, PINKY, CLENCHED]
        self.controller = Control()
    def run(self):
        while True:
            state_ind =random.randint(0, len(self.states)-1)
            state = self.states[state_ind]
            self.controller.run(state)

if __name__ == '__main__':
    model = MockModel()
    model.run()