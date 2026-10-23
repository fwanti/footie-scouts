from footie_scouts.data_extraction.competitions import get_competitions

def competitions_transformation():
    response = get_competitions()
    competitions = []
    competitions = []
    for competition in response:
            item = (
                competition['id'],                
                competition['name'],
                competition['area']['name'],
                competition['lastUpdated']

            )   
                 
            if item not in competitions:
                competitions.append(item)
