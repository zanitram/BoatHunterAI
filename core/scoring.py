def calculate_score(boat):

    score = 50

    engine = boat.engine.lower()

    # Preferred engines
    if "5.0" in engine:
        score += 15

    if "5.7" in engine:
        score += 15

    # Big block penalty
    if "7.4" in engine or "454" in engine:
        score -= 10

    # Trailer
    if boat.trailer:
        score += 5

    # Price bonuses
    if boat.price <= 10000:
        score += 15
    elif boat.price <= 15000:
        score += 8

    # Length bonus
    if 23 <= boat.length <= 26:
        score += 10

    return min(score,100)