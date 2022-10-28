import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for r in range(value):
        self.contents.append(key)
      
  def draw (self, number):
    removed_balls = []
    if number > len(self.contents):
      return self.contents
    for r in range(number):
      decision = random.randrange(len(self.contents))
      removed_balls.append(self.contents.pop(decision))
            
    return removed_balls
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for r in range(num_experiments):
      expected = copy.deepcopy(expected_balls)
      hat_copy = copy.deepcopy(hat)
      colors = hat_copy.draw(num_balls_drawn)

  for c in colors:
      if c in expected:
        expected[c]-=1
  
  if(all(x <= 0 for x in expected.values())):
      count += 1
    #amount of successful draws/ total amount of draws
  return count /num_balls_drawn
