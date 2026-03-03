// script.js

// Google Maps integration
function initMap() {
    const options = {
        zoom: 15,
        center: { lat: -34.397, lng: 150.644 }  // Example location
    };
    const map = new google.maps.Map(document.getElementById('map'), options);
}

// SOS button trigger
function triggerSOS() {
    // Logic to send SOS signal
    alert('SOS triggered!');
}

// Location tracking
function trackLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            // Update map center
            map.setCenter(pos);
        });
    } else {
        alert('Geolocation is not supported by this browser.');
    }
}

// Finding nearby resources
function findNearbyResources() {
    // Logic to find nearby resources
    alert('Finding nearby resources...');
}

// Alert system
function showAlert(message) {
    // Display alert message
    alert(message);
}

// Modal display
function showModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'block';
}

// Example usage
// document.getElementById('sosButton').addEventListener('click', triggerSOS);
// initMap();

