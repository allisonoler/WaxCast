import json

def load_wax_catalog(filepath="waxes.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def find_optimal_waxes(predicted_snow_state, current_temp, catalog):
    """
    Filters the wax catalog based on the ML model's predicted snow state
    and the current environmental temperature.
    """
    recommendations = []
    
    for wax in catalog:
        # 1. Check if the current temperature falls within the wax's operating window
        min_t = wax["temp_range"]["min_celsius"]
        max_t = wax["temp_range"]["max_celsius"]
        
        if min_t <= current_temp <= max_t:
            # 2. Check if the wax is rated for the predicted snow structural state
            if predicted_snow_state in wax["optimal_snow_conditions"]:
                recommendations.append(wax)
                
    return recommendations

if __name__ == "__main__":
    wax_catalog = load_wax_catalog()
    
    mock_current_temp = -3.5  # In Celsius
    mock_predicted_snow = "packed_powder"
    
    print(f"--- Pipeline Status ---")
    print(f"Current Temp: {mock_current_temp}°C")
    print(f"ML Predicted Snow State: '{mock_predicted_snow}'\n")
    
    # Query the database
    results = find_optimal_waxes(mock_predicted_snow, mock_current_temp, wax_catalog)
    
    print(f"--- Recommended Waxes Found ({len(results)}) ---")
    for choice in results:
        print(f" -> [{choice['brand']}] {choice['line']} - {choice['product_name']} ({choice['form']})")