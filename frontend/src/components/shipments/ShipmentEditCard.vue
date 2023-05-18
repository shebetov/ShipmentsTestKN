<template>
    <v-card>
        <v-card-title class="text-h5">
            Edit Shipment #{{ shipment.id }}
        </v-card-title>
        <v-card-text>
            <ShipmentForm :shipment="shipment"></ShipmentForm>
        </v-card-text>
    </v-card>
</template>

<script>
import ShipmentForm from "@/components/shipments/ShipmentForm.vue";

export default {
    components: {
        ShipmentForm
    },
    props: [
        'shipment'
    ]
}

</script>