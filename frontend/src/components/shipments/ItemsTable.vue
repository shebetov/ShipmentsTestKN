<template>
    <v-skeleton-loader :loading="items === null" type="table-thead, table-row-divider@3">
        <v-table fixed-header v-if="items !== null">
            <thead>
            <tr>
                <th class="text-left">Id</th>
                <th class="text-left">Name</th>
                <th class="text-left">Weight</th>
                <th class="text-left">Is Fragile</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in items" :key="item.id">
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.weight }}</td>
                <td>{{ item.is_fragile }}</td>
            </tr>
            </tbody>
        </v-table>
    </v-skeleton-loader>
</template>

<script>
import {VSkeletonLoader} from 'vuetify/labs/VSkeletonLoader'

export default {
    components: {
        VSkeletonLoader
    },
    props: [
        'items'
    ]
}

</script>