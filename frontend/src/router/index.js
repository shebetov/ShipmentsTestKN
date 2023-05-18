import {createRouter, createWebHistory} from 'vue-router'
import ShipmentsView from '@/views/ShipmentsView.vue'
import ShipmentView from "@/views/ShipmentView.vue";
import AboutView from "@/views/AboutView.vue";
import ShipmentCreateView from "@/views/ShipmentCreateView.vue";
import NotFoundView from "@/views/NotFoundView.vue";

const routes = [
    {
        path: '/',
        name: 'shipments',
        component: ShipmentsView
    },
    {
        path: '/shipments/create',
        name: 'shipment-create',
        component: ShipmentCreateView
    },
    {
        path: '/shipments/:id',
        name: 'shipment',
        component: ShipmentView,
        props: route => ({
            id: Number.parseInt(route.params.id) || undefined,
        })
    },
    {
        path: '/shipments/:id/edit',
        name: 'shipment-edit',
        component: ShipmentView,
        props: route => ({
            id: Number.parseInt(route.params.id) || undefined,
            isEdit: true,
        })
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
    {
        path: "/:catchAll(.*)",
        name: 'not-found',
        component: NotFoundView
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
