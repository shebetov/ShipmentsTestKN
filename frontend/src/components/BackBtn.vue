<template>
    <v-btn variant="text" @click="onClick">&lt; back</v-btn>
</template>

<script>

export default {
    props: {
        to: {default: null},
    },
    name: 'BackBtn',
    methods: {
        onClick() {
            if (this.to) {
                this.$router.push(this.to);
            } else {
                this.$router.go(-1);
            }
        }
    }
}
</script>
