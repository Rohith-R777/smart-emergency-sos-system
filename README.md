# Emergency SOS System

## Overview
The Emergency SOS System is designed to provide immediate assistance in emergency situations by notifying pre-defined contacts and utilizing various communication methods to ensure help arrives swiftly.

## Features (MVP)
- **Instant Notifications (MVP)**: Logs SOS alerts via the built-in PHP endpoint (SMS/email integrations are planned).
- **Location Tracking**: Captures the user's location with the browser's Geolocation API.
- **User-Friendly Interface**: Easy to use application for both users and responders.
- **Multiple Communication Channels (Planned)**: SMS, email, and emergency calls.

## Nearby Places Technology (Planned)
The nearby places feature is planned and will use the technologies already present in this project:
- **Google Maps JavaScript API**: Renders the map and visualizes nearby resources.
- **Browser Geolocation API**: Captures the user's current location.
- **Vanilla JavaScript + HTML/CSS UI**: Handles API calls, filtering, and on-screen display.

## Installation and Setup Instructions

### Prerequisites
- **PHP 8+**: Used for the lightweight alert endpoint (`api/send-alerts.php`).
- **Google Maps JavaScript API key**: Required to render the map.
- **Twilio/Email Service (Planned)**: SMS/email integrations are not wired yet.

### Steps to Set Up
1. **Clone the Repository**  
   Run the following command in your terminal to clone the project:
   ```bash
   git clone https://github.com/Rohith-R777/smart-emergency-sos-system.git
   cd smart-emergency-sos-system
   ```  

2. **Add your Maps API key**  
   Replace `YOUR_API_KEY` in `index.html` with your Google Maps JavaScript API key.

3. **Run the Application**  
   Start a PHP development server in the project root:
   ```bash
   php -S localhost:8000
   ```  
   The application will be running on `http://localhost:8000/index.html`.

4. **Testing the Application**  
   Trigger the SOS feature and confirm an entry is appended to `api/alerts.log`.

## Usage Instructions
- To send emergency notifications, simply press the 'SOS' button within the application. This will trigger the alert process.
- Users can also specify which contacts they want to alert in the settings section.
- Alert messages recorded by the MVP endpoint are limited to 280 characters.

## Contributions
Contributions to the Emergency SOS System are welcome! Feel free to raise pull requests.
