function EarthPanel() {
  const [region, setRegion] = useState(null);

  const runAnalysis = async () => {
    const res = await fetch("/api/earth/harmonics", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        region,
        startYear: 2000,
        endYear: 2024,
      }),
    });

    const data = await res.json();
    setSeasonality(data.seasonalityUrl);
    setTrend(data.trendUrl);
  };

  return (
    <div className="earth-panel">
      <h3>Earth Intelligence</h3>
      <button onClick={runAnalysis}>Run Harmonic Analysis</button>
    </div>
  );
}
