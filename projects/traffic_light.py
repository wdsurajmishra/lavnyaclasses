#  Humko ek traffice light ka system jisme hum ek signal input karenge us hisab humko output milega.

signals = ["red", "yellow", "green"]
def traffic_light(signal):
    if not signal in signals:
        return "Invalid Signal"
    
    if signal == "red":
        return "Stop the Vehicle"
    
    elif signal == "yellow":
        return "Get Ready to Move"

    elif signal == "green":
        return "Move the Vehicle"




user_input = input("Enter Your Traffic Light Color: ").strip().lower()

result = traffic_light(user_input)
print(result)