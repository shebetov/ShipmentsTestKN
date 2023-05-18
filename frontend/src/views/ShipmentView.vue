<template>
    <div v-if="shipment">
        <BackBtn :to=" isEdit ? { name: 'shipment', params: { id: shipment.id }} : { name: 'shipments' } "/>
        <ShipmentCard v-if="!isEdit" :shipment="shipment"></ShipmentCard>
        <ShipmentEditCard v-else :shipment="shipment"></ShipmentEditCard>
    </div>
    <NotFoundCard v-else>
        <template #title>
            Shipment not found
        </template>
        <template #text>
            <p>Shipment with id {{ id }} does not exist.</p>
        </template>
        <template #btn-text>
            Back to shipments
        </template>
    </NotFoundCard>
</template>

<script>
import BackBtn from "@/components/BackBtn.vue";
import NotFoundCard from "@/components/NotFoundCard.vue";
import ShipmentCard from "@/components/shipments/ShipmentCard.vue";
import ShipmentEditCard from "@/components/shipments/ShipmentEditCard.vue";


export default {
    components: {
        ShipmentEditCard,
        ShipmentCard,
        NotFoundCard,
        BackBtn
    },
    props: {
        id: {
            type: Number,
            required: true
        },
        isEdit: {
            type: Boolean,
            required: false,
            default: false
        }
    },
    computed: {
        shipment() {
            return this.$store.getters.getShipment(this.id);
        }
    },
}

</script>
