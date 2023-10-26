import pandas as pd

data = pd.read_json(r'response.json')

# Use json_normalize to flatten the JSON data
# df = pd.json_normalize(data, record_path=['street'], meta=[
#     'district_code', 'district_name', 'city_code', 'city_name', 'area_code', 'area_name'
# ])

# Convert the DataFrame to a list of dictionaries
data_list = data.to_dict(orient='records')

# Initialize an empty list to store flattened data
flattened_data = []

# Iterate through the JSON data and flatten it
for item in data_list:
    district_code = item["district_code"]
    district_name = item["district_name"]
    city_code = item["city_code"]
    city_name = item["city_name"]
    area_code = item["area_code"]
    area_name = item["area_name"]

    if item["street"] and len(item["street"]) > 0:
        for street_item in item["street"]:
            street_code = street_item["street_code"]
            street_name = street_item["street_name"]

            flattened_data.append({
                "district_code": district_code,
                "district_name": district_name,
                "city_code": city_code,
                "city_name": city_name,
                "area_code": area_code,
                "area_name": area_name,
                "street_code": street_code,
                "street_name": street_name
            })  

# Create a DataFrame from the flattened data
df = pd.DataFrame(flattened_data)

# Print the resulting DataFrame
print(df)

df.to_excel(r'data.xlsx', index=False)
