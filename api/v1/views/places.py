                    for place in all_places:
                        if place.id in places_id:
                            continue
                        if place.city_id == city.id:
                            new_places.append(place)
                places.extend(new_places)
    del places_id
    if all([not keys_status[0], not keys_status[1]]) or not data:
        places = all_places
    if keys_status[2]:
        amenity_ids = []
        for amenity_id in data['amenities']:
            if not amenity_id:
                continue
            amenity = storage.get(Amenity, amenity_id)
            if amenity and amenity.id not in amenity_ids:
                amenity_ids.append(amenity.id)
        del_indices = []
        for place in places:
            place_amenities_ids = list(map(lambda x: x.id, place.amenities))
            if not amenity_ids:
                continue
            for amenity_id in amenity_ids:
                if amenity_id not in place_amenities_ids:
                    del_indices.append(place.id)
                    break
        places = list(filter(lambda x: x.id not in del_indices, places))
    result = []
    for place in places:
        obj = place.to_dict()
        if 'amenities' in obj:
            del obj['amenities']
        result.append(obj)
    return jsonify(result)
