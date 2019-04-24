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
