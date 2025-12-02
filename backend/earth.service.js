// earth.service.js
const earthService = {};

earthService.harmonic = async ({ region, startYear, endYear }) => {
  const result = runHarmonicAnalysis({ region, startYear, endYear });

  const seasonalityUrl = await result.seasonality.getDownloadURL({
    scale: 10000,
    region: region,
    crs: "EPSG:3857"
  });

  const trendUrl = await result.trend.getDownloadURL({
    scale: 10000,
    region: region,
    crs: "EPSG:3857"
  });

  return { seasonalityUrl, trendUrl };
};

module.exports = earthService;
