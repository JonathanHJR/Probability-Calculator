import copy # to use modules, classes (unlike functions = .function()), do module.themodule(). For copy module, there is shallow copy.copy() and deep copy.deepcopy(). Shallow copy does reference back to the original content and changes are made, shallow only makes changes to the unoriginal copy version.
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs): # *args for non keyworded, **kwargs for keyworded arguments and creates a list for however many arguments passed with key values. 
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value): # for each number of respective color.  
        self.contents.append(key) # append the respective number of times the color to contents variable.
  
  def draw(self, number):
    removed_balls = []
    if number > len(self.contents): # more than there are balls = draw all
      return self.contents
    for i in range(number): # for every number of the number passed
      remove = self.contents.pop(int(random.random() * len(self.contents))) # pop removes the repective indexed number and returns it. The removing is permanent after each loop and self.contents is reduced by 1. Random module picks a number between 0 - 1
      removed_balls.append(remove)
    return removed_balls # return all the balls that were popped

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
  count = 0 # for counting probability later on
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat) # using the original or shallow copying will not work because the original values will be changed and can't be used repeatedly for the experiment.
    expected_copy = copy.deepcopy(expected_balls)
    colors_drawn = hat_copy.draw(num_balls_drawn)
    for color in colors_drawn:
      if color in expected_copy:
        expected_copy[color] -= 1
    if all(x <= 0 for x in expected_copy.values()):
      count += 1
  return count / num_experiments