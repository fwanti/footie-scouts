from footie_scouts.data_extraction.areas import get_areas

def areas_transformation():
    response = get_areas()
    areas = []
    for area in response:
        item = (
            area['id'],             
            area['name'],
            area['parentArea'],
            area['parentAreaId']
        )

        if item not in areas:
            areas.append(item)
    for i in areas: print(i)
