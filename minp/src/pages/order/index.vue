<template>
	<view class="page order-page">
		<view v-for="order in orders" :key="order.id" class="order">
			<text class="order-sn">订单号：{{ order.sn }}</text>
			<view class="good-info info-label">
				<text class="good-name">名称</text>
				<text class="good-price">价格</text>
				<text class="good-opts">口味</text>
				<text class="good-count">数量</text>
			</view>
			<view v-for="good in order.goods" :key="good.id" class="good">
				<image :src="good.img" class="good-img" />
				<view class="good-info">
					<text class="good-name">{{ good.name }}</text>
					<text class="good-price">{{ good.price }}</text>
					<text class="good-opts">{{ good.choice }}</text>
					<text class="good-count">{{ good.count }}</text>
				</view>
			</view>
			<view class="total-sec">
				<view class="total-r">
					<view class="money-total">{{ order.total }} 元</view>
					<view class="created-date">{{
						new Date(+order.createdDate).toLocaleString()
					}}</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script setup>
import { onMounted, ref } from "vue";
import "./index.less";

const orders = ref();

onMounted(() => {
	orders.value = [
		{
			id: "1",
			sn: "1",
			goods: [
				{
					id: 2,
					name: "牛肉面",
					price: 25,
					discount: 0,
					kind: "面条",
					tag: "面条",
					opts: "无葱，无辣，无香菜",
					img: "https://picsum.photos/id/2/200/300",
					count: 1,
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
					count: 1,
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
					count: 1,
				},
			],
			total: 198,
			createdDate: new Date(2024, 3, 26, 17, 36, 52),
		},
		{
			id: "1",
			sn: "1",
			goods: [
				{
					id: 2,
					name: "牛肉面",
					price: 25,
					discount: 0,
					kind: "面条",
					tag: "面条",
					opts: "无葱，无辣，无香菜",
					img: "https://picsum.photos/id/2/200/300",
					count: 1,
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
					count: 1,
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
					count: 1,
				},
			],
			total: 198,
			createdDate: new Date(2024, 3, 26, 17, 36, 52),
		},
    {
			id: "1",
			sn: "1",
			goods: [
				{
					id: 2,
					name: "牛肉面",
					price: 25,
					discount: 0,
					kind: "面条",
					tag: "面条",
					opts: "无葱，无辣，无香菜",
					img: "https://picsum.photos/id/2/200/300",
					count: 1,
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
					count: 1,
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
					count: 1,
				},
			],
			total: 198,
			createdDate: new Date(2024, 3, 26, 17, 36, 52),
		},
		{
			id: "1",
			sn: "1",
			goods: [
				{
					id: 2,
					name: "牛肉面",
					price: 25,
					discount: 0,
					kind: "面条",
					tag: "面条",
					opts: "无葱，无辣，无香菜",
					img: "https://picsum.photos/id/2/200/300",
					count: 1,
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
					count: 1,
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
					count: 1,
				},
			],
			total: 198,
			createdDate: new Date(2024, 3, 26, 17, 36, 52),
		},
    {
			id: "1",
			sn: "1",
			goods: [
				{
					id: 2,
					name: "牛肉面",
					price: 25,
					discount: 0,
					kind: "面条",
					tag: "面条",
					opts: "无葱，无辣，无香菜",
					img: "https://picsum.photos/id/2/200/300",
					count: 1,
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
					count: 1,
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
					count: 1,
				},
			],
			total: 198,
			createdDate: new Date(2024, 3, 26, 17, 36, 52),
		},
		{
			id: "1",
			sn: "1",
			goods: [
				{
					id: 2,
					name: "牛肉面",
					price: 25,
					discount: 0,
					kind: "面条",
					tag: "面条",
					opts: "无葱，无辣，无香菜",
					img: "https://picsum.photos/id/2/200/300",
					count: 1,
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
					count: 1,
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
					count: 1,
				},
			],
			total: 198,
			createdDate: new Date(2024, 3, 26, 17, 36, 52),
		},
	];
});
</script>







