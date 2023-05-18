import {createStore} from 'vuex'
import api from "../api";

export default createStore({
    state: {
        loadingCounter: 0,
        shipments: [],
        countries: [],
        cities: [],
        displayError: null
    },
    getters: {
        loadingCounter: (state) => state.loadingCounter,
        isLoading: (state) => state.loadingCounter > 0,
        shipments: (state) => state.shipments,
        getShipment: (state) => (id) => {
            return state.shipments.find((p) => p.id === id);
        },
        countries: (state) => state.countries,
        cities: (state) => state.cities,
        getCountryNameById: (state) => (id) => {
            let country = state.countries.find((p) => p.id === id);
            return country ? country.name : "";
        },
        getCityNameById: (state) => (id) => {
            let city = state.cities.find((p) => p.id === id);
            return city ? city.name : "";
        },
        getCitiesByCountryId: (state) => (id) => {
            return state.cities.filter((p) => p.country === id);
        },
        displayError: (state) => state.displayError
    },
    mutations: {
        incLoadingCounter: (state) => (state.loadingCounter += 1),
        decLoadingCounter: (state) => (state.loadingCounter -= 1),

        setShipments: (state, data) => (state.shipments = data),
        createShipment: (state, data) => state.shipments.unshift(data),
        updateShipment: (state, data) => {
            let idx = state.shipments.findIndex((p) => p.id === data.id);
            state.shipments.splice(idx, 1, data);
        },
        deleteShipment(state, id) {
            let idx = state.shipments.findIndex((p) => p.id === id);
            state.shipments.splice(idx, 1);
        },

        setCountries: (state, data) => (state.countries = data),
        setCities: (state, data) => (state.cities = data),

        setDisplayError: (state, data) => (state.displayError = data)
    },
    actions: {
        loadShipments({commit}) {
            commit("incLoadingCounter");
            return api.getShipments()
                .then((response) => commit("setShipments", response.data))
                .catch((error) => commit("setDisplayError", error))
                .finally(() => commit("decLoadingCounter"));
        },
        createShipment({commit}, payload) {
            commit("incLoadingCounter");
            return api.createShipment(payload)
                .then((response) => commit("createShipment", response.data))
                .catch((error) => commit("setDisplayError", error))
                .finally(() => commit("decLoadingCounter"));
        },
        updateShipment({commit}, payload) {
            commit("incLoadingCounter");
            return api.updateShipment(payload)
                .then((response) => commit("updateShipment", response.data))
                .catch((error) => commit("setDisplayError", error))
                .finally(() => commit("decLoadingCounter"));
        },
        deleteShipment({commit}, id) {
            commit("incLoadingCounter");
            return api.deleteShipment(id)
                .then(() => commit("deleteShipment", id))
                .catch((error) => commit("setDisplayError", error))
                .finally(() => commit("decLoadingCounter"));
        },
        loadCountries({commit}) {
            commit("incLoadingCounter");
            return api.getCountries()
                .then((response) => commit("setCountries", response.data))
                .catch((error) => commit("setDisplayError", error))
                .finally(() => commit("decLoadingCounter"));
        },
        loadCities({commit}) {
            commit("incLoadingCounter");
            return api.getCities()
                .then((response) => commit("setCities", response.data))
                .catch((error) => commit("setDisplayError", error))
                .finally(() => commit("decLoadingCounter"));
        }
    },
    modules: {}
})
