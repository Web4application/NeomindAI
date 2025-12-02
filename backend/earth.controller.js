// earth.controller.js
const earthService = require("../services/earth.service");

exports.harmonic = async (req, res) => {
  try {
    const result = await earthService.harmonic(req.body);
    return res.json({
      status: "ok",
      ...result
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
