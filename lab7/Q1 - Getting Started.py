def greeting(name: str) -> str:
    # fill this in...
    return f"Hello, {name}! Functions are awesome!"

# Call function with argument: 'Luffy'
# Outputs: Hello, Luffy! Functions are awesome!

print(greeting("Luffy"))





def triangle(b:float,h:float):
    return (b*h)/2
    # fill this in...

print(triangle(5,2))  # 5.0
print(triangle(8,2))  # 8.0



def metric_to_imperial(metric_measurement:float,metric_unit:str):
    if metric_unit == "km":
        return metric_measurement * 0.62
    elif metric_unit == "kg":
        return metric_measurement * 0.16
    elif metric_unit == "L":
        return metric_measurement * 0.26
    # fill in here...

measurement = float(input('Measurement: '))
unit = input('Unit: ')

# call the function here!
# ...
print(f"Imperial conversion: {metric_to_imperial(measurement, unit):.2f}")