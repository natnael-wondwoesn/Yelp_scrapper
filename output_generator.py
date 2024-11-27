import csv


data = [
    [{'name': 'Fremont House', 'Phone': 'Business websitefremonthouseca.com', 'stars': '4.7 star rating', 
      'Address': '5030 Hwy 140 Mariposa, CA 95338', 'Number of Reviews': '12 reviews', 'Hours of Operation': '9:00 AM - 5:30 PM'}],
    [{'name': 'Northshore Boardwear', 'Phone': '(559) 642-3898', 'stars': '3.7 star rating', 
      'Address': '40034 Highway 49 Ste A6 Oakhurst, CA 93644', 'Number of Reviews': '7 reviews', 'Hours of Operation': '10:00 AM - 5:30 PM'}],
]

def convert_to_csv(raw_data, output_file="business_data.csv"):
    
    flattened_data = [item[0] for item in raw_data if item[0].get('name')]

    
    headers = ['Name', 'Phone', 'Stars', 'Address', 'Number of Reviews', 'Hours of Operation']

    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for entry in flattened_data:
            writer.writerow({
                'Name': entry.get('name', 'N/A'),
                'Phone': entry.get('Phone', 'N/A'),
                'Stars': entry.get('stars', 'N/A'),
                'Address': entry.get('Address', 'N/A'),
                'Number of Reviews': entry.get('Number of Reviews', 'N/A'),
                'Hours of Operation': entry.get('Hours of Operation', 'N/A')
            })

    print(f"Data successfully written to {output_file}")


convert_to_csv(data, "business_data.csv")
