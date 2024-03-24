export default defineAppConfig({
	pages: ["pages/index/index", "pages/order/index"],
	window: {
		backgroundTextStyle: "light",
		navigationBarBackgroundColor: "#fff",
		navigationBarTitleText: "WeChat",
		navigationBarTextStyle: "black",
	},
	tabBar: {
		color: "#000000",
		selectedColor: "#000000",
		backgroundColor: "rgba(255, 255, 255,.7)",
    borderStyle: "black",
		list: [
			{
				pagePath: "pages/index/index",
				text: "菜单",
        iconPath:"images/home-icon.png",
        selectedIconPath:"images/home-icon-selected.png",
			},
			{
				pagePath: "pages/order/index",
				text: "已点",
        iconPath:"images/order-icon.png",
        selectedIconPath:"images/order-icon-selected.png",
			},
		],
	},
});
