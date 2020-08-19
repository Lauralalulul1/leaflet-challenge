json_items = json_data[“data”][“items”]
for item in json_items:
    print(“title”, item[“title”])
    print(“rating”, item[‘rating’])
    print(“thumbnail” , item[‘thumbnail’][‘hqDefault’])
    print(“views”,item[‘viewCount’])