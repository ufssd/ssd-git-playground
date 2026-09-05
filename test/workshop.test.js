const { getWorkshopStatus, getSetupHeading } = require("../src/workshop");

function expectEqual(actual, expected, message) {
  if (actual !== expected) {
    console.error(`FAIL: ${message}`);
    console.error(`Expected: ${expected}`);
    console.error(`Received: ${actual}`);
    process.exit(1);
  }
}

expectEqual(getWorkshopStatus(), "ready", "Workshop status should be ready");
expectEqual(getSetupHeading(), "Setup", "Setup heading should be named Setup");

console.log("All checks passed.");
