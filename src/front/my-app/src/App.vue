<template>
	<div id="app">
		<div class="header">

			<div class="logo">
				<img src="./assets/logo.jpg">
			</div>

			<div class="types">
				<button @click="changeItems('complex')">Жилые комплексы</button>
				<!-- <button @click="changeItems('house')">Литеры</button> -->
				<!-- <button @click="changeItems('floor')">Этажи</button> -->
				<button @click="changeItems('workTypeEmpty')">Типы работ</button>
			</div>

			<div class="selects">
				<div class="select">
					<v-select 
						@input="addFilterStatus"
						:options="statuses" 
						label="name"
						:searchable="false"
						:reduce="status => status.id" 
						placeholder="Статус"
						multiple>
							<template #option="{ id, name }">
								<span class="option-status"
									:class="id === 1 ? 'success' : id === 2 ? 'error' : 'between'">
										{{ name }}
								</span>
							</template>
					</v-select>
				</div>

				<div class="select">
					<v-select 
						@input="addFilterExecutor"
						:options="executors" 
						label="name"
						:searchable="false"
						:reduce="status => status.id" 
						placeholder="Ответственный"
						multiple>
							<template #option="{ name }">
								{{ name }}
							</template>
					</v-select>
				</div>
			</div>

			<div class="selects test">
				<div class="select">
					<v-select 
						:options="[]" 
						label="name"
						:searchable="false"
						:reduce="status => status.id" 
						placeholder="Объекты"
						multiple>
							<template #option="{ id, name }">
								<span class="option-status"
									:class="id === 1 ? 'success' : id === 2 ? 'error' : 'between'">
										{{ name }}
								</span>
							</template>
					</v-select>
				</div>

				<div class="select">
					<v-select 
						:options="[]" 
						label="name"
						:searchable="false"
						:reduce="status => status.id" 
						placeholder="Дата"
						multiple>
							<template #option="{ name }">
								{{ name }}
							</template>
					</v-select>
				</div>
			</div>
		</div>

		<hr>
		<div class="history">
			<a @click="main()">ООО ЗСК</a>

			<template v-for="(value, i) in historyData">
				<a v-bind:key="i" @click="backTo(value.key, value.item)">
					-> {{ value.item.name }}
				</a>
			</template>
		</div>

		<List
			v-if="items.length != 0"
			:items="items"
			:key="componentKey">
		</List>

		<Modal
			v-if="modalData.length != 0"
			:item="modalData">
		</Modal>
	</div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Modal from './components/Modal.vue';
import List from './components/List.vue';

import ComplexesData from './data/compelexes.json';
import LitersData from './data/liters.json';
import FloorsData from './data/floors.json';
import WorksData from './data/works.json';

