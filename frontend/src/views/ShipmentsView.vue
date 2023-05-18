<template>
    <v-row justify="space-between" class="mb-5">
        <div class="text-h4">Shipments</div>
        <v-btn align-self="end" color="primary" :to="{ name: 'shipment-create' }">Create</v-btn>
    </v-row>
    <div v-if="$store.getters.shipments.length > 0">
        <v-table fixed-header>
            <thead>
            <tr>
                <th class="text-left">Id</th>
                <th class="text-left">Status</th>
                <th class="text-left">Delivery Address</th>
                <th class="text-left">Sent</th>
                <th class="text-left">Created</th>
                <th class="text-left">Update</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="shipment in $store.getters.shipments" :key="shipment.id" class="shipment-row"
                @click="$router.push({'name': 'shipment', params: { id: shipment.id }})">
                <td>{{ shipment.id }}</td>
                <td>{{ getShipmentStatusDisplay(shipment.status) }}</td>
                <td>{{ shipment.full_address }}</td>
                <td>{{ shipment.sent_at || "---" }}</td>
                <td>{{ shipment.created_at }}</td>
                <td>{{ shipment.updated_at }}</td>
            </tr>
            </tbody>
        </v-table>
    </div>
    <div v-else>
        <div class="text-h5">No shipments found, create first</div>
    </div>
</template>

<script>
import {getShipmentStatusDisplay} from "@/utils";

export default {
    methods: {
        getShipmentStatusDisplay
    }
}

</script>

<style scoped>
.shipment-row {
    cursor: pointer;
}

.shipment-row:hover {
    background-color: #f5f5f5;
}
</style>
