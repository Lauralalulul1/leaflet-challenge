//Import & Visualize the Data
// Create map use Leaflet plots all the earthquakes from your data set based on their long and lat.


// Your data markers show magnitude of the earthquake by size & depth of earthquake by color. 
// Earthquakes with higher magnitudes larger and earthquakes with greater depth darker in color.


// HINT depth of earth can be found as the third coordinate for each earthquake.


// Include popups provide info about earthquake when marker is clicked.


// Create legend will provide context for your map data.


// Your visualization should look something like the map above.


//Create map object slack
var mapProperties = L.map("map", {
    center: [37.7749, -122.4194],
    zoom: 8
  }
var myMap = L.map("map", mapProperties)
  
  // Add tile layer slack
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>", 
    maxZoom: 18,
    id: "mapbox/streets-v11",
    accessToken: "API_KEY",
  }).addTo(myMap);

  // Use link to get geojson data. slack
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson";

//D3 grabs data. slack
d3.json(link, function(data) {

// Creating a GeoJSON layer with the retrieved data
L.geoJson(data).addTo(myMap);
});

//d3.json(api, function(data) {
    // data.forEach(d => {
    //     var latLong = d.location.coordinates
    //     L.marker(latLong.reverse()).addTo(myMap);
    // })
    //var heatPoints = data.map(function(d) {
        //return d.location.coordinates.reverse()
    //})
    //var heat = L.heatLayer(heatPoints, { radius: 50, blur: 50 }).addTo(myMap);
    
//});

// Createa new marker
//var marker = L.marker([])
//a loop

function styleInfo(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: getColor(feature.properties.mag),
      color: "#000000",
      radius: getRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5
    };
  }
  // Function determines color of marker based on magnitude of earthquake.
    function getColor(magnitude) {
    switch (true) {
    case magnitude > 5:
      return "#ea2c2c";
    case magnitude > 4:
      return "#ea822c";
    case magnitude > 3:
      return "#ee9c00";
    case magnitude > 2:
      return "#eecc00";
    case magnitude > 1:
      return "#d4ee00";
    default:
      return "#98ee00";
    }
  }
  // set radius from magnitude
    function getRadius(magnitude) {
    if (magnitude === 0) {
      return 1;
    }

    return magnitude * 4;
  }
    // Creating GeoJSON layer with retrieved data
    L.geoJson(data, {
      // circle
      pointToLayer: function(feature, latlng) {
        return L.circleMarker(latlng);
      },
      // style
      style: styleInfo,
      // binding a popup for each marker
      onEachFeature: function(feature, layer) {
        layer.bindPopup("Magnitude: " + feature.properties.mag + "<br>Location: " + feature.properties.place);
      }
    }).addTo(myMap);
  
    // an object legend
    var legend = L.control({
      position: "bottomright"
    });
  
    // details for the legend
    legend.onAdd = function() {
      var div = L.DomUtil.create("div", "info legend");
  
      var grades = [0, 1, 2, 3, 4, 5];
      var colors = [
        "#98ee00",
        "#d4ee00",
        "#eecc00",
        "#ee9c00",
        "#ea822c",
        "#ea2c2c"
      ];
  
      // Looping through the grades
      for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
          "<i style='background: " + colors[i] + "'></i> " +
          grades[i] + (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+");
      }
      return div;
    };
  
    // Finally, we our legend to the map.
    legend.addTo(myMap);
  });

//future notes: L. because for "leaflet"