# Ananya's Weather and Calendar Notes Application

This is a Python application that allows users to fetch weather data for a specified city and create calendar notes that sync with Google Calendar. The application uses Tkinter for the GUI, OpenWeatherMap API for weather data, and Google Calendar API for event management.

## Features

- Fetch and display current weather information for a specified city.
- Create and save calendar notes.
- Sync calendar notes with Google Calendar.

## Prerequisites

- Python 3.x
- Tkinter
- tkcalendar
- requests
- python-dotenv
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install Dependencies

```bash
pip install tkcalendar requests python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 3. OpenWeatherMap API Key

- Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get an API key.
- Create a `.env` file in the project directory and add your OpenWeatherMap API key:

```
WEATHER_API_KEY=your_openweathermap_api_key
```

### 4. Google Calendar API Setup

#### 4.1. Create a Project

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project.

#### 4.2. Enable Google Calendar API

- In the Google Cloud Console, go to "APIs & Services" > "Library".
- Search for "Google Calendar API" and enable it for your project.

#### 4.3. Create Service Account

- Navigate to "IAM & Admin" > "Service Accounts".
- Click "Create Service Account".
- Provide a name and description for the service account and click "Create".
- Assign the "Editor" role to the service account.
- Click "Done".

#### 4.4. Create and Download Service Account Key

- Go to the "Keys" tab of the created service account.
- Click "Add Key" > "Create New Key".
- Select "JSON" and click "Create".
- Download the `credentials.json` file and place it in the project directory.

#### 4.5. Share Google Calendar with Service Account

1. Open your browser and navigate to [Google Calendar](https://calendar.google.com/).
2. On the left side of the screen, you will see a list of calendars under "My calendars".
3. Find the calendar you want the service account to manage.
4. If you want to create a new calendar, click the "+" button next to "Add other calendars" and select "Create new calendar".
5. Click on the three vertical dots (menu icon) next to the calendar name.
6. Select "Settings and sharing" from the dropdown menu.
7. Scroll down to the "Share with specific people" section.
8. Click on "Add people".
9. In the "Add email or name" field, enter the email address of your service account. The service account email can be found in your `credentials.json` file.
10. Choose the role "Make changes to events" from the permissions dropdown.
11. Click "Send". The service account will now have permission to manage events in the calendar.

### 5. Update Calendar ID

If you are not using the primary calendar, update the `CALENDAR_ID` in the `gui_app.py` script to the calendar ID you are using:

```python
CALENDAR_ID = 'your_calendar_id'
```

## Running the Application

Run the script using Python:

```bash
python gui_app.py
```

## Application Usage

1. **Fetch Weather Data**:
   - Enter a city name in the "Enter city" field.
   - Click "Get Weather" to fetch and display the weather information.

2. **Create Calendar Note**:
   - Select a date from the calendar.
   - Enter a note in the "Note" field.
   - Click "Save Note" to save the note and sync it with Google Calendar.

## Viewing Calendar Events

You can view the created events in Google Calendar using the provided public URL:

[Public Calendar URL]

Or embed it in a web page using the following embed code


## Troubleshooting

- Ensure all dependencies are installed correctly.
- Verify that the `credentials.json` file is in the correct directory.
- Check the permissions of the service account on Google Calendar.
- Refer to `error_log.txt` for detailed error messages.

## Contact

For any inquiries, please contact Ananya at ananya.sathyanarayana2022@gmail.com.