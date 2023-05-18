<template>
    <v-card height="400" color="transparent" flat>
        <v-card-title class="text-h4">
            <slot name="title">Page not found</slot>
        </v-card-title>
        <v-card-text>
            <slot name="text">
                <p>Sorry, but the page you were trying to view does not exist.</p>
            </slot>
        </v-card-text>
        <v-card-actions>
            <v-btn color="primary" :to="to">
                <slot name="btn-text">Go to home</slot>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    props: {
        to: {
            type: Object,
            required: false,
            default: () => ({name: 'shipments'})
        }
    }
}
</script>
