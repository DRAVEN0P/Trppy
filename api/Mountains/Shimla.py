# from fastapi import FastAPI

# app = FastAPI()

places_shimla = [
    {
        "name": "Mall Road",
        "budget": "₹500 - ₹2000 per person per day",
        "travel_expense": "₹500 - ₹1500 (round trip by bus or taxi)",
        "description": "Mall Road is the main street in Shimla, lined with shops, restaurants, and cafes, offering stunning views of the surrounding mountains and colonial architecture.",
        "Image_link": "https://wehimachali.com/wp-content/uploads/2023/08/Shimla-Mall-Road-01.png"
    },
    {
        "name": "The Ridge",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "The Ridge is a spacious open area in the heart of Shimla, offering panoramic views of the Himalayas, perfect for leisurely walks and enjoying the sunset.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2jqNDAV1cxqf6XPVLUSJQCLhZdXXf9P9LUw&usqp=CAU"
    },
    {
        "name": "Jakhu Temple",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Jakhu Temple is dedicated to Lord Hanuman and is located atop Jakhu Hill, offering breathtaking views of Shimla and surrounding hills.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8mnWPy8q0-7wDOqPs8V8GUVS5JHWYyMlqhQ&usqp=CAU"
    },
    {
        "name": "Kufri",
        "budget": "₹500 - ₹2000 per person per day",
        "travel_expense": "₹1000 - ₹2000 (round trip by bus or taxi)",
        "description": "Kufri is a small hill station near Shimla known for its picturesque landscapes, adventure activities like skiing and tobogganing, and the Himalayan Nature Park.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStrL3C9PZZ9CysSw4sWQOIgR9OqybcZcDjhw&usqp=CAU"
    },
    {
        "name": "Christ Church",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Christ Church is a historic church located on the Ridge in Shimla, known for its neo-Gothic architecture and beautiful stained glass windows.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsZhD8DgLMVHpxv6zLlnbnshBUPzSo6f1fcg&usqp=CAU"
    },
    {
        "name": "Summer Hill",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Summer Hill is a scenic hill station on the outskirts of Shimla, offering lush greenery, peaceful surroundings, and panoramic views of the Himalayas.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTm0EqbxnknKjnQbQGgjQvtQEfS6idUxg4Tzw&usqp=CAU"
    },
    {
        "name": "Chadwick Falls",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Chadwick Falls is a picturesque waterfall located near Shimla, surrounded by dense forests and offering a tranquil retreat from the city.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkvcReV7T2RVlIQGQvcnHbToiFA6CSr8aP_A&usqp=CAU"
    },
    {
        "name": "Indian Institute of Advanced Study (IIAS)",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "IIAS is housed in the former Viceregal Lodge, offering insights into India's colonial history and a serene setting amidst pine forests.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuoOkjYuY6Ir8oH_aNJ3JLqBbLSiaHqXrOAw&usqp=CAU"
    },
    {
        "name": "Annandale",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Annandale is a scenic flat terrain near Shimla, offering opportunities for picnics, golfing, and enjoying panoramic views of the surrounding mountains.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEjOt1ulkmcVl-rA201FxQeB4YJBlVYMEMpQ&usqp=CAU"
    },
    {
        "name": "Tara Devi Temple",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Tara Devi Temple is a revered Hindu temple located on a hilltop near Shimla, offering spiritual solace and panoramic views of the valley below.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu_Jlm4_0EqqlpxuZrBBgqYXQjrlPKtl8iJA&usqp=CAU"
    },
    {
        "name": "Viceregal Lodge (Rashtrapati Niwas)",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Viceregal Lodge is a historic building in Shimla, formerly the residence of the British Viceroy, now housing the Indian Institute of Advanced Study.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq4Ixk-Ij8crzHkIlsMcjC7QpiyvHG5bOxww&usqp=CAU"
    },
    {
        "name": "Shaily Peak",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Shaily Peak offers panoramic views of the surrounding mountains and valleys, accessible by a short trek from Kufri.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDH7gyu7S3vH8-K0chHKvzxTM1hBiTHjU_pQ&usqp=CAU"
    },
    {
        "name": "Gaiety Theatre",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by bus or taxi)",
        "description": "Gaiety Theatre is a historic landmark in Shimla, known for its Victorian architecture and hosting cultural events and performances.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYHcyH_uCoQWUx71psYJGrIIlD3rsdK_KtJg&usqp=CAU"
    },
    {
        "name": "Tattapani Hot Springs",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹1000 - ₹2000 (round trip by bus or taxi)",
        "description": "Tattapani Hot Springs is a natural thermal spring located near Shimla, known for its therapeutic properties and scenic surroundings along the Sutlej River.",
        "Image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-IfCYdUgyPl-HCR5QZllZq0CPuV6AtFWZuQ&usqp=CAU"
    }
]
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Shimla Places API"}

# @app.get("/places/{place_id}")
# def read_place(place_id: int):
#     return places_shimla[place_id - 1]

# @app.get("/places")
# def read_all_places():
#     return { "places":places_shimla}
