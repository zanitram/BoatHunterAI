def calculate_score(boat):
    score=50
    e=boat.engine.lower()
    if "5.0" in e: score+=15
    elif "5.7" in e: score+=12
    elif "7.4" in e or "454" in e: score-=8
    if 23<=boat.length<=27: score+=8
    if boat.trailer: score+=5
    if boat.price<=10000: score+=10
    return min(score,100)
