from fastapi import FastAPI

app = FastAPI()

places_kutch = [
    {
        "name": "Rann of Kutch",
        "description": "A vast salt marsh known for its stunning white landscape, especially during the Rann Utsav, offering cultural performances, camel safaris, and traditional handicrafts.",
        "budget": "₹1000 - ₹3000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹2000 - ₹5000 (round trip by bus or taxi)."
    },
    {
        "name": "Kala Dungar (Black Hill)",
        "description": "The highest point in Kutch offering panoramic views of the Rann of Kutch, the Indo-Pak border, and surrounding villages.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Bhuj",
        "description": "The main town of Kutch district, known for its historic monuments, colorful markets, and vibrant culture, including the Aina Mahal, Prag Mahal, and Swaminarayan Temple.",
        "budget": "₹500 - ₹2000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹1000 - ₹3000 (round trip by bus or taxi)."
    },
    {
        "name": "Mandvi Beach",
        "description": "A serene coastline with golden sands, calm waters, and water sports activities, along with attractions like the Vijay Vilas Palace and Shipbuilding Yard.",
        "budget": "₹500 - ₹2000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Dholavira",
        "description": "An ancient Harappan archaeological site known for its well-preserved ruins, including the Great Rann of Kutch, signifying the Indus Valley Civilization.",
        "budget": "₹1000 - ₹3000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹2000 - ₹5000 (round trip by taxi or bus)."
    },
    {
        "name": "Narayan Sarovar",
        "description": "A sacred lake and pilgrimage site surrounded by temples, ghats, and wildlife, offering spiritual solace and scenic beauty.",
        "budget": "₹500 - ₹2000 per person (including transportation and offerings).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Chhari Dhand Bird Sanctuary",
        "description": "A wetland habitat for migratory birds like flamingos, pelicans, and cranes, ideal for birdwatching and nature walks.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Kutch Desert Wildlife Sanctuary",
        "description": "Home to endangered species like the Indian Wild Ass, desert fox, and various migratory birds, offering jeep safaris and nature trails.",
        "budget": "₹500 - ₹2000 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Lakhpat Fort",
        "description": "A historic fortification on the India-Pakistan border, offering panoramic views of the Rann of Kutch and the Arabian Sea.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Banni Grasslands Reserve",
        "description": "A unique ecosystem known for its biodiversity, including migratory birds, Indian Wild Ass, and indigenous communities practicing traditional crafts.",
        "budget": "₹500 - ₹2000 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Aina Mahal",
        "description": "A historic palace in Bhuj known for its exquisite mirror work, European-style architecture, and royal artifacts, offering insights into Kutchi craftsmanship.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Prag Mahal",
        "description": "A majestic palace in Bhuj known for its Gothic-style architecture, grand interiors, and panoramic views of the city from its bell tower.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Wild Ass Sanctuary",
        "description": "A protected area known for its population of Indian Wild Ass, along with birdwatching opportunities and scenic landscapes.",
        "budget": "₹500 - ₹2000 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Khavda Village",
        "description": "A traditional village in Kutch known for its handicrafts, embroidery, and traditional mud houses, offering insights into rural Kutchi life and culture.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Dhordo Village",
        "description": "The gateway to the Rann of Kutch during the Rann Utsav, offering cultural performances, handicraft stalls, and traditional Gujarati cuisine.",
        "budget": "₹100 - ₹500 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Rann of Kutch Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places_kutch[place_id - 1]

@app.get("/places")
def read_all_places():
    return {"places": places_kutch}
