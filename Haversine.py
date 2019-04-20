import math

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
        a1, b1 = source
        a2, b2 = destination
        
        radius = 6371 # km

        da = math.radians(a2-a1)
        db = math.radians(b2-b1)
