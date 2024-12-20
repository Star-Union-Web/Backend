def parse_data(data):
    parsed_data = []
    for item in data:
        temp_dict = {}
        temp_dict["type"] = item["type"]
        temp_dict["name"] = item["name"]
        temp_dict["country"] = item["country"]
        temp_dict["age"] = item["age"]
        temp_dict["date"] = item["date"]
        parsed_data.append(temp_dict)
    return parsed_data
    
