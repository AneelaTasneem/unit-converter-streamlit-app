import streamlit as st  

# Setup Streamlit App  
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")  
st.title("🔄 Unit Converter")  
st.markdown("Convert Length, Temperature, and Weight easily with this tool.")  

# Sidebar for Conversion Type  
st.sidebar.title("⚙️ Select Conversion Type")  
options = ["Length", "Temperature", "Weight"]  
choice = st.sidebar.radio("", options)  

# Define conversion functions  
def convert_length(value, from_unit, to_unit):  
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371}  
    return value * (length_units[to_unit] / length_units[from_unit])  

def convert_temperature(value, from_unit, to_unit):  
    if from_unit == "Celsius" and to_unit == "Fahrenheit":  
        return (value * 9/5) + 32  
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":  
        return (value - 32) * 5/9  
    return value  

def convert_weight(value, from_unit, to_unit):  
    weight_units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462}  
    return value * (weight_units[to_unit] / weight_units[from_unit])  

# Main Conversion UI  
st.write(f"### {choice} Converter")  

col1, col2 = st.columns(2)  

if choice == "Length":  
    from_unit = col1.selectbox("From:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles"])  
    to_unit = col2.selectbox("To:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles"])  
elif choice == "Temperature":  
    from_unit = col1.selectbox("From:", ["Celsius", "Fahrenheit"])  
    to_unit = col2.selectbox("To:", ["Celsius", "Fahrenheit"])  
elif choice == "Weight":  
    from_unit = col1.selectbox("From:", ["Kilograms", "Grams", "Pounds"])  
    to_unit = col2.selectbox("To:", ["Kilograms", "Grams", "Pounds"])  

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")  

if st.button("🔄 Convert"):  
    if value == 0:  
        st.warning("Please enter a value greater than 0!")  
    else:  
        if choice == "Length":  
            result = convert_length(value, from_unit, to_unit)  
        elif choice == "Temperature":  
            result = convert_temperature(value, from_unit, to_unit)  
        elif choice == "Weight":  
            result = convert_weight(value, from_unit, to_unit)  

        st.success(f"✅ Converted value: **{result:.2f} {to_unit}**")  
