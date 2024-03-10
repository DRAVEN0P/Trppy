from fastapi import FastAPI

app = FastAPI()

places = [
    {
        "name": "Radhanagar Beach, Havelock Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by flight or ferry)",
        "description": "Radhanagar Beach is renowned for its crystal-clear waters, powdery white sands, and breathtaking sunset views, making it one of the best beaches in Asia."
    },
    {
        "name": "Cellular Jail, Port Blair",
        "budget": "₹100 - ₹500 per person",
        "travel_expense": "₹1000 - ₹2000 (round trip by taxi or bus)",
        "description": "Cellular Jail, also known as Kālā Pānī, is a historic colonial prison-turned-museum that offers insights into India's struggle for independence."
    },
    {
        "name": "Ross Island",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹1000 - ₹3000 (round trip by ferry or boat)",
        "description": "Ross Island, once the administrative headquarters of the British, now stands in ruins surrounded by lush greenery, offering a glimpse into its colonial past."
    },
    {
        "name": "Elephant Beach, Havelock Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "Elephant Beach is known for its vibrant coral reefs, diverse marine life, and thrilling water sports activities like snorkeling and scuba diving."
    },
    {
        "name": "Neil Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "Neil Island, also known as Shaheed Dweep, is a serene island with pristine beaches, lush greenery, and relaxed vibes, perfect for a peaceful getaway."
    },
    {
        "name": "Baratang Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "Baratang Island is known for its mangrove forests, limestone caves, and unique natural formations like the Mud Volcano and Limestone Caves."
    },
    {
        "name": "North Bay Island",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹2000 - ₹5000 (round trip by ferry or boat)",
        "description": "North Bay Island is famous for its underwater sea walk, glass-bottom boat rides, and vibrant coral reefs, offering excellent opportunities for snorkeling and diving."
    },
    {
        "name": "Limestone Caves, Baratang Island",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "The Limestone Caves of Baratang Island are natural formations created over centuries by the erosion of limestone rocks, offering a unique and mesmerizing experience."
    },
    {
        "name": "Mahatma Gandhi Marine National Park",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹2000 - ₹5000 (round trip by ferry or boat)",
        "description": "The Mahatma Gandhi Marine National Park is a protected area known for its rich biodiversity, colorful coral reefs, and diverse marine life, offering opportunities for snorkeling and diving."
    },
    {
        "name": "Chidiya Tapu (Bird Island)",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹2000 - ₹5000 (round trip by taxi or bus)",
        "description": "Chidiya Tapu is a picturesque destination known for its stunning sunset views, mangrove forests, and diverse bird species, making it a paradise for birdwatchers and nature enthusiasts."
    },
    {
        "name": "Wandoor Beach",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹2000 - ₹5000 (round trip by taxi or bus)",
        "description": "Wandoor Beach is famous for its clear turquoise waters, pristine sands, and coral reefs, offering excellent opportunities for swimming, sunbathing, and snorkeling."
    },
    {
        "name": "Mount Harriet National Park",
        "budget": "₹500 - ₹1500 per person",
        "travel_expense": "₹2000 - ₹5000 (round trip by ferry or boat)",
        "description": "Mount Harriet National Park is a protected area known for its lush greenery, diverse flora and fauna, and panoramic views of the surrounding islands and sea."
    },
    {
        "name": "Lalaji Bay Beach, Long Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "Lalaji Bay Beach is a secluded and pristine beach located on Long Island, offering solitude, serenity, and stunning natural beauty away from the crowds."
    },
    {
        "name": "Cinque Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "Cinque Island is a group of two picturesque islands known for their clear waters, vibrant coral reefs, and diverse marine life, perfect for snorkeling and diving enthusiasts."
    },
    {
        "name": "Jolly Buoy Island",
        "budget": "₹1000 - ₹3000 per person per day",
        "travel_expense": "₹5000 - ₹10000 (round trip by ferry or boat)",
        "description": "Jolly Buoy Island is part of the Mahatma Gandhi Marine National Park and is famous for its pristine beaches, coral reefs, and underwater marine life, making it an ideal spot for snorkeling and diving adventures."
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Andaman and Nicobar Islands Places API"}

@app.get("/places/{place_id}")
def read_place(place_id: int):
    return places[place_id - 1]

@app.get("/places")
def read_all_places():
    return { "places":places}


