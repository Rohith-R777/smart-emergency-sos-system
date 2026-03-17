(() => {
    const state = {
        map: null,
        marker: null
    };
    const fallbackLocation = { lat: 0, lng: 0 };
    const GEOLOCATION_TIMEOUT_MS = 10000;
    const FALLBACK_ZOOM = 2;
    const ACTIVE_ZOOM = 15;
    const ALERT_ENDPOINT = '/api/send-alerts.php';

    function initMap() {
        state.map = new google.maps.Map(document.getElementById('map'), {
            zoom: FALLBACK_ZOOM,
            center: fallbackLocation
        });
    }

    function updateMapPosition(position) {
        if (!state.map) {
            return;
        }

        state.map.setCenter(position);
        state.map.setZoom(ACTIVE_ZOOM);

        if (state.marker) {
            state.marker.setPosition(position);
            return;
        }

        state.marker = new google.maps.Marker({
            position: position,
            map: state.map
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

    function getLocationErrorMessage(error) {
        if (!error || typeof error.code !== 'number') {
            return 'Unable to determine your location.';
        }

        switch (error.code) {
            case 1:
                return 'Location access was denied.';
            case 2:
                return 'Unable to determine your location.';
            case 3:
                return 'Location request timed out.';
            default:
                return 'Unable to determine your location.';
        }
    }

    function getCurrentPosition() {
        return new Promise((resolve, reject) => {
            if (!navigator.geolocation) {
                reject(new Error('Geolocation is not supported by this browser.'));
                return;
            }

            navigator.geolocation.getCurrentPosition(resolve, (error) => {
                reject(new Error(getLocationErrorMessage(error)));
            }, {
                enableHighAccuracy: true,
                timeout: GEOLOCATION_TIMEOUT_MS,
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
            const errorMessage = error instanceof Error && error.message
                ? error.message.trim()
                : 'Location unavailable';
            setAlert(`${errorMessage} Sending SOS without location...`);
        }

        try {
            const response = await fetch(ALERT_ENDPOINT, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error('Unable to send SOS at this time.');
            }

            const responseText = await response.text();
            let data = {};
            if (responseText) {
                try {
                    data = JSON.parse(responseText);
                } catch (parseError) {
                    throw new Error('Received an invalid response from the server.');
                }
            }

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

    window.initMap = initMap;
})();
