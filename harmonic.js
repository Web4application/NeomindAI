// harmonic.js
const runHarmonicAnalysis = (params) => {
  var region = ee.Geometry.Polygon(params.region);
  var startYear = params.startYear || 2000;
  var endYear = params.endYear || 2024;

  var c = ee.ImageCollection('MODIS/006/MOD13A1')
      .select('EVI')
      .filterDate(startYear + '-01-01', endYear + '-12-31')
      .filterBounds(region);

  function addIndependentVariables(image) {
    var date = ee.Date(image.get('system:time_start'));
    var phase = date.getFraction('year').multiply(2 * Math.PI);
    var sin = phase.sin();
    var cos = phase.cos();
    var time = date.difference(ee.Date('2000-01-01'), 'year');
    var independent = ee.Image([sin, cos, time, 1]).double();
    return independent.addBands(image);
  }

  var regression = c.map(addIndependentVariables)
    .reduce(ee.Reducer.linearRegression(4))
    .select('coefficients')
    .arrayProject([0])
    .arrayFlatten([['sin', 'cos', 'slope', 'offset']])
    .divide(10000);

  var seasonality = ee.Image.cat(
    regression.select('sin').atan2(regression.select('cos')).unitScale(-Math.PI, Math.PI),
    regression.select('cos').hypot(regression.select('sin')).multiply(2.5),
    regression.select('offset').multiply(1.5)
  ).hsvToRgb();

  var trendVis = {
    bands: ['slope', 'offset', 'slope'],
    min: 0,
    max: [-0.005, 1, 0.005]
  };

  var trend = regression.visualize(trendVis);

  return {
    seasonality: seasonality,
    trend: trend
  };
};

exports.runHarmonicAnalysis = runHarmonicAnalysis;
