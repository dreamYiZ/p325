<template>
	<view class="index page home" v-if="kinds && goods && kinds.length">
		<view class="menu">
			<scroll-view :scroll-y="true" style="height: 100%" @scroll="scrollMenu">
				<view
					class="menu-item"
					:class="{ 'active-menu-item': activeKind === item }"
					v-for="(item, index) in kinds"
					:key="index"
					:onTap="() => onClickMenu(item)"
				>
					{{ item }}
				</view>
			</scroll-view>
		</view>
		<view class="goods">
			<scroll-view
				:scroll-y="true"
				style="height: 100%"
				@scroll="scrollGoods"
				:scrollIntoView="toScrollViewId"
				:scrollWithAnimation="true"
				:enhanced="true"
			>
				<view
					v-for="(item, index) in goods"
					:key="index"
					:id="`scrollid${item.id}`"
					class="good"
				>
					<image
						class="good-img"
						style="width: 65px; height: 65px; background: #fff"
						:src="item.img"
						:alt="item.name"
					/>
					<view class="good-detail">
						<view class="name">{{ item.name }}</view>
						<view class="price">{{ item.price }}</view>
					</view>
				</view>
				<view class="padding-space"></view>
				<view class="reach2bottom">~~~ 到底了 ~~~</view>
			</scroll-view>
		</view>
	</view>
</template>

<script setup>
import { onMounted, ref } from "vue";
import "./index.less";

const GOOD_DIV_HEIGHT = "70";
const goods = ref();
const kinds = ref();
const toScrollViewId = ref();
const kindsTopArray = ref();
const activeKind = ref();

const scrollMenu = (e) => {
	console.log("scroll menu", e);
};

const scrollGoods = (e) => {
	const scrollTop = e.detail.scrollTop;

	let n = 0;
	let totalTop = 0;
	while (true) {
		if (kinds.value[n]) {
			if (scrollTop > totalTop + kindsTopArray.value[n]) {
				totalTop += kindsTopArray.value[n];
				n++;
			} else {
				break;
			}
		}
		break;
	}
	activeKind.value = kinds.value[n];
};

const onClickMenu = (e) => {
	console.log("onClickMenu", e);
	let scrollToElId = goods.value.find((good) => good.kind === e).id;
	toScrollViewId.value = `scrollid${scrollToElId}`;
	activeKind.value = e;
};

onMounted(() => {
	goods.value = [
		{
			id: 1,
			name: "火鸡面",
			price: 20,
			discount: 0,
			kind: "面条",
			tag: "面条",
			opts: "无葱，无辣，无香菜",
			img: "https://picsum.photos/id/1/200/300",
		},
	];
	goods.value.push(
		{
			id: 2,
			name: "牛肉面",
			price: 25,
			discount: 0,
			kind: "面条",
			tag: "面条",
			opts: "无葱，无辣，无香菜",
			img: "https://picsum.photos/id/2/200/300",
		},
		{
			id: 3,
			name: "猪肉面",
			price: 22,
			discount: 0,
			kind: "面条",
			tag: "面条",
			opts: "无葱，无辣，无香菜",
			img: "https://picsum.photos/id/3/200/300",
		},
		{
			id: 4,
			name: "鸡肉面",
			price: 23,
			discount: 0,
			kind: "面条",
			tag: "面条",
			opts: "无葱，无辣，无香菜",
			img: "https://picsum.photos/id/4/200/300",
		},
	);

	// 米饭类
	for (let i = 8; i <= 12; i++) {
		goods.value.push({
			id: i,
			name: `米饭${i}`,
			price: 18 + i,
			discount: 0,
			kind: "米饭",
			tag: "主食",
			opts: "无葱，无辣，无香菜",
			img: `https://picsum.photos/id/${i}/200/300`,
		});
	}

	// 饮料类
	for (let i = 13; i <= 17; i++) {
		goods.value.push({
			id: i,
			name: `饮料${i}`,
			price: 8 + i,
			discount: 0,
			kind: "饮料",
			tag: "冷饮",
			opts: "无糖",
			img: `https://picsum.photos/id/${i}/200/300`,
		});
	}

	// 小吃类
	for (let i = 18; i <= 22; i++) {
		goods.value.push({
			id: i,
			name: `小吃${i}`,
			price: 12 + i,
			discount: 0,
			kind: "小吃",
			tag: "零食",
			opts: "无盐",
			img: `https://picsum.photos/id/${i}/200/300`,
		});
	}

	kinds.value = [...new Set(goods.value.map((item) => item.kind))];
	kindsTopArray.value = kinds.value.map((kind) => {
		return goods.value.filter((good) => good.kind === kind).length * GOOD_DIV_HEIGHT;
	});
	activeKind.value = kinds.value[0];
});
</script>
