import streamlit as st

def main():
    st.title("Unit Converter")
    
    # Sidebar for category selection
    category = st.sidebar.selectbox(
        "Select Conversion Category",
        ["Length", "Weight/Mass", "Temperature", "Area", "Volume", "Speed", "Time"]
    )
    
    # Conversion logic based on category
    if category == "Length":
        length_converter()
    elif category == "Weight/Mass":
        weight_converter()
    elif category == "Temperature":
        temperature_converter()
    elif category == "Area":
        area_converter()
    elif category == "Volume":
        volume_converter()
    elif category == "Speed":
        speed_converter()
    elif category == "Time":
        time_converter()

def length_converter():
    st.header("Length Converter")
    
    # Define conversion factors to meters
    length_units = {
        "Meter (m)": 1.0,
        "Kilometer (km)": 1000.0,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Mile (mi)": 1609.34,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048,
        "Inch (in)": 0.0254
    }
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=1.0)
        from_unit = st.selectbox("From:", list(length_units.keys()), key="from_length")
    
    with col2:
        to_unit = st.selectbox("To:", list(length_units.keys()), key="to_length")
        # Calculate and display result
        result = input_value * length_units[from_unit] / length_units[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
    
    # Conversion formula explanation
    st.info(f"Conversion Formula: {from_unit} to {to_unit} = Value × {length_units[from_unit] / length_units[to_unit]:.6f}")

def weight_converter():
    st.header("Weight/Mass Converter")
    
    # Define conversion factors to kilograms
    weight_units = {
        "Kilogram (kg)": 1.0,
        "Gram (g)": 0.001,
        "Milligram (mg)": 0.000001,
        "Metric Ton (t)": 1000.0,
        "Pound (lb)": 0.453592,
        "Ounce (oz)": 0.0283495,
        "Stone (st)": 6.35029
    }
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=1.0, key="weight_input")
        from_unit = st.selectbox("From:", list(weight_units.keys()), key="from_weight")
    
    with col2:
        to_unit = st.selectbox("To:", list(weight_units.keys()), key="to_weight")
        # Calculate and display result
        result = input_value * weight_units[from_unit] / weight_units[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
    
    # Conversion formula explanation
    st.info(f"Conversion Formula: {from_unit} to {to_unit} = Value × {weight_units[from_unit] / weight_units[to_unit]:.6f}")

def temperature_converter():
    st.header("Temperature Converter")
    
    temperature_units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=0.0, key="temp_input")
        from_unit = st.selectbox("From:", temperature_units, key="from_temp")
    
    with col2:
        to_unit = st.selectbox("To:", temperature_units, key="to_temp")
        
        # Temperature conversion requires special formulas
        if from_unit == to_unit:
            result = input_value
        else:
            # Convert to Celsius first
            if from_unit == "Celsius (°C)":
                celsius = input_value
            elif from_unit == "Fahrenheit (°F)":
                celsius = (input_value - 32) * 5/9
            else:  # Kelvin
                celsius = input_value - 273.15
            
            # Convert from Celsius to target unit
            if to_unit == "Celsius (°C)":
                result = celsius
            elif to_unit == "Fahrenheit (°F)":
                result = celsius * 9/5 + 32
            else:  # Kelvin
                result = celsius + 273.15
        
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")
    
    # Show conversion formulas
    st.info("Conversion Formulas:")
    st.write("- Celsius to Fahrenheit: °F = °C × 9/5 + 32")
    st.write("- Fahrenheit to Celsius: °C = (°F - 32) × 5/9")
    st.write("- Celsius to Kelvin: K = °C + 273.15")
    st.write("- Kelvin to Celsius: °C = K - 273.15")

