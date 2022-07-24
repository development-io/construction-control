<template>
    <div class="modal" v-if="$parent.isModalOpen">
        <div class="info" :class="item['status'] === 1 ? 'success' : item['status'] === 2 ? 'error' : 'between'">
            <a class="close-button" @click="$parent.isModalOpen = !$parent.isModalOpen">
                x
            </a>
            <div class="item">
                <div class="name">{{ item.name }}</div>
                <div>Исполнитель: {{ item.executor }}</div>

                <template v-if="item.status != 1">
                    <button @click="$parent.markDone(item.id)">Выполнено</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
export default ({
    props: {
        item: Object
    },
    methods: {
		hide() {
			this.$parent.isModalOpen = false;
		},
    }
})
</script>