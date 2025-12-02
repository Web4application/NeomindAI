function EarthMap({ seasonality, trend }) {
  return (
    <div className="earth-map">
      <h2>Neomind Earth Module</h2>

      <div className="map-row">
        <img src={seasonality} alt="Seasonality Map" />
        <img src={trend} alt="Trend Map" />
      </div>
    </div>
  );
}
