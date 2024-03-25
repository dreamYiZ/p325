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
					<view class="add-to-cart">
						<view
							v-if="item.count"
							:onTap="
								() => {
									item.count--;
									reCalculateCart();
								}
							"
							>减</view
						>
						<view v-if="item.count" class="count-number">{{ item.count }}</view>
						<view :onTap="() => addToCart(item)">加</view>
					</view>
				</view>
				<view class="padding-space"></view>
				<view class="reach2bottom">~~~ 到底了 ~~~</view>
			</scroll-view>
		</view>
		<view class="cart-total">
			<view class="cart-l">
				<view :onTap="showCartDetail">总</view>
				<view v-if="totalCartMoney" class="cart-total-money">{{ totalCartMoney }}</view>
			</view>
			<view>结算</view>
		</view>
		<view class="cart-detail-box" :class="{ 'active-cart-detail': !isCartDetailShow }">
			<view class="cart-item label">
				<view class="cart-total-name">名称</view>
				<view class="cart-total-price">价格</view>
				<view class="cart-total-discount">优惠</view>
				<view class="cart-total-count">数量</view>
				<view class="cart-total-good-total">总计</view>
			</view>
			<scroll-view :scroll-y="true" style="max-height: 420px" @scroll="scrollMenu">
				<view v-for="(good, index) in goodsCounted" :key="index" class="cart-item">
					<view class="cart-total-name">{{ good.name }}</view>
					<view class="cart-total-price">{{ good.price }}</view>
					<view class="cart-total-discount">{{ good.discount }}</view>
					<view class="cart-total-count">{{ good.count }}</view>
					<view class="cart-total-good-total">{{
						Math.floor((good.price - good.discount) * good.count)
					}}</view>
				</view>
			</scroll-view>
		</view>
	</view>
</template>

<script setup>
import { onMounted, ref, nextTick } from "vue";
import "./index.less";

const GOOD_DIV_HEIGHT = 80;
const goods = ref();
const kinds = ref();
const toScrollViewId = ref();
const kindsTopArray = ref();
const activeKind = ref();

const totalCartMoney = ref();
const goodsCounted = ref();
const isCartDetailShow = ref(false);

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
				continue;
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

const addToCart = (item) => {
	if (!item.count) {
		item.count = 1;
	}

	if (item.count) {
		item.count++;
	}

	reCalculateCart();
};

const reCalculateCart = async () => {
	console.log("reCalculateCart");
	goodsCounted.value = goods.value.filter((good) => good.count > 0);
	totalCartMoney.value = goodsCounted.value.reduce((a, b) => {
		let money = Math.floor((b.price - b.discount) * b.count);
		return a + money;
	}, 0);
};

const showCartDetail = () => {
	isCartDetailShow.value = !isCartDetailShow.value;
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
