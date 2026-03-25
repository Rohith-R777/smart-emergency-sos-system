#!/usr/bin/env python3
"""Generate a comprehensive PDF project report for Smart Emergency SOS System."""

from fpdf import FPDF


class ProjectReport(FPDF):
    """Custom PDF class for the project report."""

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(211, 47, 47)
        self.cell(0, 8, "Smart Emergency SOS System - Project Report", align="C", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def chapter_title(self, number, title):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(211, 47, 47)
        self.cell(0, 10, f"{number}. {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(211, 47, 47)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(21, 101, 192)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def subsection_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(66, 66, 66)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 33, 33)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet_point(self, text, indent=10):
        x = self.get_x()
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 33, 33)
        self.cell(indent, 5.5, "-")
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def table_header(self, headers, widths):
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(244, 67, 54)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, border=1, fill=True, align="C")
        self.ln()

    def table_row(self, cells, widths, fill=False):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(33, 33, 33)
        if fill:
            self.set_fill_color(245, 245, 245)
        for i, cell in enumerate(cells):
            self.cell(widths[i], 6, cell, border=1, fill=fill, align="L")
        self.ln()


def generate_report():
    pdf = ProjectReport()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # ========== TITLE PAGE ==========
    pdf.add_page()
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(211, 47, 47)
    pdf.cell(0, 15, "Smart Emergency", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 15, "SOS System", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_draw_color(211, 47, 47)
    pdf.set_line_width(1)
    pdf.line(60, pdf.get_y(), pdf.w - 60, pdf.get_y())
    pdf.ln(10)

    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(66, 66, 66)
    pdf.cell(0, 10, "Comprehensive Project Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)

    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Author: Rohith R", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Repository: Rohith-R777/smart-emergency-sos-system", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "License: MIT License", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Date: March 2026", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(30)

    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 8, "A web-based emergency notification system for immediate assistance", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "during emergency situations using real-time location tracking,", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "multi-channel alerts, and nearby resource discovery.", align="C", new_x="LMARGIN", new_y="NEXT")

    # ========== TABLE OF CONTENTS ==========
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(211, 47, 47)
    pdf.cell(0, 12, "Table of Contents", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    toc_items = [
        ("1", "Introduction & Overview"),
        ("2", "Project Planning"),
        ("3", "System Architecture"),
        ("4", "Technology Stack"),
        ("5", "Project Structure"),
        ("6", "Feature Details"),
        ("7", "Database Design"),
        ("8", "UI/UX Design"),
        ("9", "API & Integration Details"),
        ("10", "Security Analysis"),
        ("11", "Testing & Quality Assurance"),
        ("12", "Deployment Guide"),
        ("13", "Future Enhancements"),
        ("14", "Conclusion"),
    ]
    for num, title in toc_items:
        pdf.set_font("Helvetica", "", 12)
        pdf.set_text_color(33, 33, 33)
        pdf.cell(15, 8, num + ".")
        pdf.set_font("Helvetica", "", 12)
        pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # ========== 1. INTRODUCTION ==========
    pdf.add_page()
    pdf.chapter_title("1", "Introduction & Overview")

    pdf.section_title("1.1 Project Background")
    pdf.body_text(
        "The Smart Emergency SOS System is a web-based application designed to provide "
        "immediate assistance during emergency situations. In critical moments, every second "
        "counts. This system enables users to send instant emergency alerts to pre-defined "
        "contacts and emergency services with a single button press, while simultaneously "
        "sharing their real-time location."
    )

    pdf.section_title("1.2 Problem Statement")
    pdf.body_text(
        "During emergencies, people often struggle to communicate their location and the "
        "nature of the emergency effectively. Traditional methods of calling emergency "
        "services can be slow, and providing accurate location information under stress is "
        "challenging. There is a need for a streamlined, one-touch emergency notification "
        "system that automatically shares location data and finds nearby emergency resources."
    )

    pdf.section_title("1.3 Objectives")
    pdf.bullet_point("Provide a one-click SOS alert system for emergency situations")
    pdf.bullet_point("Track and share the user's real-time location automatically")
    pdf.bullet_point("Send multi-channel notifications (SMS, Email) to emergency contacts")
    pdf.bullet_point("Discover nearby hospitals, police stations, and fire stations")
    pdf.bullet_point("Offer an admin dashboard for monitoring and managing emergency requests")
    pdf.bullet_point("Manage emergency responder assignments and availability")

    pdf.section_title("1.4 Scope")
    pdf.body_text(
        "The system covers emergency alert notification via SMS and email, real-time GPS "
        "location tracking using the Browser Geolocation API, nearby emergency resource "
        "discovery using Google Maps Places API (within a 5 km radius), an admin dashboard "
        "for monitoring SOS requests, and a MySQL database for persistent data storage. "
        "The project serves both end-users (people in emergencies) and administrators "
        "(emergency coordinators/responders)."
    )

    # ========== 2. PROJECT PLANNING ==========
    pdf.add_page()
    pdf.chapter_title("2", "Project Planning")

    pdf.section_title("2.1 Development Methodology")
    pdf.body_text(
        "The project follows an Agile development approach with iterative feature delivery. "
        "Features are developed in incremental phases, allowing for continuous testing and "
        "refinement. Each phase builds upon the previous one, ensuring a stable foundation."
    )

    pdf.section_title("2.2 Development Phases")

    pdf.subsection_title("Phase 1: Foundation & Core UI")
    pdf.bullet_point("Project setup and repository initialization")
    pdf.bullet_point("HTML5 structure for main SOS interface (index.html)")
    pdf.bullet_point("CSS3 styling with emergency-themed color scheme (styles.css)")
    pdf.bullet_point("Basic SOS button functionality")

    pdf.subsection_title("Phase 2: Map Integration & Location Tracking")
    pdf.bullet_point("Google Maps JavaScript API integration")
    pdf.bullet_point("Browser Geolocation API for real-time position tracking")
    pdf.bullet_point("User location marker on interactive map")
    pdf.bullet_point("Map initialization and centering logic")

    pdf.subsection_title("Phase 3: Nearby Places Feature")
    pdf.bullet_point("Google Maps Places API (Nearby Search) integration")
    pdf.bullet_point("Search for hospitals, police stations, and fire stations")
    pdf.bullet_point("Color-coded markers and info windows on map")
    pdf.bullet_point("Styled results list with ratings and open/closed status")

    pdf.subsection_title("Phase 4: Backend & Notification System")
    pdf.bullet_point("PHP backend API for sending alerts (api/send-alerts.php)")
    pdf.bullet_point("Twilio SMS integration for emergency notifications")
    pdf.bullet_point("Email service integration (SendGrid/SMTP)")
    pdf.bullet_point("Multi-recipient notification support")

    pdf.subsection_title("Phase 5: Database & Admin Dashboard")
    pdf.bullet_point("MySQL database schema design (5 tables)")
    pdf.bullet_point("Admin dashboard UI (dashboard.html)")
    pdf.bullet_point("SOS request monitoring and statistics")
    pdf.bullet_point("Responder management and assignment tracking")

    pdf.section_title("2.3 Timeline Estimate")
    widths = [40, 75, 75]
    pdf.table_header(["Phase", "Description", "Duration"], widths)
    rows = [
        ["Phase 1", "Foundation & Core UI", "1 Week"],
        ["Phase 2", "Map & Location Tracking", "1 Week"],
        ["Phase 3", "Nearby Places Feature", "1-2 Weeks"],
        ["Phase 4", "Backend & Notifications", "1-2 Weeks"],
        ["Phase 5", "Database & Dashboard", "1-2 Weeks"],
        ["Testing", "Integration & User Testing", "1 Week"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    # ========== 3. SYSTEM ARCHITECTURE ==========
    pdf.add_page()
    pdf.chapter_title("3", "System Architecture")

    pdf.section_title("3.1 High-Level Architecture")
    pdf.body_text(
        "The Smart Emergency SOS System follows a multi-tier architecture with clear "
        "separation between the presentation layer (frontend), business logic layer "
        "(JavaScript + PHP backend), and data layer (MySQL database). External services "
        "(Google Maps, Twilio, Email) are integrated via APIs."
    )

    pdf.section_title("3.2 Architecture Layers")

    pdf.subsection_title("Presentation Layer (Client-Side)")
    pdf.bullet_point("index.html - Main user interface with SOS button, map, and nearby results")
    pdf.bullet_point("dashboard.html - Admin monitoring dashboard with statistics and request table")
    pdf.bullet_point("styles.css - Complete CSS3 styling with responsive flexbox layouts")
    pdf.bullet_point("jQuery 3.6.0 - Client-side DOM manipulation library")

    pdf.subsection_title("Application Logic Layer")
    pdf.bullet_point("script.js - Core JavaScript engine (242 lines) handling geolocation, map operations, and Places API calls")
    pdf.bullet_point("api/send-alerts.php - Backend notification gateway for SMS and email delivery")

    pdf.subsection_title("External Services Layer")
    pdf.bullet_point("Google Maps JavaScript API - Interactive map rendering and marker management")
    pdf.bullet_point("Google Maps Places API - Nearby Search for emergency resources")
    pdf.bullet_point("Browser Geolocation API - GPS coordinate retrieval")
    pdf.bullet_point("Twilio API - SMS notification delivery")
    pdf.bullet_point("SendGrid/SMTP - Email notification delivery")

    pdf.subsection_title("Data Layer")
    pdf.bullet_point("MySQL Database - 5 relational tables for users, emergencies, alerts, responders, and assignments")
    pdf.bullet_point("Foreign key relationships with CASCADE delete for referential integrity")

    pdf.section_title("3.3 Data Flow")
    pdf.body_text(
        "1. User presses the SOS button on index.html.\n"
        "2. Browser Geolocation API retrieves the user's GPS coordinates.\n"
        "3. Location is displayed on the Google Maps interactive map.\n"
        "4. Alert request is sent to api/send-alerts.php.\n"
        "5. Backend dispatches SMS via Twilio and email via SendGrid/SMTP.\n"
        "6. Emergency record is stored in the MySQL Emergencies table.\n"
        "7. Alert record is logged in the Alerts table.\n"
        "8. Admin dashboard reflects updated statistics and new request."
    )

    # ========== 4. TECHNOLOGY STACK ==========
    pdf.add_page()
    pdf.chapter_title("4", "Technology Stack")

    pdf.section_title("4.1 Frontend Technologies")
    widths = [50, 60, 80]
    pdf.table_header(["Technology", "Version", "Purpose"], widths)
    rows = [
        ["HTML5", "5", "Page structure and semantic markup"],
        ["CSS3", "3", "Styling, flexbox layouts, animations"],
        ["JavaScript", "ES5", "Core application logic and DOM manipulation"],
        ["jQuery", "3.6.0", "Utility library for DOM/AJAX operations"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("4.2 APIs & External Services")
    widths = [55, 55, 80]
    pdf.table_header(["Service", "Type", "Purpose"], widths)
    rows = [
        ["Google Maps JS API", "Client-side", "Interactive map rendering & markers"],
        ["Google Places API", "Client-side", "Nearby Search for emergency resources"],
        ["Geolocation API", "Browser API", "GPS coordinate retrieval"],
        ["Twilio", "REST API", "SMS emergency notifications"],
        ["SendGrid/SMTP", "Email API", "Email emergency notifications"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("4.3 Backend & Database")
    widths = [50, 60, 80]
    pdf.table_header(["Technology", "Type", "Purpose"], widths)
    rows = [
        ["PHP", "Server-side", "Backend alert notification gateway"],
        ["MySQL", "Database", "Relational data storage (5 tables)"],
        ["Node.js", "Runtime", "Server execution environment"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("4.4 Technologies Used in Nearby Places Feature")
    pdf.body_text(
        "The Nearby Places feature is a key component that enables users to find nearby "
        "emergency resources. The following technologies power this feature:"
    )
    widths = [55, 135]
    pdf.table_header(["Technology", "Purpose in Nearby Places"], widths)
    rows = [
        ["HTML5", "Results container structure and list elements"],
        ["CSS3", "Section cards, rating badges, open/closed status badges"],
        ["Vanilla JavaScript", "Geolocation calls, API requests, DOM rendering"],
        ["Google Maps JS API", "Map markers, info windows, map centering"],
        ["Google Places API", "nearbySearch for hospital, police, fire_station"],
        ["Geolocation API", "User position (latitude, longitude)"],
        ["Google Maps Markers", "Color-coded pins (red, blue, orange)"],
        ["Google InfoWindows", "Popup details on marker click"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    # ========== 5. PROJECT STRUCTURE ==========
    pdf.add_page()
    pdf.chapter_title("5", "Project Structure")

    pdf.section_title("5.1 Directory Layout")
    pdf.set_font("Courier", "", 10)
    pdf.set_text_color(33, 33, 33)
    tree = (
        "smart-emergency-sos-system/\n"
        "|-- LICENSE                    MIT License\n"
        "|-- README.md                  Project documentation\n"
        "|-- index.html                 Main user SOS interface\n"
        "|-- dashboard.html             Admin monitoring dashboard\n"
        "|-- script.js                  Core JavaScript logic (242 lines)\n"
        "|-- styles.css                 UI styling (114 lines)\n"
        "|-- database_schema.sql        MySQL schema (5 tables)\n"
        "|-- generate_report.py         Report generation script\n"
        "'-- api/\n"
        "    '-- send-alerts.php        Alert notification backend\n"
    )
    pdf.multi_cell(0, 5, tree)
    pdf.ln(4)

    pdf.section_title("5.2 File Descriptions")
    widths = [45, 30, 115]
    pdf.table_header(["File", "Type", "Description"], widths)
    rows = [
        ["index.html", "HTML", "Main SOS UI with map, buttons, and nearby results"],
        ["dashboard.html", "HTML", "Admin dashboard with stats and request history"],
        ["script.js", "JavaScript", "Core logic: geolocation, maps, places search, markers"],
        ["styles.css", "CSS", "Emergency-themed styling with nearby places styles"],
        ["database_schema.sql", "SQL", "MySQL schema: Users, Emergencies, Alerts, Responders"],
        ["send-alerts.php", "PHP", "Backend gateway for SMS and email notifications"],
        ["README.md", "Markdown", "Setup instructions and technology documentation"],
        ["LICENSE", "Text", "MIT License (Copyright 2026 Rohith R)"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    # ========== 6. FEATURE DETAILS ==========
    pdf.add_page()
    pdf.chapter_title("6", "Feature Details")

    pdf.section_title("6.1 SOS Emergency Alert")
    pdf.body_text(
        "The core feature of the system is the one-click SOS emergency alert. When a user "
        "presses the prominent green SOS button on the main interface, the system immediately "
        "triggers an alert notification workflow. The alert message is displayed to the user "
        "('Alert sent! Help is on the way!'), and the backend sends SMS and email "
        "notifications to all pre-configured emergency contacts simultaneously."
    )

    pdf.section_title("6.2 Real-Time Location Tracking")
    pdf.body_text(
        "The system uses the HTML5 Browser Geolocation API (navigator.geolocation) to "
        "retrieve the user's current GPS coordinates (latitude and longitude). The location "
        "is then displayed on an interactive Google Map as a blue circular marker. The map "
        "automatically centers on the user's position to provide spatial context. Location "
        "data is shared with emergency services to enable rapid response."
    )

    pdf.section_title("6.3 Nearby Emergency Resources Discovery")
    pdf.body_text(
        "The Find Nearby Resources feature uses the Google Maps Places API (Nearby Search) "
        "to search for emergency resources within a 5 km radius of the user's current "
        "location. The system searches for three types of emergency resources:"
    )
    pdf.bullet_point("Hospitals - Displayed with red markers on the map")
    pdf.bullet_point("Police Stations - Displayed with blue markers on the map")
    pdf.bullet_point("Fire Stations - Displayed with orange markers on the map")
    pdf.body_text(
        "Results are shown both as interactive markers on the map (with clickable info "
        "windows showing name, address, and rating) and as a styled list below the map. "
        "Each list entry shows the place name, address/vicinity, Google rating (out of 5), "
        "and current open/closed status with color-coded badges."
    )

    pdf.section_title("6.4 Multi-Channel Alert Notifications")
    pdf.body_text(
        "The alert notification system supports two communication channels:\n"
        "- SMS Notifications: Sent via the Twilio API to phone numbers of emergency contacts.\n"
        "- Email Notifications: Sent via SendGrid or SMTP to email addresses of contacts.\n"
        "Both channels are triggered simultaneously through the PHP backend "
        "(api/send-alerts.php), which accepts an alert message along with arrays of phone "
        "numbers and email addresses."
    )

    pdf.section_title("6.5 Admin Dashboard")
    pdf.body_text(
        "The admin dashboard (dashboard.html) provides emergency coordinators with a "
        "monitoring interface. It displays key statistics (Total SOS Requests, Active "
        "Volunteers), a table of recent SOS requests with ID, timestamp, location, and "
        "status (Resolved/Pending), and navigation controls for managing the system."
    )

    pdf.section_title("6.6 Responder Management")
    pdf.body_text(
        "The database design supports full responder lifecycle management including "
        "responder registration (name, phone number), availability tracking "
        "(available/busy status), emergency assignment mapping, and timestamped "
        "response records for audit purposes."
    )

    # ========== 7. DATABASE DESIGN ==========
    pdf.add_page()
    pdf.chapter_title("7", "Database Design")

    pdf.section_title("7.1 Entity-Relationship Overview")
    pdf.body_text(
        "The database consists of 5 normalized tables with foreign key relationships. "
        "The Users table is the central entity, linked to Emergencies. Emergencies are "
        "linked to both Alerts (notification records) and Response_Assignments (responder "
        "assignments). The Responders table tracks emergency personnel availability."
    )

    pdf.section_title("7.2 Table: Users")
    widths = [40, 40, 50, 60]
    pdf.table_header(["Column", "Type", "Constraints", "Description"], widths)
    rows = [
        ["user_id", "INT", "PK, AUTO_INCREMENT", "Unique user identifier"],
        ["username", "VARCHAR(100)", "NOT NULL", "User display name"],
        ["password", "VARCHAR(255)", "NOT NULL", "Hashed password"],
        ["email", "VARCHAR(100)", "NOT NULL", "User email address"],
        ["phone_number", "VARCHAR(15)", "NOT NULL", "Contact phone number"],
        ["created_at", "TIMESTAMP", "DEFAULT NOW()", "Account creation time"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("7.3 Table: Emergencies")
    rows = [
        ["emergency_id", "INT", "PK, AUTO_INCREMENT", "Unique emergency ID"],
        ["user_id", "INT", "FK -> Users", "Reporting user"],
        ["emergency_type", "VARCHAR(50)", "NOT NULL", "Type of emergency"],
        ["description", "TEXT", "", "Detailed description"],
        ["location", "VARCHAR(255)", "NOT NULL", "GPS coordinates/address"],
        ["status", "ENUM", "reported/in_progress/resolved", "Current status"],
        ["created_at", "TIMESTAMP", "DEFAULT NOW()", "Report timestamp"],
    ]
    pdf.table_header(["Column", "Type", "Constraints", "Description"], widths)
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("7.4 Table: Alerts")
    rows = [
        ["alert_id", "INT", "PK, AUTO_INCREMENT", "Unique alert ID"],
        ["emergency_id", "INT", "FK -> Emergencies", "Related emergency"],
        ["alert_message", "TEXT", "NOT NULL", "Notification content"],
        ["timestamp", "TIMESTAMP", "DEFAULT NOW()", "Alert sent time"],
    ]
    pdf.table_header(["Column", "Type", "Constraints", "Description"], widths)
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("7.5 Table: Responders")
    rows = [
        ["responder_id", "INT", "PK, AUTO_INCREMENT", "Unique responder ID"],
        ["responder_name", "VARCHAR(100)", "NOT NULL", "Full name"],
        ["phone_number", "VARCHAR(15)", "NOT NULL", "Contact number"],
        ["status", "ENUM", "available/busy", "Current availability"],
    ]
    pdf.table_header(["Column", "Type", "Constraints", "Description"], widths)
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("7.6 Table: Response_Assignments")
    rows = [
        ["assignment_id", "INT", "PK, AUTO_INCREMENT", "Unique assignment ID"],
        ["emergency_id", "INT", "FK -> Emergencies", "Assigned emergency"],
        ["responder_id", "INT", "FK -> Responders", "Assigned responder"],
        ["timestamp", "TIMESTAMP", "DEFAULT NOW()", "Assignment time"],
    ]
    pdf.table_header(["Column", "Type", "Constraints", "Description"], widths)
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    # ========== 8. UI/UX DESIGN ==========
    pdf.add_page()
    pdf.chapter_title("8", "UI/UX Design")

    pdf.section_title("8.1 Design Philosophy")
    pdf.body_text(
        "The UI follows an emergency-first design principle where the most critical "
        "action (SOS button) is prominently placed and immediately accessible. The visual "
        "hierarchy prioritizes urgency, clarity, and speed of interaction. Red is used as "
        "the primary brand color to convey emergency and urgency."
    )

    pdf.section_title("8.2 Color Scheme")
    widths = [45, 45, 100]
    pdf.table_header(["Color", "Hex Code", "Usage"], widths)
    rows = [
        ["Primary Red", "#f44336", "Headers, section borders, emergency branding"],
        ["Dark Red", "#d32f2f / #b71c1c", "SOS button and hover states"],
        ["Action Green", "green", "SOS trigger button (positive action)"],
        ["Blue", "#1565C0", "Find Nearby Resources button"],
        ["Blue (hover)", "#0D47A1", "Button hover state"],
        ["Light Gray", "#fafafa", "Result card backgrounds"],
        ["Dark Text", "#212121", "Primary text content"],
        ["Orange", "#ff9800", "Rating badge color"],
        ["Status Green", "#2e7d32", "'Open Now' status badge"],
        ["Status Red", "#c62828", "'Closed' status badge"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(4)
    pdf.section_title("8.3 Layout Structure")
    pdf.body_text(
        "Main Interface (index.html):\n"
        "- Full-width red header bar with project title\n"
        "- Container with 20px padding for main content\n"
        "- SOS button (green, 20px font) positioned at top\n"
        "- Find Nearby Resources button (blue, 16px font) adjacent to SOS\n"
        "- Interactive Google Map (100% width, 400px height)\n"
        "- Alert confirmation banner (yellow background, hidden by default)\n"
        "- Nearby results container with styled section cards\n"
        "- Features section listing system capabilities"
    )

    pdf.section_title("8.4 Responsive Design")
    pdf.body_text(
        "The interface uses modern CSS features for responsiveness:\n"
        "- Viewport meta tag for mobile device scaling\n"
        "- Flexbox layouts with flex-wrap for result items\n"
        "- Full-width map container (100% width)\n"
        "- Inline-block buttons with appropriate margins\n"
        "- Text wrapping and padding for mobile readability"
    )

    pdf.section_title("8.5 Visual Feedback")
    pdf.bullet_point("Button hover effects: Color transitions (0.3s) for SOS and nearby buttons")
    pdf.bullet_point("Status badges: Green 'Open Now' / Red 'Closed' pills with background colors")
    pdf.bullet_point("Rating badges: Orange pill-shaped indicators with rating score")
    pdf.bullet_point("Map markers: Color-coded pins (red=hospital, blue=police, orange=fire)")
    pdf.bullet_point("Info windows: Popup details on map marker click with place details")
    pdf.bullet_point("Alert banner: Yellow confirmation banner after SOS activation")

    # ========== 9. API & INTEGRATION DETAILS ==========
    pdf.add_page()
    pdf.chapter_title("9", "API & Integration Details")

    pdf.section_title("9.1 Google Maps JavaScript API")
    pdf.body_text(
        "The Google Maps JavaScript API is loaded via a script tag in index.html with the "
        "Places library enabled (&libraries=places). The initMap() function initializes the "
        "map centered on a default location with zoom level 15. The API provides map "
        "rendering, marker creation, info window popups, and event handling for user "
        "interaction with map elements."
    )

    pdf.section_title("9.2 Google Maps Places API (Nearby Search)")
    pdf.body_text(
        "The Places API Nearby Search is used to find emergency resources. A "
        "PlacesService instance is created from the map object, and nearbySearch() is "
        "called with parameters: location (user coordinates), radius (5000 meters), and "
        "type (hospital, police, or fire_station). Results include place name, vicinity, "
        "geometry (coordinates), rating, and opening_hours."
    )

    pdf.section_title("9.3 Browser Geolocation API")
    pdf.body_text(
        "The HTML5 Geolocation API (navigator.geolocation.getCurrentPosition) retrieves "
        "the user's GPS coordinates. It requires explicit user permission and provides "
        "latitude and longitude in the success callback. Error handling is implemented "
        "for browsers that don't support geolocation or when the user denies permission."
    )

    pdf.section_title("9.4 Twilio SMS Integration")
    pdf.body_text(
        "SMS notifications are configured through environment variables:\n"
        "- TWILIO_ACCOUNT_SID: Twilio account identifier\n"
        "- TWILIO_AUTH_TOKEN: Authentication token\n"
        "- TWILIO_PHONE_NUMBER: Sender phone number\n"
        "The send_sms() function in send-alerts.php dispatches messages to emergency "
        "contacts via the Twilio REST API."
    )

    pdf.section_title("9.5 Email Service Integration")
    pdf.body_text(
        "Email notifications support SendGrid or SMTP configuration:\n"
        "- EMAIL_SERVICE: Service provider identifier\n"
        "- EMAIL_USER: Email account username\n"
        "- EMAIL_PASS: Email account password\n"
        "The send_email() function handles email delivery to multiple recipients "
        "with the emergency alert message."
    )

    pdf.section_title("9.6 jQuery CDN Integration")
    pdf.body_text(
        "jQuery 3.6.0 is loaded from the official jQuery CDN with Subresource Integrity "
        "(SRI) verification (sha256 hash) and crossorigin='anonymous' attribute to ensure "
        "the loaded script has not been tampered with. This provides a secure foundation "
        "for DOM manipulation and potential AJAX operations."
    )

    # ========== 10. SECURITY ANALYSIS ==========
    pdf.add_page()
    pdf.chapter_title("10", "Security Analysis")

    pdf.section_title("10.1 Implemented Security Measures")
    pdf.bullet_point("Subresource Integrity (SRI) on jQuery CDN - Prevents script tampering")
    pdf.bullet_point("HTTPS icon URLs for map markers - Prevents mixed content issues")
    pdf.bullet_point("Environment variable configuration for API keys and credentials")
    pdf.bullet_point("Foreign key constraints with CASCADE delete for database integrity")
    pdf.bullet_point("Password field (VARCHAR 255) sized for bcrypt hash storage")
    pdf.bullet_point("Browser permission prompt for geolocation access")

    pdf.section_title("10.2 Areas for Improvement")
    pdf.bullet_point("API key management: Replace YOUR_API_KEY placeholder with secure key rotation")
    pdf.bullet_point("Authentication: Add user login/session management for SOS access")
    pdf.bullet_point("HTTPS enforcement: Require TLS/SSL for all connections")
    pdf.bullet_point("Input validation: Server-side validation of all user inputs")
    pdf.bullet_point("Rate limiting: Throttle SOS button to prevent alert spam")
    pdf.bullet_point("CORS protection: Restrict API access to authorized origins")
    pdf.bullet_point("CSRF tokens: Protect form submissions from cross-site forgery")
    pdf.bullet_point("Prepared statements: Use parameterized SQL queries in PHP")
    pdf.bullet_point("Audit logging: Log all system actions for security review")

    # ========== 11. TESTING & QA ==========
    pdf.add_page()
    pdf.chapter_title("11", "Testing & Quality Assurance")

    pdf.section_title("11.1 Testing Strategy")
    pdf.body_text(
        "Due to the nature of the project (emergency response system), testing should "
        "cover functional correctness, integration reliability, and user experience under "
        "stress conditions. The following testing approaches are recommended:"
    )

    pdf.subsection_title("Manual Testing")
    pdf.bullet_point("SOS button activation and alert display verification")
    pdf.bullet_point("Geolocation permission flow testing (grant/deny scenarios)")
    pdf.bullet_point("Google Maps loading and marker placement verification")
    pdf.bullet_point("Nearby places search across different locations")
    pdf.bullet_point("Dashboard statistics and table rendering")
    pdf.bullet_point("Cross-browser compatibility (Chrome, Firefox, Safari, Edge)")
    pdf.bullet_point("Mobile responsiveness and touch interaction testing")

    pdf.subsection_title("Integration Testing")
    pdf.bullet_point("Twilio SMS delivery end-to-end verification")
    pdf.bullet_point("Email notification delivery confirmation")
    pdf.bullet_point("Google Maps API response handling (success/failure)")
    pdf.bullet_point("Database CRUD operations for all 5 tables")

    pdf.section_title("11.2 Code Quality")
    pdf.body_text(
        "The codebase uses consistent coding patterns including function-scoped variables, "
        "IIFE closures for marker event handlers, null-safe property access, and clear "
        "function naming conventions. Helper functions are extracted to reduce duplication "
        "(e.g., createOrUpdateUserMarker)."
    )

    # ========== 12. DEPLOYMENT GUIDE ==========
    pdf.add_page()
    pdf.chapter_title("12", "Deployment Guide")

    pdf.section_title("12.1 Prerequisites")
    pdf.bullet_point("Node.js installed (https://nodejs.org)")
    pdf.bullet_point("npm package manager")
    pdf.bullet_point("MySQL database server")
    pdf.bullet_point("PHP runtime environment")
    pdf.bullet_point("Web server (Apache/Nginx)")
    pdf.bullet_point("Google Maps API key with Maps and Places APIs enabled")
    pdf.bullet_point("Twilio account with Account SID, Auth Token, and Phone Number")
    pdf.bullet_point("Email service credentials (SendGrid or SMTP)")

    pdf.section_title("12.2 Installation Steps")
    pdf.body_text(
        "1. Clone the repository:\n"
        "   git clone https://github.com/Rohith-R777/smart-emergency-sos-system.git\n"
        "   cd smart-emergency-sos-system\n\n"
        "2. Install dependencies:\n"
        "   npm install\n\n"
        "3. Create .env file with environment variables:\n"
        "   TWILIO_ACCOUNT_SID=your_twilio_account_sid\n"
        "   TWILIO_AUTH_TOKEN=your_twilio_auth_token\n"
        "   TWILIO_PHONE_NUMBER=your_twilio_phone_number\n"
        "   EMAIL_SERVICE=your_email_service\n"
        "   EMAIL_USER=your_email\n"
        "   EMAIL_PASS=your_email_password\n\n"
        "4. Import database schema:\n"
        "   mysql -u root -p < database_schema.sql\n\n"
        "5. Replace YOUR_API_KEY in index.html with your Google Maps API key.\n\n"
        "6. Start the application:\n"
        "   npm start\n\n"
        "7. Access the application at http://localhost:3000"
    )

    # ========== 13. FUTURE ENHANCEMENTS ==========
    pdf.add_page()
    pdf.chapter_title("13", "Future Enhancements")

    pdf.section_title("13.1 Planned Features")
    pdf.bullet_point("User authentication and registration system with JWT tokens")
    pdf.bullet_point("Push notifications via Web Push API for real-time updates")
    pdf.bullet_point("Progressive Web App (PWA) support for offline capability")
    pdf.bullet_point("Voice-activated SOS trigger using Web Speech API")
    pdf.bullet_point("Emergency type categorization (medical, fire, crime, accident)")
    pdf.bullet_point("Photo and video attachment for emergency reports")
    pdf.bullet_point("Real-time responder tracking on the map")
    pdf.bullet_point("Historical emergency data analytics and heat maps")
    pdf.bullet_point("Integration with national emergency services (911/112)")
    pdf.bullet_point("Multi-language support for international deployment")

    pdf.section_title("13.2 Technical Improvements")
    pdf.bullet_point("Migrate to React or Vue.js for scalable component architecture")
    pdf.bullet_point("Add Node.js/Express backend replacing PHP for unified stack")
    pdf.bullet_point("Implement WebSocket for real-time bidirectional communication")
    pdf.bullet_point("Add comprehensive automated test suite (Jest, Cypress)")
    pdf.bullet_point("CI/CD pipeline with GitHub Actions for automated deployments")
    pdf.bullet_point("Docker containerization for consistent deployment")
    pdf.bullet_point("Cloud deployment on AWS/GCP/Azure with auto-scaling")
    pdf.bullet_point("API rate limiting and request throttling")
    pdf.bullet_point("Database migration to PostgreSQL for advanced features")

    # ========== 14. CONCLUSION ==========
    pdf.add_page()
    pdf.chapter_title("14", "Conclusion")

    pdf.body_text(
        "The Smart Emergency SOS System is a comprehensive web-based application designed "
        "to address the critical need for rapid emergency response. By combining real-time "
        "location tracking, multi-channel alert notifications, and nearby emergency resource "
        "discovery, the system provides a complete emergency assistance platform."
    )

    pdf.body_text(
        "The project leverages modern web technologies including HTML5, CSS3, JavaScript, "
        "Google Maps JavaScript API, Google Maps Places API, Browser Geolocation API, "
        "jQuery, PHP, and MySQL to deliver a functional emergency response system. The "
        "frontend provides an intuitive, emergency-first interface with a prominent SOS "
        "button and interactive map. The backend supports multi-channel notifications via "
        "Twilio SMS and email services. The database layer ensures persistent storage of "
        "users, emergencies, alerts, and responder assignments."
    )

    pdf.body_text(
        "Key achievements of the project include:\n"
        "- One-click SOS emergency alert with instant notification delivery\n"
        "- Real-time GPS location tracking and sharing via Browser Geolocation API\n"
        "- Nearby emergency resource discovery (hospitals, police, fire stations) within "
        "5 km using Google Maps Places API with color-coded map markers\n"
        "- Admin dashboard for monitoring and managing emergency requests\n"
        "- Relational database design with 5 normalized tables and foreign key integrity\n"
        "- Responsive UI with emergency-themed design and visual feedback"
    )

    pdf.body_text(
        "The system demonstrates a practical application of web technologies for social "
        "good, addressing a real-world problem of emergency response efficiency. With the "
        "planned future enhancements, including PWA support, voice activation, and real-time "
        "responder tracking, the system has strong potential for growth into a production-"
        "ready emergency assistance platform."
    )

    pdf.ln(8)
    pdf.set_draw_color(211, 47, 47)
    pdf.set_line_width(0.5)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(6)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "End of Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "Smart Emergency SOS System - Project Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "Author: Rohith R | License: MIT | March 2026", align="C", new_x="LMARGIN", new_y="NEXT")

    # Save the PDF in the same directory as this script
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "Smart_Emergency_SOS_System_Project_Report.pdf")
    pdf.output(output_path)
    print(f"Report generated successfully: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_report()
