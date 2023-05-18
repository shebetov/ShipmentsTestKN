<template>
    <BackBtn :to="{ name: 'shipments'}"/>
    <v-card>
        <v-card-title class="text-h5">
            Create Shipment
        </v-card-title>
        <v-card-text>
            <ShipmentForm></ShipmentForm>
        </v-card-text>
    </v-card>
</template>

<script>
import BackBtn from "@/components/BackBtn.vue";
import ShipmentForm from "@/components/shipments/ShipmentForm.vue";

export default {
    components: {
        ShipmentForm,
        BackBtn
    },
}
</script>
