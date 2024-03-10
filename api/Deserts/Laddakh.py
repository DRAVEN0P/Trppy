from fastapi import FastAPI

app = FastAPI()

places_ladakh = [
    {
        "name": "Pangong Lake",
        "description": "A breathtaking high-altitude lake known for its azure blue waters, surrounded by barren mountains, and featured in several Bollywood movies.",
        "budget": "₹1000 - ₹3000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹5000 - ₹10000 (round trip by taxi or bus)."
    },
    {
        "name": "Nubra Valley",
        "description": "A stunning desert landscape with sand dunes, monasteries, and Bactrian camel safaris, offering a unique experience in the Himalayas.",
        "budget": "₹1000 - ₹3000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹5000 - ₹10000 (round trip by taxi or bus)."
    },
    {
        "name": "Leh Palace",
        "description": "A historic royal palace offering panoramic views of Leh town and the surrounding mountains, showcasing Tibetan architectural style.",
        "budget": "₹100 - ₹500 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Shanti Stupa",
        "description": "A Buddhist white-domed stupa offering stunning views of the Himalayas and a peaceful ambiance for meditation and prayer.",
        "budget": "₹50 - ₹200 per person (including transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Tso Moriri Lake",
        "description": "A remote high-altitude lake known for its clear blue waters, surrounded by snow-capped peaks and nomadic settlements.",
        "budget": "₹1000 - ₹3000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹5000 - ₹10000 (round trip by taxi or bus)."
    },
    {
        "name": "Hemis Monastery",
        "description": "The largest and wealthiest monastery in Ladakh, known for its annual Hemis Festival and impressive collection of Buddhist artifacts.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Khardung La Pass",
        "description": "One of the highest motorable passes in the world, offering panoramic views of the Karakoram Range and thrilling adventure for travelers.",
        "budget": "₹500 - ₹2000 per person (including transportation and snacks).",
        "travel_expense": "₹5000 - ₹10000 (round trip by taxi or bus)."
    },
    {
        "name": "Alchi Monastery",
        "description": "A UNESCO World Heritage Site known for its ancient wall paintings, sculptures, and unique Kashmiri-style architecture.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Diskit Monastery",
        "description": "The largest and oldest monastery in Nubra Valley, housing a giant statue of Maitreya Buddha and offering panoramic views of the valley.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Zanskar Valley",
        "description": "A remote and rugged region known for its stunning landscapes, monasteries, and trekking routes, offering a glimpse into traditional Ladakhi culture.",
        "budget": "₹1000 - ₹3000 per person per day (including transportation, accommodation, and food).",
        "travel_expense": "₹5000 - ₹10000 (round trip by taxi or bus)."
    },
    {
        "name": "Shey Palace and Shey Monastery",
        "description": "Once the summer capital of Ladakh, featuring a historic palace and monastery with ancient Buddhist statues and murals.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)."
    },
    {
        "name": "Likir Monastery",
        "description": "Known for its impressive Buddha statue, vibrant murals, and panoramic views of the surrounding mountains.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Lamayuru Monastery",
        "description": "One of the oldest and largest monasteries in Ladakh, perched on a hilltop overlooking the village and lunar-like landscapes.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Phyang Monastery",
        "description": "Known for its annual festival, ancient murals, and religious artifacts, offering insights into Tibetan Buddhism and Ladakhi culture.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    },
    {
        "name": "Spituk Monastery",
        "description": "Perched atop a hill overlooking the Indus Valley, housing ancient shrines, thangkas, and a giant statue of Kali.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ladakh Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places_ladakh[place_id - 1]

@app.get("/places")
def read_all_places():
    return {"places": places_ladakh}
