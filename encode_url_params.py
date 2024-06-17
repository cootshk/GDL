import base64
def encode(domain: str, game_id: str, timespan: int) -> str:
    return base64.encode(f"{domain=}&{game_id=}&{timespan}".encode("utf-8")).decode("utf-8").replace("=", "%3D")