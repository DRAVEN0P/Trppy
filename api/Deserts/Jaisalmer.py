from fastapi import FastAPI

app = FastAPI()

places_jaisalmer = [
    {
        "name": "Jaisalmer Fort",
        "description": "A UNESCO World Heritage Site, known for its stunning architecture, intricate carvings, and panoramic views of the city.",
        "budget": "₹100 - ₹500 per person (including entry fees, guided tour, and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Patwon ki Haveli",
        "description": "A cluster of five havelis, adorned with exquisite Rajasthani architecture, intricate carvings, and ornate balconies.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Gadisar Lake",
        "description": "A man-made reservoir surrounded by temples, ghats, and pavilions, offering a serene atmosphere and boat rides.",
        "budget": "₹50 - ₹200 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Sam Sand Dunes",
        "description": "Offers a quintessential desert experience with camel safaris, dune bashing, traditional folk performances, and overnight camping under the stars.",
        "budget": "₹500 - ₹2000 per person per day (including camel safari, desert camping, and meals).",
        "travel_expense": "₹2000 - ₹5000 (round trip by taxi or jeep)."
    },
    {
        "name": "Desert National Park",
        "description": "Home to diverse desert flora and fauna, including migratory birds, desert foxes, and rare species like the Great Indian Bustard.",
        "budget": "₹100 - ₹500 per person (including entry fees and transportation).",
        "travel_expense": "₹2000 - ₹5000 (round trip by taxi or bus)."
    },
    {
        "name": "Kuldhara Village",
        "description": "An abandoned ghost village, known for its eerie atmosphere, mysterious past, and tales of paranormal activity.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Jain Temples",
        "description": "Boasts several beautifully carved Jain temples, such as the Jain Temples inside Jaisalmer Fort and the Lodurva Jain Temple.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Bada Bagh (Royal Cenotaphs)",
        "description": "A complex of royal cenotaphs, known for their architectural grandeur, intricate carvings, and panoramic views of the desert landscape.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Thar Heritage Museum",
        "description": "Showcases the rich cultural heritage of Rajasthan, with exhibits on local history, folk art, traditional costumes, and artifacts.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Salim Singh ki Haveli",
        "description": "A historic mansion known for its distinctive architecture, intricately carved balconies, and fascinating legends.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Tazia Tower",
        "description": "A five-tiered sandstone structure, known for its elegant design, intricate carvings, and cultural significance in Rajasthani architecture.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Nathmal ki Haveli",
        "description": "A historic mansion built by two brothers, known for its unique blend of Rajasthani and Islamic architectural styles, ornate carvings, and exquisite craftsmanship.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Windmill Park",
        "description": "A picturesque area dotted with wind turbines, offering scenic views of the desert landscape and opportunities for photography.",
        "budget": "₹50 - ₹200 per person (including transportation and snacks).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Desert Culture Centre and Museum",
        "description": "Showcases the cultural heritage of Rajasthan, with exhibits on desert life, folk traditions, music, dance, and handicrafts.",
        "budget": "₹50 - ₹200 per person (including entry fees and guided tour).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    },
    {
        "name": "Silk Route Art Gallery",
        "description": "Features contemporary and traditional artworks inspired by the desert landscape, local culture, and Rajasthani traditions.",
        "budget": "₹50 - ₹200 per person (including entry fees and transportation).",
        "travel_expense": "₹1000 - ₹3000 (round trip by taxi or bus)."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Jaisalmer Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places_jaisalmer[place_id - 1]

@app.get("/places")
def read_all_places():
    return {"places": places_jaisalmer}
