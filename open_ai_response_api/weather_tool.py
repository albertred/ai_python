from openai import OpenAI
import os

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_weather_info(city):
    try:
        # Create the chat completion
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """You are a weather reporting assistant. When asked about weather, 
                simulate realistic weather information for the given location based on its typical climate, season, 
                and geographical location. Include temperature, conditions, humidity, and wind speed in your response. 
                Present the information as if it's real current weather data."""},
                {"role": "user", "content": f"What is the current weather in {city}? Include temperature, conditions, humidity, and wind speed."}
            ],
            temperature=0.7
        )
        
        # Get the response content
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content
        else:
            return "Sorry, I couldn't get the weather information."
            
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("\nWeather Information Tool (Enter 'quit' to exit)")
    print("----------------------------------------")
    
    while True:
        # Get city from user input
        city = input("\nEnter city name: ")
        
        if city.lower() == 'quit':
            print("\nGoodbye!")
            break
            
        # Get and display weather
        print("\nFetching weather information...")
        weather_info = get_weather_info(city)
        print("\n" + weather_info)

if __name__ == "__main__":
    main()