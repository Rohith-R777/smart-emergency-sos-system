// script.js

var map;
var userMarker;
var nearbyMarkers = [];
var infoWindow;

// Google Maps integration
function initMap() {
    const options = {
        zoom: 15,
        center: { lat: -34.397, lng: 150.644 }  // Default location
    };
    map = new google.maps.Map(document.getElementById('map'), options);
    infoWindow = new google.maps.InfoWindow();
}

// SOS button trigger
function triggerSOS() {
    // Logic to send SOS signal
    alert('SOS triggered!');
}

// Location tracking using the Browser Geolocation API
function trackLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            // Update map center
            map.setCenter(pos);

            // Add or update user marker
            createOrUpdateUserMarker(pos);
        }, function() {
            alert('Error: Unable to retrieve your location.');
        });
    } else {
        alert('Geolocation is not supported by this browser.');
    }
}

// Create or update the user location marker on the map
function createOrUpdateUserMarker(pos) {
    if (userMarker) {
        userMarker.setPosition(pos);
    } else {
        userMarker = new google.maps.Marker({
            position: pos,
            map: map,
            title: 'Your Location',
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 10,
                fillColor: '#4285F4',
                fillOpacity: 1,
                strokeColor: '#ffffff',
                strokeWeight: 2
            }
        });
    }
}

// Clear existing nearby markers from the map
function clearNearbyMarkers() {
    for (var i = 0; i < nearbyMarkers.length; i++) {
        nearbyMarkers[i].setMap(null);
    }
    nearbyMarkers = [];
}

// Display nearby places results in the results container
function displayNearbyResults(places, type) {
    var resultsContainer = document.getElementById('nearby-results');
    if (!resultsContainer) return;

    var section = document.createElement('div');
    section.className = 'nearby-section';

    var title = document.createElement('h3');
    title.className = 'nearby-section-title';
    title.textContent = type.charAt(0).toUpperCase() + type.slice(1).replace('_', ' ') + 's';
    section.appendChild(title);

    if (places.length === 0) {
        var noResults = document.createElement('p');
        noResults.className = 'nearby-no-results';
        noResults.textContent = 'No ' + type.replace('_', ' ') + 's found nearby.';
        section.appendChild(noResults);
    } else {
        var list = document.createElement('ul');
        list.className = 'nearby-list';

        for (var i = 0; i < places.length; i++) {
            var place = places[i];
            var item = document.createElement('li');
            item.className = 'nearby-item';

            var name = document.createElement('span');
            name.className = 'nearby-name';
            name.textContent = place.name;
            item.appendChild(name);

            if (place.vicinity) {
                var address = document.createElement('span');
                address.className = 'nearby-address';
                address.textContent = place.vicinity;
                item.appendChild(address);
            }

            if (place.rating) {
                var rating = document.createElement('span');
                rating.className = 'nearby-rating';
                rating.textContent = 'Rating: ' + place.rating + '/5';
                item.appendChild(rating);
            }

            if (place.opening_hours) {
                var status = document.createElement('span');
                status.className = place.opening_hours.open_now ? 'nearby-open' : 'nearby-closed';
                status.textContent = place.opening_hours.open_now ? 'Open Now' : 'Closed';
                item.appendChild(status);
            }

            list.appendChild(item);
        }

        section.appendChild(list);
    }

    resultsContainer.appendChild(section);
}

// Add markers to the map for found places
function addPlaceMarkers(places, icon) {
    for (var i = 0; i < places.length; i++) {
        var place = places[i];
        var marker = new google.maps.Marker({
            position: place.geometry.location,
            map: map,
            title: place.name,
            icon: icon
        });

        // Attach info window on marker click using Google Maps Event Listener
        (function(marker, place) {
            google.maps.event.addListener(marker, 'click', function() {
                var content = '<div class="info-window">' +
                    '<strong>' + place.name + '</strong><br>' +
                    (place.vicinity ? place.vicinity + '<br>' : '') +
                    (place.rating ? 'Rating: ' + place.rating + '/5' : '') +
                    '</div>';
                infoWindow.setContent(content);
                infoWindow.open(map, marker);
            });
        })(marker, place);

        nearbyMarkers.push(marker);
    }
}

// Search for a specific type of place using Google Maps Places API (Nearby Search)
function searchNearbyPlaces(location, type, icon) {
    var service = new google.maps.places.PlacesService(map);
    var request = {
        location: location,
        radius: 5000,
        type: [type]
    };

    service.nearbySearch(request, function(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            addPlaceMarkers(results, icon);
            displayNearbyResults(results, type);
        } else {
            displayNearbyResults([], type);
        }
    });
}

// Finding nearby emergency resources using Google Maps Places API
// Technologies: Browser Geolocation API, Google Maps JavaScript API, Google Maps Places API (Nearby Search)
function findNearbyResources() {
    if (!navigator.geolocation) {
        alert('Geolocation is not supported by this browser.');
        return;
    }

    navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        // Center map on user location
        map.setCenter(pos);
        map.setZoom(14);

        // Add or update user marker
        createOrUpdateUserMarker(pos);

        // Clear previous results
        clearNearbyMarkers();
        var resultsContainer = document.getElementById('nearby-results');
        if (resultsContainer) {
            resultsContainer.innerHTML = '';
        }

        // Search for emergency-related places within a 5 km radius
        var placeTypes = [
            { type: 'hospital', icon: 'https://maps.google.com/mapfiles/ms/icons/red-dot.png' },
            { type: 'police', icon: 'https://maps.google.com/mapfiles/ms/icons/blue-dot.png' },
            { type: 'fire_station', icon: 'https://maps.google.com/mapfiles/ms/icons/orange-dot.png' }
        ];

        for (var i = 0; i < placeTypes.length; i++) {
            searchNearbyPlaces(pos, placeTypes[i].type, placeTypes[i].icon);
        }
    }, function() {
        alert('Error: Unable to retrieve your location.');
    });
}

// Alert system
function showAlert(message) {
    // Display alert message
    alert(message);
}

// Modal display
function showModal() {
    var modal = document.getElementById('modal');
    modal.style.display = 'block';
}

// Example usage
// document.getElementById('sosButton').addEventListener('click', triggerSOS);
// initMap();