def area_converter():
    st.header("Area Converter")
    
    # Define conversion factors to square meters
    area_units = {
        "Square Meter (m²)": 1.0,
        "Square Kilometer (km²)": 1000000.0,
        "Square Centimeter (cm²)": 0.0001,
        "Square Millimeter (mm²)": 0.000001,
        "Square Mile (mi²)": 2590000.0,
        "Square Yard (yd²)": 0.836127,
        "Square Foot (ft²)": 0.092903,
        "Square Inch (in²)": 0.00064516,
        "Acre": 4046.86,
        "Hectare (ha)": 10000.0
    }
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=1.0, key="area_input")
        from_unit = st.selectbox("From:", list(area_units.keys()), key="from_area")
    
    with col2:
        to_unit = st.selectbox("To:", list(area_units.keys()), key="to_area")
        # Calculate and display result
        result = input_value * area_units[from_unit] / area_units[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
    
    # Conversion formula explanation
    st.info(f"Conversion Formula: {from_unit} to {to_unit} = Value × {area_units[from_unit] / area_units[to_unit]:.6f}")

def volume_converter():
    st.header("Volume Converter")
    
    # Define conversion factors to cubic meters
    volume_units = {
        "Cubic Meter (m³)": 1.0,
        "Cubic Kilometer (km³)": 1000000000.0,
        "Cubic Centimeter (cm³)": 0.000001,
        "Cubic Millimeter (mm³)": 1e-9,
        "Liter (L)": 0.001,
        "Milliliter (mL)": 0.000001,
        "Gallon (US)": 0.00378541,
        "Quart (US)": 0.000946353,
        "Pint (US)": 0.000473176,
        "Cup (US)": 0.000236588,
        "Fluid Ounce (US)": 2.9574e-5,
        "Tablespoon (US)": 1.4787e-5,
        "Teaspoon (US)": 4.9289e-6
    }
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=1.0, key="volume_input")
        from_unit = st.selectbox("From:", list(volume_units.keys()), key="from_volume")
    
    with col2:
        to_unit = st.selectbox("To:", list(volume_units.keys()), key="to_volume")
        # Calculate and display result
        result = input_value * volume_units[from_unit] / volume_units[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
    
    # Conversion formula explanation
    st.info(f"Conversion Formula: {from_unit} to {to_unit} = Value × {volume_units[from_unit] / volume_units[to_unit]:.6f}")

def speed_converter():
    st.header("Speed Converter")
    
    # Define conversion factors to meters per second
    speed_units = {
        "Meter per Second (m/s)": 1.0,
        "Kilometer per Hour (km/h)": 0.277778,
        "Mile per Hour (mph)": 0.44704,
        "Foot per Second (ft/s)": 0.3048,
        "Knot (kn)": 0.514444
    }
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=1.0, key="speed_input")
        from_unit = st.selectbox("From:", list(speed_units.keys()), key="from_speed")
    
    with col2:
        to_unit = st.selectbox("To:", list(speed_units.keys()), key="to_speed")
        # Calculate and display result
        result = input_value * speed_units[from_unit] / speed_units[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
    
    # Conversion formula explanation
    st.info(f"Conversion Formula: {from_unit} to {to_unit} = Value × {speed_units[from_unit] / speed_units[to_unit]:.6f}")

def time_converter():
    st.header("Time Converter")
    
    # Define conversion factors to seconds
    time_units = {
        "Second (s)": 1.0,
        "Millisecond (ms)": 0.001,
        "Microsecond (μs)": 0.000001,
        "Nanosecond (ns)": 1e-9,
        "Minute (min)": 60.0,
        "Hour (h)": 3600.0,
        "Day (d)": 86400.0,
        "Week (wk)": 604800.0,
        "Month (avg)": 2629800.0,  # Average month (30.44 days)
        "Year (avg)": 31557600.0   # Average year (365.25 days)
    }
    
    # Input and unit selection
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value:", value=1.0, key="time_input")
        from_unit = st.selectbox("From:", list(time_units.keys()), key="from_time")
    
    with col2:
        to_unit = st.selectbox("To:", list(time_units.keys()), key="to_time")
        # Calculate and display result
        result = input_value * time_units[from_unit] / time_units[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.6f} {to_unit}")
    
    # Conversion formula explanation
    st.info(f"Conversion Formula: {from_unit} to {to_unit} = Value × {time_units[from_unit] / time_units[to_unit]:.6f}")

if __name__ == "__main__":
    main()

print("Unit Converter App is running!")