export default {
	name: 'App',
	components: {
        Modal,
		List
    },
	data() {
        return {
			key: '',
			componentKey: 0,
 			items: [],
			statusArr: [],
			executorArr: [],
			historyData: [],
			isModalOpen: false,
			modalData: {},

			complexes: ComplexesData,
			liters: LitersData,
			floors: FloorsData,
			works: WorksData,

			workTypes: [
				{
					"id": 1,
					"name": "Общие",
				},
				{
					"id": 2,
					"name": "Инженерные коммуникации",
				},
				{
					"id": 3,
					"name": "Отделочные работы",
				},
			],
			statuses: [
				{
					"id": 1,
					"name": "Выполнены"
				},
				{
					"id": 2,
					"name": "Не выполнены"
				},
				{
					"id": 3,
					"name": "В процессе"
				},
			],
			executors: [
				{
					"id": "ООО Гранит",
					"name": "ООО Гранит"
				},
				{
					"id": "ООО Металл",
					"name": "ООО Металл"
				},
				{
					"id": "ООО Серебро",
					"name": "ООО Серебро"
				},
			],
		}
	},
	created() {
		this.main();
    },
	methods: {
		changeItems(key) {
			this.key = key;
			this.historyData = [];

			switch (key) {
				case 'complex':
					this.items = this.complexes;
					break;
				case 'workTypeEmpty':
					this.items = this.workTypes;
					break;
			}
		},
		addFilterStatus(statusArr) {
			this.statusArr = statusArr;
			this.componentKey++;
		},
		addFilterExecutor(executorArr) {
			this.executorArr = executorArr;
			this.componentKey++;
		},
		modalOpen(item) {
			this.modalData = item;
			this.isModalOpen = true;
		},
		markDone(id) {
			this.isModalOpen = !this.isModalOpen;
			document.querySelector('[data-id="' + id + '"]').remove();
		},
		inside(id) {
			switch (this.key) {
				case 'complex':
					this.items = this.liters.filter(element => element['complex_id'] == id);
					this.history(this.key, this.complexes.find(element => element['id'] == id));
					this.key = 'liter';
					break;
				case 'liter':
					this.items = this.floors.filter(element => element['liter_id'] == id);
					this.history(this.key, this.liters.find(element => element['id'] == id));
					this.key = 'floor';
					break;
				case 'floor':
					this.items = this.workTypes;
					this.floorId = id;
					this.history(this.key, this.floors.find(element => element['id'] == id));
					this.key = 'workType';
					break;
			}
		},
		getWorks(id) {
			switch (this.key) {
				case 'complex':
					return this.works.filter(function( element ) {

						if (this.statusArr.length > 0 && this.executorArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 &&
								element['complex_id'] == id;
						}

						if (this.statusArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								element['complex_id'] == id;
						}

						if (this.executorArr.length > 0) {
							return this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 && 
								element['complex_id'] == id;
						}

						return element['complex_id'] == id;
					}, this);
				case 'liter':
					return this.works.filter(function( element ) {

						if (this.statusArr.length > 0 && this.executorArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 &&
								element['liter_id'] == id;
						}

						if (this.statusArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								element['liter_id'] == id;
						}

						if (this.executorArr.length > 0) {
							return this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 && 
								element['liter_id'] == id;
						}

						return element['liter_id'] == id;
					}, this);
				case 'floor':
					return this.works.filter(function( element ) {

						if (this.statusArr.length > 0 && this.executorArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 &&
								element['floor_id'] == id;
						}

						if (this.statusArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								element['floor_id'] == id;
						}

						if (this.executorArr.length > 0) {
							return this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 && 
								element['floor_id'] == id;
						}

						return element['floor_id'] == id;
					}, this);
				case 'workType':
					return this.works.filter(function( element ) {

						if (this.statusArr.length > 0 && this.executorArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 &&
								element['work_type_id'] == id && element['floor_id'] == this.floorId;
						}

						if (this.statusArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								element['work_type_id'] == id && element['floor_id'] == this.floorId;
						}

						if (this.executorArr.length > 0) {
							return this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 && 
								element['work_type_id'] == id && element['floor_id'] == this.floorId;
						}

						return element['work_type_id'] == id && element['floor_id'] == this.floorId;
					}, this);
				case 'workTypeEmpty':
					return this.works.filter(function( element ) {

						if (this.statusArr.length > 0 && this.executorArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 &&
								element['work_type_id'] == id;
						}

						if (this.statusArr.length > 0) {
							return this.statusArr.indexOf(this.works.find(el => el.id == element.id)['status']) >= 0 && 
								element['work_type_id'] == id;
						}

						if (this.executorArr.length > 0) {
							return this.executorArr.indexOf(this.works.find(el => el.id == element.id)['executor']) >= 0 && 
								element['work_type_id'] == id;
						}

						return element['work_type_id'] == id;
					}, this);
			}
		},
		history(key, item) {
			this.historyData.push({
				"key": key,
				"item": item
			});
		},
		backTo(key, item) {
			var historyData = JSON.parse(JSON.stringify(this.historyData))

			var newHistoryData = [];

			for (var i = 0; i < historyData.length; i++) {

				if (historyData[i]['item']['name'] == item.name) {
					break;
				} else {
					newHistoryData.push(historyData[i]);
				}
			}

			this.historyData.splice(0, historyData.length);
			this.historyData = newHistoryData;

			this.key = key;
			this.inside(item.id);
		},
		main() {
			this.key = 'complex';
			this.items = this.complexes;
			this.historyData = [];
		}
	},
}
</script>

<style>
  @import './assets/styles/global.css';
</style>