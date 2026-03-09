/**
 * OrchLayer Gemini - Drive Infrastructure Setup
 * Creates the standardized folder hierarchy for the project.
 */
function setupOrchLayerDrive() {
  const rootFolderName = "PROJ-ORCH-GEMINI";
  const rootFolder = DriveApp.createFolder(rootFolderName);
  const folders = [
    "00_KB-Core",
    "01_Project-State",
    "02_Session-Packets",
    "03_Handoffs",
    "04_Decision-Logs",
    "05_Domain-Overlays",
    "99_Archive"
  ];
  folders.forEach(name => rootFolder.createFolder(name));
}
