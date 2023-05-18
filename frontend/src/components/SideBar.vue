<template>
    <v-navigation-drawer expand-on-hover permanent v-model:rail="isFolded">
        <v-list>
            <v-list-item
                title="Shipments App"
                subtitle="Test Project For Interview"
            ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
            <v-list-item prepend-icon="mdi-package-variant-closed" title="Shipments" value="shipments"
                         to="/"></v-list-item>
            <v-list-item prepend-icon="mdi-information-outline" title="About" value="about" to="/about"></v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>

export default {
    data() {
        return {
            isFolded: true,
        }
    },
}

</script>