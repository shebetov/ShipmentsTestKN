<template>
    <v-form id="shipment-form" v-model="valid" lazy-validation @submit.prevent="submit">
        <v-select
            v-model="fields.status"
            label="Status"
            item-title="title"
            item-value="value"
            :items="statusSelectItems"
            :rules="[ rules.required ]"
        ></v-select>
        <v-select
            v-model="fields.country"
            label="Country"
            item-title="name"
            item-value="id"
            :items="$store.getters.countries"
            :rules="[ rules.required ]"
            @update:modelValue="onCountryChange"
        ></v-select>
        <v-select
            v-model="fields.city"
            label="City"
            item-title="name"
            item-value="id"
            :items="citySelectItems"
            :disabled="citySelectItems.length === 0"
            :rules="[ rules.required ]"
        ></v-select>
        <v-text-field v-model="fields.address" label="Address" :rules="[ rules.required ]"></v-text-field>

        <v-btn color="primary" type="submit" form="shipment-form">Save</v-btn>
    </v-form>
</template>

<script>
import {SHIPMENT_STATUSES} from "@/constants";
import {getShipmentStatusDisplay} from "@/utils";

export default {
    props: [
        'shipment'
    ],
    data() {
        return {
            valid: false,
            fields: {
                status: SHIPMENT_STATUSES[0],
                country: null,
                city: null,
                address: null,
            },
            rules: {
                required: value => !!value || 'This field is required',
            }
        }
    },
    computed: {
        citySelectItems() {
            return this.fields.country ? this.$store.getters.getCitiesByCountryId(this.fields.country) : []
        }
    },
    created() {
        this.statusSelectItems = Object.values(SHIPMENT_STATUSES).map(key => ({
            title: getShipmentStatusDisplay(key),
            value: key
        }))
    },
    mounted() {
        if (this.shipment) {
            this.fields.status = this.shipment.status
            this.fields.country = this.shipment.country
            this.fields.city = this.shipment.city
            this.fields.address = this.shipment.address
        }
    },
    methods: {
        onCountryChange() {
            this.fields.city = null
        },
        submit() {
            if (this.valid) {
                let payload = {
                    status: this.fields.status,
                    city: this.fields.city,
                    address: this.fields.address,
                }
                if (this.shipment) {
                    payload.id = this.shipment.id
                    this.$store.dispatch('updateShipment', payload)
                        .then(() => this.$router.push({name: 'shipment', params: {id: this.shipment.id}}));
                } else {
                    this.$store.dispatch('createShipment', payload)
                        .then(() => this.$router.push({name: 'shipments'}));
                }
            }
        }
    }
}

</script>
