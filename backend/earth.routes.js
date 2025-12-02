const router = require("express").Router();
const ctrl = require("../controllers/earth.controller");

router.post("/harmonics", ctrl.harmonic);

module.exports = router;
