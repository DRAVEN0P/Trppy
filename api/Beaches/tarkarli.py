from fastapi import FastAPI

app = FastAPI()

places_tarkarli = [
    {
        "name": "Tarkarli Beach",
        "description": "Known for its pristine waters and water sports activities.",
        "budget": "INR 1500 - INR 3000 per day for accommodation and food."
    },
    {
        "name": "Devbagh Beach",
        "description": "Serene and less crowded with options for boat rides and dolphin spotting.",
        "budget": "INR 1200 - INR 2500 per day for accommodation and food."
    },
    {
        "name": "Sindhudurg Fort",
        "description": "Historic sea fort offering panoramic views of the Arabian Sea.",
        "budget": "Entrance fee around INR 50, accommodation and food budget separate."
    },
    {
        "name": "Malvan",
        "description": "Famous for Malvani cuisine, historic forts, and beautiful beaches.",
        "budget": "INR 1000 - INR 2500 per day for accommodation and food."
    },
    {
        "name": "Devbagh Sangam Point",
        "description": "Confluence of the Karli River and Arabian Sea, offering scenic views.",
        "budget": "INR 500 - INR 1000 per day for accommodation and food."
    },
    {
        "name": "Rock Garden",
        "description": "Natural garden with unique rock formations near Malvan.",
        "budget": "INR 500 - INR 1000 per day for accommodation and food."
    },
    {
        "name": "Tsunami Island",
        "description": "Small island offering water sports activities like jet skiing and banana boat rides.",
        "budget": "INR 1000 - INR 2000 per day for accommodation and food."
    },
    {
        "name": "Vengurla Beach",
        "description": "Picturesque beach known for its golden sand and clear waters.",
        "budget": "INR 1500 - INR 3000 per day for accommodation and food."
    },
    {
        "name": "Sagareshwar Wildlife Sanctuary",
        "description": "Home to diverse flora and fauna, ideal for nature walks.",
        "budget": "INR 500 - INR 1500 per day for accommodation and food."
    },
    {
        "name": "Karli Backwaters",
        "description": "Serene backwaters for boat rides and bird watching.",
        "budget": "INR 1000 - INR 2000 per day for accommodation and food."
    },
    {
        "name": "Nivati Beach",
        "description": "Pristine beach with rocky terrain, ideal for solitude seekers.",
        "budget": "INR 1000 - INR 2500 per day for accommodation and food."
    },
    {
        "name": "Tondavali Beach",
        "description": "Peaceful beach offering stunning sunset views.",
        "budget": "INR 1500 - INR 3000 per day for accommodation and food."
    },
    {
        "name": "Dhamapur Lake",
        "description": "Serene lake surrounded by lush greenery, perfect for a leisurely picnic.",
        "budget": "INR 500 - INR 1500 per day for accommodation and food."
    },
    {
        "name": "Achara Beach",
        "description": "Secluded beach known for its tranquil atmosphere.",
        "budget": "INR 1000 - INR 2000 per day for accommodation and food."
    },
    {
        "name": "Bhogwe Beach",
        "description": "Scenic beach with golden sands and coconut trees.",
        "budget": "INR 1500 - INR 3000 per day for accommodation and food."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tarkarli Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places_tarkarli[place_id - 1]

@app.get("/places_tarkarli/")
def read_all_places():
    return {"places": places_tarkarli}
