

function capitalize(s) {
    return s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
}

function getShipmentStatusDisplay(status) {
    return capitalize(status).replace('_', ' ');
}


export {
    getShipmentStatusDisplay,
}
