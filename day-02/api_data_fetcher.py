import requests
import json

api_url = "https://api.waqi.info/feed/here/"
API_KEY = "5ea29bf2e8b3fd388a867e2609976e9960bfa173"

def check_air_quality():
    params = {
        "token": API_KEY
    }

    # User input
    user_aqi = int(input("Enter AQI threshold: "))
    #print(user_aqi)

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
       # print(data)

        if data["status"] == "ok":
            api_aqi = data["data"]["aqi"]
            city = data["data"]["city"]["name"]

            print(f"\n📍 City: {city}")
            print(f" Current AQI: {api_aqi}")
             
            # if-else comparison
            
            if api_aqi < user_aqi:
                limit_status = "Within acceptable limit"
                print ("Air quality is within your acceptable limit")
            else:
               limit_status = "Exceeds acceptable limit"
               print("Air quality excceds your limit")
               

        
            #AQI classification
            if api_aqi <= 50:
                level = "Good"
            elif api_aqi <= 100:
                level = "Moderate"
            elif api_aqi <= 150:
                level = "Unhealthy for Sensitive Groups"
            elif api_aqi <=200:
                level = "Unhealthy "
            else:
                level = "Hazardous "
            print(f"Air Quality level : {level}")

            processed_data = {
                "city": city,
                "current_aqi": api_aqi,
                "aqi_level": level,
                "user_threshold": user_aqi,
                "status" :limit_status,
            
            }

            # 🔹 Save to JSON file
            with open("output.json", "w") as file:
                json.dump(processed_data, file, indent=4)

        else:
            print("API returned error",data)


    else:
        print("HTTP Error:",response.status_code)
            
#call function            
check_air_quality()