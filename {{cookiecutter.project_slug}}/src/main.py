import torch
import uvicorn
from fastapi import FastAPI

from config.config import cfg
from src.schema import ModelPayload

#
# Instantiate the FastAPI app
#
app = FastAPI()

#
# Load the model into memory
#
model = torch.load(cfg["fastapi.model"]["path"])
model.eval()  # <-- NOTE: This is required for inference to work properly


#
# Define the routes
#
@app.get("/")
def index():
    """Index route

    Serves as both a health check and simple desciption of the API
    """
    return {"message": cfg["fastapi.service"]["description"]}


@app.post("/predict")
def predict(
    data: ModelPayload,  # <-- NOTE: FastAPI comes with built-in data validation based on pydantic schemas
):
    """Prediction route

    Args:
        data (ModelPayload): Payload containing the data to be used for inference

    Returns:
    [TODO: Replace this generic dict with a defined schema that is serializable to JSON; see schema.py]
        dict: Prediction results
    """
    # Convert the payload into a tensor
    # NOTE: This assumes that the payload is a dict with a single key, "data".
    # Update to fit your needs. Also, if the model is running on GPU-enabled hardware,
    # the tensor should be moved to the GPU prior to inference.
    tensor = torch.tensor(data.dict()["data"])

    # Make a prediction
    prediction = model(tensor)

    # NOTE: If the model is running on GPU-enabled hardware, the prediction will need
    # to be moved to the CPU prior to serialization.

    # Return the prediction
    return {"prediction": prediction.tolist()}


#
# Run the app
#
if __name__ == "__main__":
    config = uvicorn.Config(**cfg["fastapi.server"])
    server = uvicorn.Server(config)
    server.run()
