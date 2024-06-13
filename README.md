# Weather and Calendar Notes Application

This is a simple GUI application that allows users to check the weather for a specified city and manage calendar notes. The application is built using Python's `tkinter` library for the GUI and `requests` for fetching weather data from the OpenWeather API.

## Features

- Fetch current weather information for any city.
- Display weather details including temperature and weather description.
- Calendar widget to select dates.
- Add and save notes for selected dates.
- Periodic update of weather information.

## Requirements

- Python 3.x
- `tkinter` library (included with Python standard library)
- `requests` library
- `tkcalendar` library
- `python-dotenv` library

## Setup and Installation

1. **Clone the repository or download the source code.**

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries:**
    ```bash
    pip install requests tkcalendar python-dotenv
    ```

4. **Create a `.env` file in the same directory as your script and add your OpenWeather API key:**
    ```
    WEATHER_API_KEY=your_api_key_here
    ```

5. **Run the application:**
    ```bash
    python gui_app.py
    ```

## Usage

1. **Weather Widget:**
   - Enter the name of the city in the input field.
   - Click the "Get Weather" button to fetch and display the weather information.

2. **Calendar Notes Widget:**
   - Select a date from the calendar.
   - Enter a note in the "Note" input field.
   - Click the "Save Note" button to save the note for the selected date.
   - The note will appear in the list below.

## Code Overview

- **`gui_app.py`**: The main script that creates the GUI application. It includes functions to fetch weather data, update the weather information, save calendar notes, and periodically refresh data.

## Example .env File
WEATHER_API_KEY=your_api_key_here



## Troubleshooting

- **Invalid API Key Error**: Ensure that your API key is valid and correctly set in the `.env` file.
- **Library Import Errors**: Ensure all required libraries are installed. Use `pip install -r requirements.txt` if a `requirements.txt` file is provided.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenWeather](https://openweathermap.org/) for providing the weather API.
- [tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI library.
- [tkcalendar](https://github.com/j4321/tkcalendar) for the calendar widget.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.

## Contact

For any questions or issues, please open an issue in this repository or contact the maintainer at [ananya.sathyanarayana2022@gmail.com].



