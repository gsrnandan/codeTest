""" Defines a tracker class for tracking the input temperatures

"""

class TempTracker(object):
	""" Temperature Tracker Class

	"""

	minimumTemperature = 0
	maximumTemperature = 110
	
	def __init__(self):
		
		# A list to store the input temperature values
		self._temperatureTrackerList = []

	def is_valid(self, temperature):
	    """ Method to validate the input temperature type and range
		 	
		 	This method reads the input value and checks if the temperature is within the
		 	range of (0-110) and if its a valid int type
		 		
		 	Args:
		     	temperature (int): The temperature value that is to be validated
		     	
		 	Return:
		     	(bool): Returns True if its a valid input, if not raises an Error
		 
	    """
	    if isinstance(temperature, int):
	    	if (temperature >= TempTracker.minimumTemperature) and (temperature <= TempTracker.maximumTemperature):
	    		return True
	    	else:
	    		raise ValueError("Value out of range")
	    else:
	    	raise TypeError("Element {0} has unsupported type ({1})".format(temperature,type(temperature).__name__))

	def insert(self, *temperatures):
		""" Method to insert a new temperature into the existing list of temperatures
			
			This function takes a tuple/int argument and adds it to the tempTrackerList
			after validation
			    
			Args:
			    temperatures (tuple): List of temperatures 
		"""
		self._temperatureTrackerList.extend([temperature for temperature in temperatures if self.is_valid(temperature)]
			)

	def get_max(self):
		""" Method to return the maximum of all the temperatures in the Tracker
				
			This function will return the max of temperatureTrackerList
			   
			Return:
				(int): The maximum value in the list of temperatures, None if the list is empty
		"""
		if self._temperatureTrackerList:
			return max(self._temperatureTrackerList)

	def get_min(self):
		""" Method to return the minimum of all the temperatures in the Tracker
				
			This function will return the min of temperatureTrackerList 
			      
			Return:
				(int): The minimum value in the list of temperatures, None if the list is empty
		"""		
		if self._temperatureTrackerList:
			return min(self._temperatureTrackerList)

	def get_mean(self):
		""" Method to return the mean of all the temperatures tracked
				
			This function will calculate the average of all integer values inside the temperatureTrackerList. 
			      
			Return:
				(float): Returns the average of all the temperatures in the list of temperatures. None if the list is empty
		"""
		if self._temperatureTrackerList:
			noOfElements = len(self._temperatureTrackerList)
			sumOfElements = float(sum(self._temperatureTrackerList))
			return sumOfElements / noOfElements


if __name__ == '__main__':
    tt = TempTracker()
    tt.insert(33)
    print tt.get_mean()
    print tt.get_max()
    print tt.get_min()