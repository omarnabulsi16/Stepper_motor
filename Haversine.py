#libraries
import math

#distance function
def setDistance(source, destination):
        '''
        Description:
            Haversine formula - Calculates and sets self.__distance (in cm) given self.__gps 
            and self.__nextWaypoint
        Args:
            None
        Returns:
            Nothing
        '''
        
        #initialization of destination and initial and final coordinates
        a1, b1 = source
        a2, b2 = destination
        
        #radius of Earth
        radius = 6371 # km
        
        #math formulas to calculate the distance between 2 coordinates
        da = math.radians(a2-a1)
        db = math.radians(b2-b1)
        a = math.sin(da/2) * math.sin(da/2) + math.cos(math.radians(a1)) \ 
                * math.cos(math.radians(a2)) * math.sin(db/2) * math.sin(db/2)
        
        #calculate the radius and distance traveled
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
              
        #conversion
        return d * 100000

#target destination function
def setTargetHeading(source, destination):
        '''
        Description:
            Code adapted from https://gist.github.com/jeromer
            Calculates and sets self.__targetHeading given self.__gps and self.__nextWaypoint
        Args:
            None
        Returns:
            Nothing
        '''
        
        #sequencing objects
        if (type(source) != tuple) or (type(destination) != tuple) :
                #raise TypeError
                print("Only tuples allowed")
        
        #setting latitude variables
        lat1 = math.radians(source[0])
        lat2 = math.radians(destination[0])
        
        #setting the longitude as x and y variables
        diffLong = math.radians(destination[1] - source[1])
        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                * math.cos(lat2) * math.cos(diffLong))
        
        #more calculations to convert the GPS coorinates to directional headings
        initial_heading = math.atan2(x, y)
        initial_heading = math.degrees(initial_heading)
        compass_heading = (initial_heading + 360) % 360
        
        #returns compass heading directional angle
        return compass_heading
