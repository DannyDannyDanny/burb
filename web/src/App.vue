<template>
	<div class="app">
		<!-- <img alt="Vue logo" src="./assets/logo.png"> -->
		<HelloWorld msg="Welcome to Burb 🦜" />
		<audio-uploader />
	</div>
</template>

<script>
import AudioUploader from "./components/AudioUploader.vue";
import HelloWorld from "./components/HelloWorld.vue";

export default {
	name: "App",
	components: {
		HelloWorld,
		AudioUploader,
	},
};
</script>

<style>
</style>
