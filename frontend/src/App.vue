<template>
    <v-app>
        <SideBar/>
        <v-main class="pt-8">
            <v-container>
                <div v-show="!$store.getters.isLoading">
                    <router-view/>
                </div>
                <v-skeleton-loader v-if="$store.getters.isLoading" :loading="true" type="table"></v-skeleton-loader>
            </v-container>
        </v-main>
        <v-overlay
            :model-value="displayError !== null"
            class="align-center justify-center"
            persistent
        >
            <v-card class="pa-10">
                <v-card-title class="text-h4 pb-10">Something went wrong :(</v-card-title>
                <v-card-text>
                    <v-alert type="error" dismissible>
                        {{ displayError }}
                    </v-alert>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" @click="$store.commit('setDisplayError', null)">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-overlay>
    </v-app>
</template>

<script>
import {VSkeletonLoader} from 'vuetify/labs/VSkeletonLoader'
import SideBar from "@/components/SideBar.vue";
import {mapState} from "vuex";

export default {
    name: 'App',
    components: {
        SideBar,
        VSkeletonLoader
    },
    computed: {
        ...mapState(['displayError'])
    },
    mounted() {
        this.$watch(() => this.$route.path, (to, from) => {
            this.$store.commit('setDisplayError', null);
        })

        this.$store.dispatch('loadCountries');
        this.$store.dispatch('loadCities');
        this.$store.dispatch('loadShipments');
    }
}

</script>