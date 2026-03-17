let map;
let marker;
const defaultLocation = { lat: -34.397, lng: 150.644 };

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: defaultLocation
    });

    marker = new google.maps.Marker({
        position: defaultLocation,
        map: map
    });
}

function updateMapPosition(position) {
    if (!map) {
        return;
    }

    map.setCenter(position);
    map.setZoom(15);

    if (marker) {
        marker.setPosition(position);
        return;
    }

    marker = new google.maps.Marker({
        position: position,
        map: map
    });
}

function setAlert(message, type = 'info') {
    const alertElement = document.getElementById('alert');
    if (!alertElement) {
        return;
    }

    alertElement.textContent = message;
    alertElement.classList.toggle('error', type === 'error');
    alertElement.style.display = 'block';
}

function setSosButtonLoading(isLoading) {
    const sosButton = document.getElementById('sosButton');
    if (!sosButton) {
        return;
    }

    sosButton.disabled = isLoading;
    sosButton.textContent = isLoading ? 'Sending...' : 'SOS';
}

function getCurrentPosition() {
    return new Promise((resolve, reject) => {
        if (!navigator.geolocation) {
            reject(new Error('Geolocation is not supported by this browser.'));
            return;
        }

        navigator.geolocation.getCurrentPosition(resolve, reject, {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        });
    });
}

async function sendSOS() {
    setSosButtonLoading(true);
    setAlert('Sending SOS...');

    const payload = {
        message: 'Emergency SOS triggered',
        timestamp: new Date().toISOString(),
        location: null
    };

    try {
        const position = await getCurrentPosition();
        payload.location = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        updateMapPosition(payload.location);
    } catch (error) {
        setAlert(`${error.message} Sending SOS without location...`);
    }

    try {
        const response = await fetch('api/send-alerts.php', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error('Unable to send SOS at this time.');
        }

        const data = await response.json().catch(() => ({}));
        const fallbackMessage = payload.location
            ? 'Alert sent! Help is on the way!'
            : 'Alert sent without location. Help is on the way!';
        setAlert(data.message || fallbackMessage);
    } catch (error) {
        setAlert(error.message || 'Unable to send SOS at this time.', 'error');
    } finally {
        setSosButtonLoading(false);
    }
}

const sosButton = document.getElementById('sosButton');
if (sosButton) {
    sosButton.addEventListener('click', sendSOS);
}
