import React, { Component } from "react";
import ee from "@google/earthengine";

class Map extends Component {
    constructor(props) {
        super(props);
        this.state = {
          selectedCountry: null,
        };
        this.clearDrawing = this.clearDrawing.bind(this);
      }

  componentDidMount() {
    // Load the Google Maps API
    const script = document.createElement("script");
    script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCwz8tYryeQJeA_CI2nOvxzAwpQd1c80Pc&libraries=drawing&v=3.52?client=570329943228-gr2gm28ha8kkd3ueum00mijoaiihbjmt.apps.googleusercontent.com`;
    script.async = true;
    document.body.appendChild(script);
    script.onload = () => {
      // Initialize the map and drawing manager
      this.initMap();
    };
  }

  initMap() {
    // Initialize the Google Map
    const map = new window.google.maps.Map(document.getElementById("map"), {
      center: { lat: 37.76, lng: -122.45 },
      zoom: 3,
    });
  
    // Initialize the drawing manager
    this.drawingManager = new window.google.maps.drawing.DrawingManager({
      drawingMode: window.google.maps.drawing.OverlayType.RECTANGLE,
      drawingControl: true,
      drawingControlOptions: {
        position: window.google.maps.ControlPosition.TOP_CENTER,
        drawingModes: [window.google.maps.drawing.OverlayType.RECTANGLE],
      },
      rectangleOptions: {
        fillColor: "#00FF00",
        fillOpacity: 0.2,
        strokeWeight: 2,
        strokeColor: "#00FF00",
        clickable: true,
        editable: true,
        draggable: true,
      },
    });
  
    // Add the drawing manager to the map
    this.drawingManager.setMap(map);
  
    // Listen for rectangle complete event
    window.google.maps.event.addListener(this.drawingManager, "rectanglecomplete", (rectangle) => {
      // Get the rectangle's bounds and convert to Earth Engine geometry
      const bounds = rectangle.getBounds();
      const ne = bounds.getNorthEast();
      const sw = bounds.getSouthWest();
      const geometry = ee.Geometry.Rectangle([sw.lng(), sw.lat(), ne.lng(), ne.lat()]);
  
      // Load a Sentinel-2 image collection and add it to the map
      const collection = ee.ImageCollection("COPERNICUS/S2_SR")
        .filterBounds(geometry)
        .filterDate("2022-01-01", "2022-03-01")
        .median()
        .clip(geometry);
  
      const visParams = { bands: ["B4", "B3", "B2"], min: 0, max: 3000 };
  
      map.overlayMapTypes.insertAt(
        0,
        new ee.MapTypeOverlay({ name: "Sentinel-2 SR", imageCollection: collection, visParams: visParams })
      );
      this.setState({ selectedCountry: null });
    });
  }

  clearDrawing() {
    // Remove all shapes from the map
    this.drawingManager.setMap(null);
  
    // Reset the drawing mode to rectangle
    this.drawingManager.setDrawingMode(window.google.maps.drawing.OverlayType.RECTANGLE);
  
    // Set the map for the drawing manager
    this.drawingManager.setMap(this.map);
  
    // Reset the state
    this.setState({ selectedCountry: null });
  }

  render() {
    return (
      <div>
        <div id="map" style={{ width: "100%", height: "800px" }}></div>
        <button onClick={this.clearDrawing} style={{ backgroundColor: 'transparent', border: 'none', fontSize: '16px', fontWeight: '500', marginLeft: '20px', color: '#6b6b6b' }}>
Clear Selections
</button>
      </div>
    );
  }  
}

export default Map;
