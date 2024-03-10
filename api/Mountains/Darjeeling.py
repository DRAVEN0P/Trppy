from fastapi import FastAPI

app = FastAPI()

places_darjeeling = [
    {
        "name": "Tiger Hill",
        "description": "Famous for its panoramic views of the sunrise over the Himalayas, offering breathtaking vistas of Mount Kanchenjunga and surrounding peaks.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Darjeeling Himalayan Railway (Toy Train)",
        "description": "A UNESCO World Heritage Site, offers a scenic journey through the mountains, tea gardens, and picturesque landscapes.",
        "budget": "₹100 - ₹500 per person (including train ride and snacks).",
        "travel_expense": "₹500 - ₹1000 (round trip by toy train or taxi)."
    },
    {
        "name": "Batasia Loop and War Memorial",
        "description": "A spiral railway track offering stunning views of the surrounding mountains, along with a War Memorial honoring Gorkha soldiers.",
        "budget": "₹50 - ₹200 per person (including transportation and snacks).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Peace Pagoda (Japanese Temple)",
        "description": "A symbol of peace and harmony, offering serene surroundings, panoramic views of Darjeeling, and a tranquil ambiance for meditation.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Padmaja Naidu Himalayan Zoological Park",
        "description": "Known for its conservation efforts and housing rare Himalayan species like the Red Panda and Snow Leopard.",
        "budget": "₹100 - ₹500 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Darjeeling Ropeway (Rangeet Valley Cable Car)",
        "description": "Offers breathtaking aerial views of the valley, tea gardens, and mountains, providing an unforgettable experience for visitors.",
        "budget": "₹100 - ₹500 per person (including ropeway ride and snacks).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Himalayan Mountaineering Institute (HMI)",
        "description": "A renowned mountaineering institute founded by Tenzing Norgay, offering mountaineering courses, museum exhibits, and insights into Himalayan expeditions.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Darjeeling Mall Road",
        "description": "A bustling street lined with shops, cafes, and restaurants, offering a lively atmosphere and stunning views of the surrounding hills.",
        "budget": "₹100 - ₹500 per person (including transportation, shopping, food, and snacks).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Rock Garden",
        "description": "A terraced garden with waterfalls, rock sculptures, and colorful flowers, offering a peaceful retreat amidst nature.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Observatory Hill and Mahakal Temple",
        "description": "Offers panoramic views of Darjeeling and the Himalayas, along with the Mahakal Temple dedicated to Lord Shiva.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Happy Valley Tea Estate",
        "description": "Offers guided tours of tea gardens, tea processing units, and tea tasting sessions, providing insights into the tea-making process.",
        "budget": "₹100 - ₹500 per person (including entry fees, transportation, and tea tasting).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Tenzing and Gombu Rock",
        "description": "Offers opportunities for rock climbing and rappelling, along with stunning views of the surrounding mountains and valleys.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Chowrasta (The Mall)",
        "description": "A popular public square in Darjeeling, offering panoramic views, street performances, and a vibrant atmosphere.",
        "budget": "₹100 - ₹500 per person (including transportation, shopping, food, and snacks).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Bengal Natural History Museum",
        "description": "Showcases the rich biodiversity of the region through exhibits of flora, fauna, and geological specimens.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Bhutia Busty Monastery (Karma Dorjee Chyoling Monastery)",
        "description": "A serene Buddhist monastery known for its colorful frescoes, prayer wheels, and peaceful ambiance for meditation.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Manali Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places_darjeeling[place_id - 1]

@app.get("/places")
def read_all_places():
    return {"places": places_darjeeling}
