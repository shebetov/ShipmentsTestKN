import axios from "axios";

axios.defaults.baseURL = process.env.VUE_APP_API_URL;

const api = {
    getShipments() {
        return axios.get(`/shipments/shipments/`);
    },
    getShipmentItems(id) {
        return axios.get(`/shipments/shipments/${id}/items`);
    },
    createShipment(payload) {
        return axios.post(`/shipments/shipments/`, payload);
    },
    updateShipment(payload) {
        return axios.put(`/shipments/shipments/${payload.id}/`, payload);
    },
    deleteShipment(id) {
        return axios.delete(`/shipments/shipments/${id}/`);
    },
    getCountries() {
        return axios.get(`/shipments/countries/`);
    },
    getCities() {
        return axios.get(`/shipments/cities/`);
    }
};

export default api;
