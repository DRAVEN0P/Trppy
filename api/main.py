from fastapi import FastAPI

import Mountains.Shimla as Sh
from Beaches.main import AllBeaches
from Beaches.Goa import places as Goa

shimla = Sh.places_shimla
app = FastAPI()


@app.get("/goa")
def read_root():
    return {
        "shimla": Goa
    }

@app.get("/allBeaches")
def read_all_beaches():
    return {
        "AllBeaches": AllBeaches
    }