# from fastapi import FastAPI

# app = FastAPI()

places = [
    {
        "name": "Baga Beach",
        "budget": "₹500 - ₹2000 per person per day",
        "travel_expense": "₹200 - ₹500 (round trip, depending on distance)",
        "description": "Baga Beach is famous for its lively atmosphere, water sports, and beach shacks serving delicious seafood."
    },
    {
        "name": "Calangute Beach",
        "budget": "₹500 - ₹2000 per person per day",
        "travel_expense": "₹200 - ₹500 (round trip, depending on distance)",
        "description": "Calangute Beach is one of the most popular and busiest beaches in Goa, known for its long stretch of golden sand and various water activities."
    },
    {
        "name": "Anjuna Beach",
        "budget": "₹500 - ₹1500 per person per day",
        "travel_expense": "₹500 - ₹1000 (round trip, depending on distance)",
        "description": "Anjuna Beach is famous for its trance parties, flea market, and laid-back vibe, making it a favorite among backpackers and hippies."
    }
    # {
    #     "name": "Palolem Beach",
    #     "budget": "₹500 - ₹2000 per person per day",
    #     "travel_expense": "₹500 - ₹1000 (round trip, depending on distance)",
    #     "description": "Palolem Beach is a beautiful crescent-shaped beach with calm waters, ideal for swimming, sunbathing, and dolphin spotting."
    # },
    # {
    #     "name": "Dudhsagar Waterfalls",
    #     "budget": "₹1000 - ₹2500 per person",
    #     "travel_expense": "₹1000 - ₹1500 (round trip by bus or taxi)",
    #     "description": "Dudhsagar Waterfalls is one of the tallest waterfalls in India, surrounded by lush greenery and offering breathtaking views."
    # },
    # {
    #     "name": "Fort Aguada",
    #     "budget": "₹100 - ₹300 per person",
    #     "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
    #     "description": "Fort Aguada is a well-preserved 17th-century Portuguese fort offering panoramic views of the Arabian Sea and the surrounding landscape."
    # },
    # {
    #     "name": "Chapora Fort",
    #     "budget": "₹100 - ₹300 per person",
    #     "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
    #     "description": "Chapora Fort is known for its ruins and offers stunning views of Vagator Beach and the nearby coastline."
    # },
    # {
    #     "name": "Mangeshi Temple",
    #     "budget": "₹50 - ₹200 per person",
    #     "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
    #     "description": "Mangeshi Temple is one of the most famous and beautiful temples in Goa, dedicated to Lord Shiva."
    # },
    # {
    #     "name": "Se Cathedral",
    #     "budget": "₹50 - ₹200 per person",
    #     "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
    #     "description": "Se Cathedral is one of the largest churches in Asia and a UNESCO World Heritage Site, known for its stunning architecture and religious significance."
    # },
    # {
    #     "name": "Dona Paula",
    #     "budget": "₹100 - ₹500 per person",
    #     "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
    #     "description": "Dona Paula is a popular tourist destination known for its romantic viewpoint overlooking the Arabian Sea."
    # },
    # {
    #     "name": "Candolim Beach",
    #     "budget": "₹500 - ₹2000 per person per day",
    #     "travel_expense": "₹200 - ₹500 (round trip, depending on distance)",
    #     "description": "Candolim Beach is known for its serene atmosphere and water sports activities, making it a perfect destination for relaxation and adventure."
    # },
    # {
    #     "name": "Miramar Beach",
    #     "budget": "₹500 - ₹1500 per person per day",
    #     "travel_expense": "₹200 - ₹500 (round trip, depending on distance)",
    #     "description": "Miramar Beach is a popular destination for evening walks, water sports, and enjoying beautiful sunsets."
    # },
    # {
    #     "name": "Vagator Beach",
    #     "budget": "₹500 - ₹2000 per person per day",
    #     "travel_expense": "₹200 - ₹500 (round trip, depending on distance)",
    #     "description": "Vagator Beach is famous for its scenic beauty, rocky cliffs, and vibrant nightlife, making it a favorite among both locals and tourists."
    # },
    # {
    #     "name": "Morjim Beach",
    #     "budget": "₹500 - ₹1500 per person per day",
    #     "travel_expense": "₹500 - ₹1000 (round trip, depending on distance)",
    #     "description": "Morjim Beach is known for its tranquil atmosphere, clean sands, and as a nesting site for Olive Ridley turtles."
    # },
    # {
    #     "name": "Aguada Fort",
    #     "budget": "₹100 - ₹300 per person",
    #     "travel_expense": "₹100 - ₹300 (round trip by taxi or bus)",
    #     "description": "Aguada Fort is a well-preserved 17th-century Portuguese fort offering panoramic views of the Arabian Sea and the surrounding coastline."
    # }
]

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Goa Places API"}

# @app.get("/places/{place_id}")
# def read_place(place_id: int):
#     return places[place_id - 1]

# @app.get("/places")
# def read_all_places():
#     return { "places":places}