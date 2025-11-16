/**
 * ArcGIS Map Integration
 * Loads LA County Grant Funding Distribution map
 */

// ArcGIS Feature Service URL
const FEATURE_SERVICE_URL = "https://services.arcgis.com/hVnyNvwbpFFPDV5j/arcgis/rest/services/LA_County_Grant_Funding_Distribution/FeatureServer/0";

let map = null;
let view = null;
let mapInitialized = false;

/**
 * Initialize ArcGIS map using AMD require pattern
 */
function initializeMap() {
    if (mapInitialized) return;
    
    require([
        "esri/Map",
        "esri/views/MapView",
        "esri/layers/FeatureLayer"
    ], function(Map, MapView, FeatureLayer) {
        try {
            // Create map
            map = new Map({
                basemap: "streets-navigation-vector"
            });

            // Add Feature Layer
            const featureLayer = new FeatureLayer({
                url: FEATURE_SERVICE_URL,
                title: "LA County Grant Funding Distribution",
                opacity: 0.8
            });

            map.add(featureLayer);

            // Create map view
            const mapContainer = document.getElementById("map-container");
            if (!mapContainer) {
                console.error('Map container not found');
                return;
            }

            view = new MapView({
                container: "map-container",
                map: map,
                center: [-118.2437, 34.0522], // Los Angeles center
                zoom: 10
            });

            mapInitialized = true;
            window.mapInitialized = true;
            console.log('[OK] ArcGIS map initialized');

        } catch (error) {
            console.error('Error initializing map:', error);
            const mapContainer = document.getElementById("map-container");
            if (mapContainer) {
                mapContainer.innerHTML = '<p class="error">Map could not be loaded. Please check your connection.</p>';
            }
        }
    });
}

/**
 * Show user location on map (from zip code)
 */
function showUserLocation(zipCode) {
    if (!view || !mapInitialized) {
        // Wait a bit and try again
        setTimeout(() => showUserLocation(zipCode), 500);
        return;
    }

    require([
        "esri/Graphic",
        "esri/geometry/Point",
        "esri/symbols/SimpleMarkerSymbol"
    ], function(Graphic, Point, SimpleMarkerSymbol) {
        try {
            // For demo, center on LA County
            // TODO: Use geocoding service to get exact zip code location
            const userPoint = new Point({
                longitude: -118.2437,
                latitude: 34.0522
            });

            const markerSymbol = new SimpleMarkerSymbol({
                color: [226, 119, 40], // Orange
                outline: {
                    color: [255, 255, 255],
                    width: 2
                },
                size: 12
            });

            const userGraphic = new Graphic({
                geometry: userPoint,
                symbol: markerSymbol
            });

            view.graphics.removeAll();
            view.graphics.add(userGraphic);
            view.goTo({
                center: userPoint,
                zoom: 12
            });

        } catch (error) {
            console.error('Error showing user location:', error);
        }
    });
}

// Wait for ArcGIS API to load, then initialize
window.addEventListener('load', function() {
    // Wait a bit for ArcGIS API to be ready
    setTimeout(function() {
        if (typeof require !== 'undefined') {
            initializeMap();
        } else {
            console.warn('ArcGIS API not loaded yet, map will initialize when available');
        }
    }, 1000);
});

// Export for use in app.js
window.initializeMap = initializeMap;
window.showUserLocation = showUserLocation;

