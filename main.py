from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from calculator import average


app = FastAPI(title="Github Actions Practice API")


class NumbersRequest(BaseModel):
    values: list[float]


class AverageResponse(BaseModel):
    average: float


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a friendly greeting so the root endpoint is not empty."""
    return {"message": "Welcome to the Github Actions Practice API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Expose a minimal health check for smoke tests."""
    return {"status": "ok"}


@app.post("/average", response_model=AverageResponse)
def calculate_average(payload: NumbersRequest) -> AverageResponse:
    """Return the arithmetic mean of the provided values."""
    try:
        computed_average = average(payload.values)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return AverageResponse(average=computed_average)


def main() -> None:
    """Allow running the API locally with ``python main.py``."""
    try:
        import uvicorn
    except ImportError as exc:
        raise SystemExit(
            "uvicorn is required to run the FastAPI app. Please install it with "
            "'pip install uvicorn'."
        ) from exc

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
