# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, station:str):
        self.__station = station
        self.__obs_lst = []


    def add_observation(self, observation: str):
        self.__obs_lst.append(observation)

    def latest_observation(self):
        if len(self.__obs_lst) == 0:
            return self.__str__()

        else: return self.__obs_lst[-1]

    def number_of_observations(self):
        
         return len(self.__obs_lst)

    def __str__(self):
        obs = "observations"
        
        return f"{self.__station}, {len(self.__obs_lst)} {obs}"

if __name__=="__main__":
    a=WeatherStation("Kumpula")
    m=a.latest_observation()
    print(m)