/**
 * ArcGIS Map Integration - EMERGENCY FIX
 * Shows LA County grants and highlights matching grants
 */

// ArcGIS Feature Service URL
const FEATURE_SERVICE_URL = "https://services.arcgis.com/hVnyNvwbpFFPDV5j/arcgis/rest/services/LA_County_Grant_Funding_Distribution/FeatureServer/0";

let map = null;
let view = null;
let mapInitialized = false;
let featureLayer = null;
let matchingGrantIds = [];

/**
 * Initialize ArcGIS map
 */
function initializeMap() {
    if (mapInitialized) return;
    
    require([
        "esri/Map",
        "esri/views/MapView",
        "esri/layers/FeatureLayer",
        "esri/widgets/Popup"
    ], function(Map, MapView, FeatureLayer, Popup) {
        try {
            // Create map with gray-vector basemap
            map = new Map({
                basemap: "gray-vector"
            });

            // Add Feature Layer with popup
            featureLayer = new FeatureLayer({
                url: FEATURE_SERVICE_URL,
                title: "LA County Grant Funding Distribution",
                opacity: 0.9,
                popupTemplate: {
                    title: "{Title}",
                    content: [{
                        type: "fields",
                        fieldInfos: [{
                            fieldName: "Funder",
                            label: "Funder"
                        }, {
                            fieldName: "Amount",
                            label: "Amount"
                        }, {
                            fieldName: "Deadline",
                            label: "Deadline"
                        }, {
                            fieldName: "Focus_Area",
                            label: "Focus Area"
                        }]
                    }]
                },
                renderer: {
                    type: "simple",
                    symbol: {
                        type: "simple-marker",
                        color: [0, 102, 204], // Blue for all grants
                        size: 8,
                        outline: {
                            color: [255, 255, 255],
                            width: 1
                        }
                    }
                }
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
                center: [-118.2437, 34.0522], // LA County center
                zoom: 9
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
 * Highlight matching grants on the map
 */
function highlightMatchingGrants(grants) {
    if (!view || !featureLayer || !mapInitialized) {
        // Wait and try again
        setTimeout(() => highlightMatchingGrants(grants), 500);
        return;
    }

    require([
        "esri/layers/FeatureLayer"
    ], function(FeatureLayer) {
        try {
            // Extract grant IDs from results (assuming grant_id or title matching)
            matchingGrantIds = grants.map(g => g.grant_id || g.title);
            
            // Update renderer to highlight matching grants
            featureLayer.renderer = {
                type: "unique-value",
                field: "Title",
                uniqueValueInfos: matchingGrantIds.map((id, index) => ({
                    value: id,
                    symbol: {
                        type: "simple-marker",
                        color: [46, 125, 50], // Green for matching grants
                        size: 12,
                        outline: {
                            color: [255, 255, 255],
                            width: 2
                        }
                    }
                })),
                defaultSymbol: {
                    type: "simple-marker",
                    color: [0, 102, 204], // Blue for non-matching
                    size: 8,
                    outline: {
                        color: [255, 255, 255],
                        width: 1
                    }
                }
            };
            
            // Refresh the layer
            featureLayer.refresh();
            
            console.log('[OK] Highlighted', matchingGrantIds.length, 'matching grants');
            
        } catch (error) {
            console.error('Error highlighting grants:', error);
            // Fallback: just refresh the layer
            if (featureLayer) {
                featureLayer.refresh();
            }
        }
    });
}

/**
 * Show user location on map (from zip code)
 */
function showUserLocation(zipCode) {
    if (!view || !mapInitialized) {
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

            // Add user location (don't remove all graphics, keep grants)
            view.graphics.removeAll();
            view.graphics.add(userGraphic);
            
            // Keep zoom at 9 to show LA County
            view.goTo({
                center: userPoint,
                zoom: 9
            });

        } catch (error) {
            console.error('Error showing user location:', error);
        }
    });
}

// Initialize map when page loads
window.addEventListener('load', function() {
    setTimeout(function() {
        if (typeof require !== 'undefined') {
            initializeMap();
        } else {
            console.warn('ArcGIS API not loaded yet, map will initialize when available');
        }
    }, 1000);
});

// Export functions
window.initializeMap = initializeMap;
window.showUserLocation = showUserLocation;
window.highlightMatchingGrants = highlightMatchingGrants;
