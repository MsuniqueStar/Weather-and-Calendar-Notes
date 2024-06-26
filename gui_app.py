import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import requests
import threading
from dotenv import load_dotenv
import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Constants
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
CALENDAR_ID = '314bf9697b202548d34eba4ec164c849cc5eb1d91baef7845d6c8727488397e0@group.calendar.google.com'

# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = 'credentials.json'

if not WEATHER_API_KEY:
    raise ValueError("No API key found. Please set the WEATHER_API_KEY environment variable.")

# Function to fetch weather data
def get_weather(city):
    try:
        response = requests.get(WEATHER_URL.format(city=city, key=WEATHER_API_KEY))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        weather_data = response.json()
        print(weather_data)  # Print the full API response for debugging
        if response.status_code == 200:
            temp = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            weather_info = f"Temperature: {temp:.2f}°C\n" \
                           f"Weather: {weather_data['weather'][0]['description']}"
        else:
            weather_info = weather_data.get('message', 'Error fetching weather data')
    except requests.exceptions.RequestException as e:
        weather_info = f"Network error: {e}"
        log_error(e)
    except Exception as e:
        weather_info = f"Error fetching weather data: {e}"
        log_error(e)
    return weather_info

# Function to update weather info
def update_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return
    weather_info = get_weather(city)
    weather_label.config(text=weather_info)

# Function to save calendar note
def save_note():
    selected_date = calendar.get_date()
    note = note_entry.get()
    if not note:
        messagebox.showwarning("Input Error", "Please enter a note")
        return
    notes[selected_date] = note
    update_notes_list()

    # Add event to Google Calendar
    try:
        start_date = datetime.datetime.strptime(selected_date, "%m/%d/%y")
        start_time = start_date.strftime("%Y-%m-%dT09:00:00Z")
        end_time = start_date.strftime("%Y-%m-%dT10:00:00Z")
        add_event_to_google_calendar(note, "Calendar Note", start_time, end_time)
    except Exception as e:
        log_error(f"Error creating calendar event: {e}")

# Function to update notes list
def update_notes_list():
    notes_list.delete(0, tk.END)
    for date, note in notes.items():
        notes_list.insert(tk.END, f"{date}: {note}")

# Function to refresh data periodically
def refresh_data():
    update_weather()
    # Schedule the function to run again after 10 minutes (600000 milliseconds)
    root.after(600000, refresh_data)

# Function to log errors to a file
def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {error_message}\n")

# Google Calendar API functions
def get_calendar_service():
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)
    return service

def add_event_to_google_calendar(event_summary, event_description, start_time, end_time):
    service = get_calendar_service()
    event = {
        'summary': event_summary,
        'description': event_description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
    }
    try:
        print(f"Creating event with data: {event}")  # Log event data for debugging
        event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
    except Exception as e:
        log_error(f"Error adding event to Google Calendar: {e}")
        print(f"Error adding event to Google Calendar: {e}")

# Create main window
root = tk.Tk()
root.title("Ananya's Weather and Calendar Notes")

# Add a signature label
signature_label = tk.Label(root, text="Created by Ananya", font=("Helvetica", 10, "italic"))
signature_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Custom styling
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), padding=10)
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TEntry", font=("Helvetica", 12), padding=10)
style.configure("TFrame", padding=10)

# Weather widget
weather_frame = ttk.LabelFrame(root, text="Weather", padding=10)
weather_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(weather_frame, text="Enter city:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
city_entry = ttk.Entry(weather_frame, font=("Helvetica", 12))
city_entry.grid(row=0, column=1, padx=5, pady=5)

weather_button = ttk.Button(weather_frame, text="Get Weather", command=update_weather)
weather_button.grid(row=0, column=2, padx=5, pady=5)

weather_label = ttk.Label(weather_frame, text="Weather info will be shown here", font=("Helvetica", 12))
weather_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Calendar widget
calendar_frame = ttk.LabelFrame(root, text="Calendar Notes", padding=10)
calendar_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

calendar = Calendar(calendar_frame, selectmode="day", font=("Helvetica", 12))
calendar.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

tk.Label(calendar_frame, text="Note:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
note_entry = ttk.Entry(calendar_frame, font=("Helvetica", 12))
note_entry.grid(row=1, column=1, padx=5, pady=5)

note_button = ttk.Button(calendar_frame, text="Save Note", command=save_note)
note_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

notes_list = tk.Listbox(calendar_frame, height=10, font=("Helvetica", 12))
notes_list.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

notes = {}

# Start the periodic data refresh
root.after(0, refresh_data)

# Run the application
root.mainloop()
