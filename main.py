from fastapi import FastAPI, HTTPException
import math

app = FastAPI(title="Calculator API")
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": "All arguments must be valid numbers."}
    )

def validate_numbers(*args):
    """Raise HTTP 422 if any argument fails float conversion."""
    for val in args:
        try:
            float(val)
        except (TypeError, ValueError):
            raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")



@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    """
    Add two numbers together.

    Parameters:
        a (float): First number.
        b (float): Second number.
    """
    validate_numbers(a, b)
    return {"operation": "add", "a": a, "b": b, "result": a + b}


@app.get("/sub/{a}/{b}")
def sub(a: float, b: float):
    """
    Subtract b from a.

    Parameters:
        a (float): Number to subtract from.
        b (float): Number to subtract.

    """
    validate_numbers(a, b)
    return {"operation": "subtract", "a": a, "b": b, "result": a - b}


@app.get("/multiply/{a}/{b}")
def mult(a: float, b: float):
    """
    Multiply two numbers together.

    Parameters:
        a (float): First number.
        b (float): Second number.
    """
    validate_numbers(a, b)
    return {"operation": "multiply", "a": a, "b": b, "result": a * b}


@app.get("/divide/{a}/{b}")
def div(a: float, b: float):
    """
    Divide a by b.

    Parameters:
        a (float): Dividend.
        b (float): Divisor. Must not be zero.
    """
    validate_numbers(a, b)
    if b == 0:
        raise HTTPException(
            status_code=422,
            detail="Division by zero is not allowed. Please provide a non-zero value for b."
        )
    return {"operation": "divide", "a": a, "b": b, "result": a / b}


@app.get("/hypotenuse/{a}/{b}")
def hypotenuse(a: float, b: float):
    """
    Calculate the hypotenuse of a right triangle given its two legs.

    Uses the Pythagorean theorem: c = sqrt(a² + b²).

    Parameters:
        a (float): Length of first leg. Must be positive.
        b (float): Length of second leg. Must be positive.
    """
    validate_numbers(a, b)
    if a <= 0 or b <= 0:
        raise HTTPException(status_code=422, detail="Both legs must be positive numbers.")
    return {"operation": "hypotenuse", "a": a, "b": b, "result": math.sqrt(a ** 2 + b ** 2)}


@app.get("/triangle-area/{base}/{height}")
def triangle_area(base: float, height: float):
    """
    Calculate the area of a triangle given its base and height.

    Formula: area = 0.5 * base * height.

    Parameters:
        base (float): Base length of the triangle. Must be positive.
        height (float): Height of the triangle. Must be positive.
    """
    validate_numbers(base, height)
    if base <= 0 or height <= 0:
        raise HTTPException(status_code=422, detail="Base and height must be positive numbers.")
    return {"operation": "triangle_area", "base": base, "height": height, "result": 0.5 * base * height}


@app.get("/average/{a}/{b}/{c}")
def average(a: float, b: float, c: float):
    """
    Calculate the average (mean) of three numbers.

    Formula: (a + b + c) / 3.

    Parameters:
        a (float): First number.
        b (float): Second number.
        c (float): Third number..
    """
    validate_numbers(a, b, c)
    return {"operation": "average", "a": a, "b": b, "c": c, "result": (a + b + c) / 3}


