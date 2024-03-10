from fastapi import FastAPI

app = FastAPI()

places = [
    {
        "name": "Promenade Beach",
        "budget": "₹300 - ₹1000 per person per day",
        "travel_expense": "₹100 - ₹500 (round trip, depending on distance)",
        "description": "Promenade Beach, also known as Rock Beach, is a popular destination for relaxing walks, beachside cafes, and beautiful sunsets."
    },
    {
        "name": "Paradise Beach",
        "budget": "₹500 - ₹1500 per person per day",
        "travel_expense": "₹200 - ₹500 (round trip, depending on distance)",
        "description": "Paradise Beach, accessible only by boat, offers pristine white sands, clear blue waters, and a tranquil atmosphere."
    },
    {
        "name": "Auroville",
        "budget": "₹300 - ₹1000 per person",
        "travel_expense": "₹200 - ₹500 (round trip by taxi or bus)",
        "description": "Auroville is an experimental township known for its spiritual community, sustainable living, and the Matrimandir, a golden-domed meditation center."
    },
    {
        "name": "Aurobindo Ashram",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Aurobindo Ashram is a spiritual retreat founded by Sri Aurobindo and The Mother, offering meditation sessions, yoga classes, and a peaceful ambiance."
    },
    {
        "name": "Botanical Garden",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Botanical Garden, also known as Jardin Botanique, is a lush green space featuring exotic plants, trees, and a serene ambiance for nature lovers."
    },
    {
        "name": "French Quarter (White Town)",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "French Quarter, or White Town, is a charming colonial district known for its French architecture, boutique cafes, and quaint streets."
    },
    {
        "name": "Serenity Beach",
        "budget": "₹300 - ₹1000 per person per day",
        "travel_expense": "₹100 - ₹500 (round trip, depending on distance)",
        "description": "Serenity Beach is a peaceful stretch of coastline offering surfing, swimming, and relaxation away from the hustle and bustle of the city."
    },
    {
        "name": "Manakula Vinayagar Temple",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Manakula Vinayagar Temple is a historic Hindu temple dedicated to Lord Ganesha, known for its colorful architecture and religious rituals."
    },
    {
        "name": "Pondicherry Museum",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Pondicherry Museum showcases the rich cultural heritage of the region through exhibits of art, artifacts, and historical artifacts."
    },
    {
        "name": "Arikamedu",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Arikamedu is an archaeological site dating back to the Roman era, offering insights into the ancient trade and cultural exchanges."
    },
    {
        "name": "Ousteri Lake",
        "budget": "₹100 - ₹300 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Ousteri Lake, also known as Osudu Lake, is a scenic freshwater lake ideal for birdwatching, boating, and picnics."
    },
    {
        "name": "Pondicherry Beach Road",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Pondicherry Beach Road is a vibrant promenade lined with cafes, boutiques, and art galleries, offering stunning views of the sea."
    },
    {
        "name": "Matrimandir",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "Matrimandir is a spiritual meditation center located in Auroville, known for its iconic golden dome and tranquil meditation chambers."
    },
    {
        "name": "Gingee Fort",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹500 - ₹1000 (round trip by taxi or bus)",
        "description": "Gingee Fort, also known as Senji Fort, is a historic hill fortress known for its architectural grandeur and panoramic views of the surrounding landscape."
    },
    {
        "name": "Mahatma Gandhi Statue",
        "budget": "₹50 - ₹200 per person",
        "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
        "description": "The Mahatma Gandhi Statue is a prominent landmark located on the Beach Road, symbolizing peace, freedom, and Gandhian ideals."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pondicherry Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places[place_id - 1]

@app.get("/places/")
def read_all_places():
    return{"places":places}
