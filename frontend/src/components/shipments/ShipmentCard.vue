<template>
    <v-card>
        <v-card-title class="text-h5">
            Shipment #{{ shipment.id }}
        </v-card-title>
        <v-card-text>
            <v-list lines="one">
                <v-list-item title="Status" :subtitle="getShipmentStatusDisplay(shipment.status)"></v-list-item>
                <v-list-item title="Created At" :subtitle="shipment.created_at"></v-list-item>
                <v-list-item title="Sent At" :subtitle="shipment.sent_at || '-'"></v-list-item>
                <v-list-item title="Comment" :subtitle="shipment.comment || '-'"></v-list-item>
                <v-list-item title="Country" :subtitle="$store.getters.getCountryNameById(shipment.country)"></v-list-item>
                <v-list-item title="City" :subtitle="$store.getters.getCityNameById(shipment.city)"></v-list-item>
                <v-list-item title="Address" :subtitle="shipment.address"></v-list-item>
                <v-list-item title="Items">
                    <ItemsTable :items="items"></ItemsTable>
                </v-list-item>
            </v-list>
        </v-card-text>
        <v-card-actions>
            <v-btn variant="text" color="teal-accent-4" :to="{ name: 'shipment-edit', params: { id: shipment.id } }">
                Edit
            </v-btn>
            <v-btn variant="text" color="red" @click="deleteShipment">Delete</v-btn>
        </v-card-actions>
    </v-card>
</template>


<script>
import {getShipmentStatusDisplay} from "@/utils";
import ItemsTable from "@/components/shipments/ItemsTable.vue";
import api from "@/api";

export default {
    components: {
        ItemsTable
    },
    props: [
        'shipment'
    ],
    data() {
        return {
            items: null
        }
    },
    methods: {
        getShipmentStatusDisplay,
        deleteShipment() {
            this.$store.dispatch('deleteShipment', this.shipment.id).then(
                () => this.$router.push({name: 'shipments'})
            );
        }
    },
    mounted() {
        api.getShipmentItems(this.shipment.id)
            .then(response => this.items = response.data)
            .catch(error => this.$store.commit('setDisplayError', error));
    }
}

</script>
