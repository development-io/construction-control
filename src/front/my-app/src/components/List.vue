<template>
    <div>
        <div class="items"
            v-for="item in items"
            v-bind:key="item.id">
                <div class="item" @click="$parent.inside(item.id)">
                    <div class="text">
                        {{ item.name }}
                    </div>
                </div>


                <div class="works">
                    <div class="works-item" :data-id="value.id"
                        v-for="value in $parent.getWorks(item.id)"
                        v-bind:key="value.id"
                        :class="value['status'] === 1 ? 'success' : value['status'] === 2 ? 'error' : 'between'">
                            <button 
                                :class="value['status'] === 1 ? 'success' : value['status'] === 2 ? 'error' : 'between'"
                                @click="$parent.modalOpen(value)">
                                    <span class="title">{{ value.name }}</span>
                                    <span class="date">{{ value.date }}</span>
                                    <span class="executor">Исп: {{ value.executor }}</span>
                                    <template v-if="value.important == true">
                                        <span class="important">!</span>
                                    </template>
                            </button>
                    </div>
                </div>
        </div>
    </div>
</template>

<script>
export default ({
    props: {
        items: Array
    },
    methods: {
		hide() {
			this.$parent.isModalOpen = false;
		},
    }
})
</script>