from fastapi import FastAPI

app = FastAPI()

places_Manali = [
    {
        "name": "Hadimba Devi Temple",
        "description": "A wooden temple dedicated to Goddess Hadimba, surrounded by cedar forests and offering serene surroundings for meditation and prayer.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Solang Valley",
        "description": "A popular destination for adventure sports like skiing, paragliding, and zorbing, offering panoramic views of snow-capped peaks and lush green meadows.",
        "budget": "₹500 - ₹2000 per person per day (including transportation, activities, food, and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Rohtang Pass",
        "description": "A high mountain pass on the eastern Pir Panjal Range, offering breathtaking views of glaciers, peaks, and valleys, along with opportunities for snow activities.",
        "budget": "₹1000 - ₹3000 per person (including transportation, entry fees, and snacks).",
        "travel_expense": "₹2000 - ₹5000 (round trip by bus or taxi)."
    },
    {
        "name": "Old Manali",
        "description": "A quaint village known for its narrow lanes, rustic cafes, and hippie vibe, offering a glimpse into the traditional way of life in the mountains.",
        "budget": "₹500 - ₹2000 per person per day (including transportation, food, shopping, and accommodation).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Manu Temple",
        "description": "Dedicated to Sage Manu, believed to be the creator of human race, offering panoramic views of the Beas River and surrounding mountains.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Vashisht Temple and Hot Springs",
        "description": "Dedicated to Sage Vashisht, known for its natural hot springs believed to have medicinal properties, perfect for relaxation and rejuvenation.",
        "budget": "₹100 - ₹500 per person (including transportation, offerings, and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Jogini Falls",
        "description": "A scenic waterfall located near Vashisht Village, surrounded by lush greenery and offering a refreshing escape from the city.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Beas River",
        "description": "Offers opportunities for river rafting, fishing, and picnics along its pristine banks, surrounded by towering mountains and lush forests.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Manali Sanctuary",
        "description": "Home to diverse flora and fauna, including Himalayan black bears, snow leopards, and deodar trees, offering opportunities for wildlife spotting and nature walks.",
        "budget": "₹100 - ₹500 per person (including transportation and entry fees).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Nehru Kund",
        "description": "A natural spring named after Jawaharlal Nehru, offering pristine waters and serene surroundings amidst pine forests.",
        "budget": "₹50 - ₹200 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Gulaba",
        "description": "A scenic spot on the way to Rohtang Pass, offering panoramic views of snow-capped peaks, lush valleys, and opportunities for snow activities.",
        "budget": "₹500 - ₹2000 per person per day (including transportation, activities, food, and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Manali Nature Park",
        "description": "A biodiversity hotspot with a variety of flora and fauna, walking trails, and viewpoints offering stunning vistas of the surrounding mountains.",
        "budget": "₹100 - ₹500 per person (including transportation and entry fees).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Bijli Mahadev Temple",
        "description": "Dedicated to Lord Shiva, located atop a hill offering panoramic views of Kullu Valley and the Beas River, accessible by a scenic trek.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Manali Club House",
        "description": "A recreational center offering indoor games, boating, and adventure activities, perfect for family outings and relaxation.",
        "budget": "₹100 - ₹500 per person (including transportation, entry fees, and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Manali Gompa (Himalayan Nyingmapa Buddhist Temple)",
        "description": "A Tibetan monastery known for its colorful murals, prayer wheels, and serene ambiance, offering a peaceful retreat for meditation and contemplation.",
        "budget": "₹50 - ₹200 per person (including transportation and offerings).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Manali Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places_Manali[place_id - 1]

@app.get("/places")
def read_all_places():
    return { "places":places_Manali}
