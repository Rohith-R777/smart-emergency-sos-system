# Emergency SOS System

## Overview
The Emergency SOS System is designed to provide immediate assistance in emergency situations by notifying pre-defined contacts and utilizing various communication methods to ensure help arrives swiftly.

## Features
- **Instant Notifications**: Sends alerts to emergency contacts via SMS and email.
- **Location Tracking**: Shares the user's location with emergency services.
- **User-Friendly Interface**: Easy to use application for both users and responders.
- **Multiple Communication Channels**: Supports SMS, email, and emergency calls.

## Installation and Setup Instructions

### Prerequisites
- **Node.js**: Ensure you have Node.js installed. You can download it from [Node.js Official Website](https://nodejs.org/).
- **npm**: npm comes with Node.js installation.
- **Twilio Account**: Sign up for a Twilio account for SMS notifications. Obtain your Account SID, Auth Token, and a Twilio phone number.
- **Email Service**: Set up an email service, such as SendGrid or SMTP, for sending email notifications.

### Steps to Set Up
1. **Clone the Repository**  
   Run the following command in your terminal to clone the project:
   ```bash
   git clone https://github.com/Rohith-R777/smart-emergency-sos-system.git
   cd smart-emergency-sos-system
   ```  

2. **Install Dependencies**  
   Install the necessary packages with npm:
   ```bash
   npm install
   ```  

3. **Configure Environment Variables**  
   Create a `.env` file in the root directory of the project and add the following variables:
   ```env
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   EMAIL_SERVICE=your_email_service
   EMAIL_USER=your_email
   EMAIL_PASS=your_email_password
   ```  

4. **Run the Application**  
   Start the server:
   ```bash
   npm start
   ```  
   The application will be running on `http://localhost:3000`.

5. **Testing the Application**  
   You can test the application by triggering the SOS feature and ensuring notifications are being sent correctly.

## Usage Instructions
- To send emergency notifications, simply press the 'SOS' button within the application. This will trigger the alert process.
- Users can also specify which contacts they want to alert in the settings section.

## Contributions
Contributions to the Emergency SOS System are welcome! Feel free to raise pull requests.

## Technologies Used in Nearby Places Feature

The **Nearby Places** feature helps users find emergency resources (hospitals, police stations, and fire stations) close to their current location. Below are the technologies used to build this feature:

| Technology | Purpose |
|---|---|
| **HTML5** | Structure and layout of the nearby places UI, including the results container and list elements |
| **CSS3** | Styling for the nearby places results, section cards, badges (open/closed status, ratings), and responsive layout |
| **JavaScript (Vanilla JS)** | Core logic for geolocation requests, API calls, DOM manipulation, and rendering results dynamically |
| **Google Maps JavaScript API** | Renders the interactive map, places markers for found locations, and displays info windows on marker click |
| **Google Maps Places API (Nearby Search)** | Searches for nearby places by type (hospital, police, fire_station) within a specified radius of the user's location |
| **Browser Geolocation API** | Retrieves the user's current latitude and longitude coordinates using the browser's built-in `navigator.geolocation` |
| **Google Maps Markers & InfoWindows** | Displays location pins on the map with clickable info popups showing place name, address, and rating |
| **jQuery 3.6.0** | Included for potential DOM manipulation and AJAX support |

### How It Works
1. The user clicks the **"Find Nearby Resources"** button.
2. The **Browser Geolocation API** (`navigator.geolocation`) retrieves the user's current GPS coordinates.
3. The map centers on the user's location using the **Google Maps JavaScript API**.
4. The **Google Maps Places API (Nearby Search)** is called for each emergency resource type (hospital, police, fire_station) within a 5 km radius.
5. Results are displayed both as **markers on the map** (with clickable info windows) and as a **styled list** below the map showing name, address, rating, and open/closed status.